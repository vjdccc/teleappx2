package com.zahid.bot

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.Service
import android.content.Context
import android.content.Intent
import android.content.pm.ServiceInfo
import android.os.Build
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.os.PowerManager
import android.os.Process
import android.util.Log
import androidx.core.app.NotificationCompat
import com.chaquo.python.Python
import java.io.File
import kotlin.concurrent.thread

/** خدمة امامية تشغّل بوت بايثون وتبقيه حياً. */
class BotService : Service() {

    companion object {
        const val ACTION_STOP = "com.zahid.bot.STOP"
        private const val CHANNEL = "zahid_bot"
        private const val NOTIF_ID = 1
        private const val TAG = "ZahidBot"

        @Volatile var running = false
        @Volatile private var instance: BotService? = null

        /** تستدعيها بايثون بدل os._exit: 42 = ايقاف نهائي، غيره = اعادة تشغيل. */
        @JvmStatic
        fun requestExit(code: Int) {
            val svc = instance ?: return
            Handler(Looper.getMainLooper()).post {
                if (code == 42) {
                    Prefs.setWantRunning(svc, false)
                    svc.shutdown()
                } else {
                    // قتل العملية؛ START_STICKY يعيد تشغيل الخدمة تلقائياً
                    svc.releaseWake()
                    Handler(Looper.getMainLooper()).postDelayed({ Process.killProcess(Process.myPid()) }, 500)
                }
            }
        }
    }

    @Volatile private var stopping = false
    private var worker: Thread? = null
    private var wake: PowerManager.WakeLock? = null

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        instance = this
        if (intent?.action == ACTION_STOP) {
            Prefs.setWantRunning(this, false)
            shutdown()
            return START_NOT_STICKY
        }
        // intent == null يعني ان النظام اعاد الخدمة بعد قتلها
        if (intent == null && !Prefs.wantRunning(this)) {
            stopSelf()
            return START_NOT_STICKY
        }
        goForeground()
        Prefs.setWantRunning(this, true)
        startWorker()
        return START_STICKY
    }

    private fun goForeground() {
        val nm = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        if (Build.VERSION.SDK_INT >= 26) {
            nm.createNotificationChannel(
                NotificationChannel(CHANNEL, "Telethon Zahid", NotificationManager.IMPORTANCE_LOW)
            )
        }
        val open = PendingIntent.getActivity(
            this, 0, Intent(this, MainActivity::class.java),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )
        val stop = PendingIntent.getService(
            this, 1, Intent(this, BotService::class.java).setAction(ACTION_STOP),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )
        val n: Notification = NotificationCompat.Builder(this, CHANNEL)
            .setSmallIcon(R.drawable.ic_notif)
            .setContentTitle(getString(R.string.notif_title))
            .setContentText(getString(R.string.notif_text))
            .setContentIntent(open)
            .setColor(0xFF00F0FF.toInt())
            .setOngoing(true)
            .addAction(0, getString(R.string.notif_stop), stop)
            .build()
        if (Build.VERSION.SDK_INT >= 34) {
            startForeground(NOTIF_ID, n, ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE)
        } else {
            startForeground(NOTIF_ID, n)
        }
        if (wake == null) {
            val pm = getSystemService(Context.POWER_SERVICE) as PowerManager
            wake = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "zahid:bot").apply { acquire() }
        }
    }

    private fun startWorker() {
        if (worker?.isAlive == true) return
        running = true
        worker = thread(name = "zahid-python", isDaemon = true) {
            try {
                PyHelper.ensure(applicationContext)
                Python.getInstance().getModule("android_runner")
                    .callAttr("run", Prefs.toJson(applicationContext), filesDir.absolutePath)
            } catch (t: Throwable) {
                Log.e(TAG, "python crashed", t)
                try {
                    File(filesDir, "zahid.log").appendText("\n[خطأ في التشغيل] ${t.message}\n")
                } catch (_: Exception) {}
            } finally {
                running = false
                // اذا انتهى بايثون من تلقاء نفسه (خطأ) لا نبقي خدمة فارغة
                Handler(Looper.getMainLooper()).post { if (instance === this) shutdown() }
            }
        }
    }

    private fun stopPython() {
        try {
            if (Python.isStarted()) {
                Python.getInstance().getModule("android_runner").callAttr("stop")
            }
        } catch (_: Throwable) {}
        worker?.join(8000)
    }

    private fun releaseWake() {
        try { wake?.takeIf { it.isHeld }?.release() } catch (_: Exception) {}
        wake = null
    }

    private fun shutdown() {
        if (stopping) return
        stopping = true
        // الايقاف في خيط جانبي حتى لا نجمّد الواجهة
        thread(name = "zahid-stop") {
            stopPython()
            Handler(Looper.getMainLooper()).post {
                releaseWake()
                running = false
                stopForeground(STOP_FOREGROUND_REMOVE)
                stopSelf()
                // ننهي العملية ليبدأ التشغيل القادم نظيفاً (مكتبات بايثون لا تُعاد تحميلها)
                Handler(Looper.getMainLooper()).postDelayed({ Process.killProcess(Process.myPid()) }, 700)
            }
        }
    }

    override fun onDestroy() {
        releaseWake()
        if (instance === this) instance = null
        super.onDestroy()
    }
}
