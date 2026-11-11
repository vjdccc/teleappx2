package com.zahid.bot

import android.content.Context
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import org.json.JSONObject

/** جسر استدعاء ادوات بايثون (setup_helper). يُستدعى دائماً من خيط خلفي. */
object PyHelper {
    @Synchronized
    fun ensure(ctx: Context) {
        if (!Python.isStarted()) Python.start(AndroidPlatform(ctx.applicationContext))
    }

    fun call(ctx: Context, fn: String, vararg args: Any?): JSONObject {
        ensure(ctx)
        val out = Python.getInstance().getModule("setup_helper").callAttr(fn, *args).toString()
        return JSONObject(out)
    }
}
