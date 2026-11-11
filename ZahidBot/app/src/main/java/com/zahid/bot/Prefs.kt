package com.zahid.bot

import android.content.Context
import android.content.SharedPreferences
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKey
import org.json.JSONObject

/** بيانات الحساب مشفّرة (Android Keystore)، وحالة التشغيل في ملف عادي. */
object Prefs {
    val FIELDS = listOf("api_id", "api_hash", "session", "token", "bot_user", "sudo_id")

    private fun secure(c: Context): SharedPreferences {
        val key = MasterKey.Builder(c).setKeyScheme(MasterKey.KeyScheme.AES256_GCM).build()
        return EncryptedSharedPreferences.create(
            c, "zahid_secure", key,
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )
    }

    private fun state(c: Context): SharedPreferences =
        c.getSharedPreferences("zahid_state", Context.MODE_PRIVATE)

    fun get(c: Context, k: String): String = secure(c).getString(k, "") ?: ""

    fun save(c: Context, values: Map<String, String>) {
        val e = secure(c).edit()
        values.forEach { (k, v) -> e.putString(k, v.trim()) }
        e.apply()
    }

    /** يرجع نص الخطأ بالعربي او null اذا كانت البيانات سليمة. */
    fun validate(v: Map<String, String>): String? {
        val apiId = v["api_id"].orEmpty().trim()
        if (apiId.isEmpty() || !apiId.all { it.isDigit() }) return "API ID يجب ان يكون ارقاماً فقط"
        if (v["api_hash"].orEmpty().trim().length < 20) return "API HASH غير صحيح"
        if (v["session"].orEmpty().trim().length < 50) return "Session String غير صحيح (قصير جداً)"
        if (!Regex("^\\d+:[A-Za-z0-9_-]{20,}$").matches(v["token"].orEmpty().trim())) return "Bot Token غير صحيح"
        val bu = v["bot_user"].orEmpty().trim()
        if (bu.isEmpty() || bu.startsWith("@") || bu.contains(" ")) return "يوزر البوت يكتب بدون @ وبدون مسافات"
        val sudo = v["sudo_id"].orEmpty().trim()
        if (sudo.isEmpty() || !sudo.all { it.isDigit() }) return "ايدي المالك يجب ان يكون ارقاماً فقط"
        return null
    }

    fun toJson(c: Context): String {
        val o = JSONObject()
        FIELDS.forEach { o.put(it, get(c, it)) }
        return o.toString()
    }

    fun isConfigured(c: Context): Boolean = validate(FIELDS.associateWith { get(c, it) }) == null

    fun onboarded(c: Context): Boolean = state(c).getBoolean("onboarded", false)
    fun setOnboarded(c: Context, v: Boolean) = state(c).edit().putBoolean("onboarded", v).apply()

    fun wantRunning(c: Context): Boolean = state(c).getBoolean("want_running", false)
    fun setWantRunning(c: Context, v: Boolean) = state(c).edit().putBoolean("want_running", v).apply()

    fun autoStart(c: Context): Boolean = state(c).getBoolean("auto_start", false)
    fun setAutoStart(c: Context, v: Boolean) = state(c).edit().putBoolean("auto_start", v).apply()
}
