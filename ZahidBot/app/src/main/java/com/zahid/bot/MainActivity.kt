package com.zahid.bot

import android.Manifest
import android.annotation.SuppressLint
import android.app.AlertDialog
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.PowerManager
import android.provider.Settings
import android.text.InputType
import android.widget.EditText
import android.widget.FrameLayout
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.google.android.material.switchmaterial.SwitchMaterial
import com.google.android.material.textfield.TextInputEditText
import java.io.File
import java.io.RandomAccessFile
import kotlin.concurrent.thread
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    private lateinit var fields: Map<String, TextInputEditText>
    private lateinit var tvStatus: TextView
    private lateinit var tvNotif: TextView
    private lateinit var tvBattery: TextView
    private lateinit var tvLog: TextView
    private lateinit var btnStart: Button
    private lateinit var btnStop: Button
    private lateinit var btnNotif: Button
    private lateinit var btnBattery: Button
    private lateinit var swBoot: SwitchMaterial

    private val handler = Handler(Looper.getMainLooper())
    private var afterNotifGranted: (() -> Unit)? = null
    private var onboardingNext: (() -> Unit)? = null

    private val notifLauncher =
        registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
            refresh()
            if (granted) afterNotifGranted?.invoke()
            else Toast.makeText(this, "بدون الاشعارات قد يقتل النظام البوت", Toast.LENGTH_LONG).show()
            afterNotifGranted = null
            onboardingNext?.invoke()   // يكمل خطوات اول تشغيل سواء وافق ام رفض
            onboardingNext = null
        }

    private val ticker = object : Runnable {
        override fun run() {
            refresh()
            handler.postDelayed(this, 2000)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        fields = mapOf(
            "api_id" to findViewById<TextInputEditText>(R.id.etApiId),
            "api_hash" to findViewById<TextInputEditText>(R.id.etApiHash),
            "session" to findViewById<TextInputEditText>(R.id.etSession),
            "token" to findViewById<TextInputEditText>(R.id.etToken),
            "bot_user" to findViewById<TextInputEditText>(R.id.etBotUser),
            "sudo_id" to findViewById<TextInputEditText>(R.id.etSudoId),
        )
        tvStatus = findViewById<TextView>(R.id.tvStatus)
        tvNotif = findViewById<TextView>(R.id.tvNotif)
        tvBattery = findViewById<TextView>(R.id.tvBattery)
        tvLog = findViewById<TextView>(R.id.tvLog)
        btnStart = findViewById<Button>(R.id.btnStart)
        btnStop = findViewById<Button>(R.id.btnStop)
        btnNotif = findViewById<Button>(R.id.btnNotif)
        btnBattery = findViewById<Button>(R.id.btnBattery)
        swBoot = findViewById<SwitchMaterial>(R.id.swBoot)

        // تحميل القيم المحفوظة
        fields.forEach { (k, v) -> v.setText(Prefs.get(this, k)) }
        swBoot.isChecked = Prefs.autoStart(this)

        findViewById<Button>(R.id.btnSave).setOnClickListener { saveAndValidate(true) }
        btnNotif.setOnClickListener { requestNotifications(null) }
        btnBattery.setOnClickListener { requestBatteryExemption() }
        swBoot.setOnCheckedChangeListener { _, on -> Prefs.setAutoStart(this, on) }
        btnStart.setOnClickListener { startBot() }
        btnStop.setOnClickListener {
            startService(Intent(this, BotService::class.java).setAction(BotService.ACTION_STOP))
        }

        findViewById<Button>(R.id.btnHelpApi).setOnClickListener { showApiHelp() }
        findViewById<Button>(R.id.btnGetSession).setOnClickListener { extractSession() }
        findViewById<Button>(R.id.btnMakeBot).setOnClickListener { makeBot() }
        findViewById<Button>(R.id.btnFetchBot).setOnClickListener { fetchBotUser() }
        findViewById<Button>(R.id.btnDev).setOnClickListener {
            AlertDialog.Builder(this)
                .setTitle("المطور")
                .setMessage("تطوير: زاهد\n\n© 2026 زاهد — جميع الحقوق محفوظة")
                .setPositiveButton("حسناً", null)
                .show()
        }

        if (!Prefs.onboarded(this)) firstRun()
    }

    override fun onResume() {
        super.onResume()
        handler.post(ticker)
    }

    override fun onPause() {
        handler.removeCallbacks(ticker)
        super.onPause()
    }

    // ───────────── اول تشغيل: يشرح المطلوب ثم يطلب الصلاحيات بالترتيب ─────────────
    private fun firstRun() {
        AlertDialog.Builder(this)
            .setTitle("اهلاً بك")
            .setMessage(
                "لتشغيل البوت يحتاج التطبيق:\n\n" +
                "١) بيانات حسابك (API ID/HASH، الجلسة، توكن البوت، يوزر البوت، ايدي المالك)\n" +
                "٢) السماح بالاشعارات (لابقاء البوت شغالاً في الخلفية)\n" +
                "٣) الغاء قيود البطارية عن التطبيق\n\n" +
                "سنطلب الصلاحيات الآن، ثم املأ البيانات واضغط حفظ."
            )
            .setCancelable(false)
            .setPositiveButton("متابعة") { _, _ ->
                if (notifGranted()) {
                    askBatteryThenFinish()
                } else {
                    onboardingNext = { askBatteryThenFinish() }
                    notifLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
                }
            }
            .show()
    }

    private fun askBatteryThenFinish() {
        Prefs.setOnboarded(this, true)
        if (!isBatteryExempt()) requestBatteryExemption()
    }

    // ───────────── الصلاحيات ─────────────
    private fun notifGranted(): Boolean =
        Build.VERSION.SDK_INT < 33 ||
            ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) ==
            PackageManager.PERMISSION_GRANTED

    private fun requestNotifications(then: (() -> Unit)?) {
        if (notifGranted()) { then?.invoke(); return }
        afterNotifGranted = then
        notifLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
    }

    private fun isBatteryExempt(): Boolean =
        (getSystemService(Context.POWER_SERVICE) as PowerManager).isIgnoringBatteryOptimizations(packageName)

    @SuppressLint("BatteryLife")
    private fun requestBatteryExemption() {
        try {
            startActivity(
                Intent(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
                    .setData(Uri.parse("package:$packageName"))
            )
        } catch (e: Exception) {
            startActivity(Intent(Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS))
        }
    }

    // ───────────── الحفظ والتشغيل ─────────────
    private fun currentValues(): Map<String, String> =
        fields.mapValues { it.value.text?.toString().orEmpty().trim() }

    private fun saveAndValidate(toast: Boolean): Boolean {
        val values = currentValues()
        val err = Prefs.validate(values)
        if (err != null) {
            Toast.makeText(this, err, Toast.LENGTH_LONG).show()
            return false
        }
        Prefs.save(this, values)
        if (toast) Toast.makeText(this, "تم الحفظ", Toast.LENGTH_SHORT).show()
        return true
    }

    private fun startBot() {
        if (!saveAndValidate(false)) return
        requestNotifications {
            ContextCompat.startForegroundService(this, Intent(this, BotService::class.java))
            Toast.makeText(this, "جاري التشغيل ...", Toast.LENGTH_SHORT).show()
        }
    }

    // ───────────── استخراج المتطلبات من داخل التطبيق ─────────────
    private fun toast(m: String) = Toast.makeText(this, m, Toast.LENGTH_LONG).show()

    private fun fieldText(k: String): String = fields[k]!!.text?.toString().orEmpty().trim()

    private fun busy(msg: String): AlertDialog =
        AlertDialog.Builder(this).setMessage(msg).setCancelable(false).create().also { it.show() }

    /** ينفّذ work في خيط خلفي مع نافذة انتظار، ثم يستدعي done في الواجهة. */
    private fun runBg(msg: String, work: () -> JSONObject, done: (JSONObject) -> Unit) {
        val d = busy(msg)
        thread(name = "zahid-helper") {
            val r = try {
                work()
            } catch (e: Throwable) {
                JSONObject().put("ok", false).put("msg", e.message ?: e.toString())
            }
            runOnUiThread { d.dismiss(); done(r) }
        }
    }

    private fun askText(title: String, hint: String, inputType: Int, onOk: (String) -> Unit) {
        val input = EditText(this).apply {
            this.hint = hint
            this.inputType = inputType
            setSingleLine()
        }
        val pad = (16 * resources.displayMetrics.density).toInt()
        val box = FrameLayout(this).apply {
            setPadding(pad, pad / 2, pad, 0)
            addView(input)
        }
        AlertDialog.Builder(this)
            .setTitle(title)
            .setView(box)
            .setPositiveButton("متابعة") { _, _ ->
                val t = input.text.toString().trim()
                if (t.isNotEmpty()) onOk(t)
            }
            .setNegativeButton("الغاء", null)
            .show()
    }

    private fun showApiHelp() {
        AlertDialog.Builder(this)
            .setTitle("API ID و API HASH")
            .setMessage(
                "تيليجرام يعطيها من موقعه الرسمي ولا يمكن استخراجها تلقائياً:\n\n" +
                "١) افتح my.telegram.org وسجّل دخول برقمك\n" +
                "٢) اختر API development tools\n" +
                "٣) املأ اسم وعنوان قصير لأي تطبيق ثم Create\n" +
                "٤) انسخ App api_id و App api_hash الى الحقول هنا"
            )
            .setPositiveButton("فتح الموقع") { _, _ ->
                try {
                    startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://my.telegram.org")))
                } catch (e: Exception) { toast("افتح my.telegram.org من المتصفح") }
            }
            .setNegativeButton("اغلاق", null)
            .show()
    }

    private fun apiPair(): Pair<Int, String>? {
        val id = fieldText("api_id")
        val hash = fieldText("api_hash")
        if (id.isEmpty() || !id.all { it.isDigit() } || hash.length < 20) {
            toast("املأ API ID و API HASH اولاً")
            return null
        }
        return Pair(id.toInt(), hash)
    }

    private fun extractSession() {
        val (id, hash) = apiPair() ?: return
        askText("رقم هاتفك", "مع رمز الدولة مثل +9647701234567", InputType.TYPE_CLASS_PHONE) { phone ->
            runBg("جاري طلب الكود ...", { PyHelper.call(this, "send_code", id, hash, phone) }) { r ->
                if (!r.optBoolean("ok")) { toast(r.optString("msg")); return@runBg }
                askText("الكود", "الكود الذي وصلك في تيليجرام", InputType.TYPE_CLASS_NUMBER) { code ->
                    runBg("جاري التحقق ...", { PyHelper.call(this, "sign_in", code) }) { afterLogin(it) }
                }
            }
        }
    }

    private fun afterLogin(r: JSONObject) {
        if (!r.optBoolean("ok")) { toast(r.optString("msg")); return }
        if (r.optBoolean("need_password")) {
            askText(
                "كلمة سر التحقق بخطوتين", "كلمة السر",
                InputType.TYPE_CLASS_TEXT or InputType.TYPE_TEXT_VARIATION_PASSWORD
            ) { pw ->
                runBg("جاري التحقق ...", { PyHelper.call(this, "check_password", pw) }) { afterLogin(it) }
            }
            return
        }
        fields["session"]!!.setText(r.optString("session"))
        fields["sudo_id"]!!.setText(r.optLong("user_id").toString())
        toast("تم استخراج الجلسة وايدي المالك ✅ — اضغط حفظ")
    }

    private fun makeBot() {
        val (id, hash) = apiPair() ?: return
        val session = fieldText("session")
        if (session.length < 50) { toast("استخرج الجلسة اولاً"); return }
        askText("اسم البوت", "مثال: بوت زاهد", InputType.TYPE_CLASS_TEXT) { name ->
            askText("يوزر البوت", "ينتهي بـ bot مثل zahid_bot", InputType.TYPE_CLASS_TEXT) { user ->
                val u = user.removePrefix("@")
                if (!Regex("^[A-Za-z][A-Za-z0-9_]{3,30}[Bb]ot$").matches(u)) {
                    toast("اليوزر لازم يكون انجليزي وينتهي بـ bot")
                    return@askText
                }
                runBg("جاري انشاء البوت عبر BotFather (قد يأخذ نصف دقيقة) ...",
                    { PyHelper.call(this, "create_bot", session, id, hash, name, u) }) { r ->
                    if (!r.optBoolean("ok")) { toast(r.optString("msg")); return@runBg }
                    fields["token"]!!.setText(r.optString("token"))
                    fields["bot_user"]!!.setText(r.optString("bot_user"))
                    toast("تم انشاء البوت ✅ — اضغط حفظ")
                }
            }
        }
    }

    private fun fetchBotUser() {
        val token = fieldText("token")
        if (token.isEmpty()) { toast("الصق التوكن في حقله اولاً"); return }
        runBg("جاري الجلب ...", { PyHelper.call(this, "fetch_bot", token) }) { r ->
            if (!r.optBoolean("ok")) { toast(r.optString("msg")); return@runBg }
            fields["bot_user"]!!.setText(r.optString("bot_user"))
            toast("تم جلب اليوزر ✅")
        }
    }

    // ───────────── تحديث الواجهة والسجل ─────────────
    private fun c(id: Int) = ContextCompat.getColor(this, id)

    private fun refresh() {
        val running = BotService.running
        tvStatus.text = if (running) "الحالة: ● شغّال" else "الحالة: ○ متوقف"
        tvStatus.setTextColor(c(if (running) R.color.cp_green else R.color.cp_magenta))
        btnStart.isEnabled = !running
        btnStop.isEnabled = running
        val notif = notifGranted()
        tvNotif.text = if (notif) "الاشعارات: ● مسموحة" else "الاشعارات: ○ غير مسموحة"
        tvNotif.setTextColor(c(if (notif) R.color.cp_green else R.color.cp_magenta))
        btnNotif.isEnabled = !notif
        val bat = isBatteryExempt()
        tvBattery.text = if (bat) "قيود البطارية: ● ملغاة" else "قيود البطارية: ○ مفعّلة (قد يوقف النظام البوت)"
        tvBattery.setTextColor(c(if (bat) R.color.cp_green else R.color.cp_magenta))
        btnBattery.isEnabled = !bat
        tvLog.text = readLogTail()
    }

    private fun readLogTail(): String {
        val f = File(filesDir, "zahid.log")
        if (!f.exists()) return "لا يوجد سجل بعد."
        return try {
            RandomAccessFile(f, "r").use { raf ->
                val n = minOf(raf.length(), 6000L).toInt()
                raf.seek(raf.length() - n)
                val buf = ByteArray(n)
                raf.readFully(buf)
                String(buf, Charsets.UTF_8)
            }
        } catch (e: Exception) { "" }
    }
}
