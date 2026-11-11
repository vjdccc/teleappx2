# -*- coding: utf-8 -*-
# Telethon Zahid - اوامر النظام (بنك / مدة التشغيل / اعاده تشغيل / ايقاف / الاوامر)
import os
import time
from arabcompat import *
from config import app, bot_user

plugin_category = "tools"
_START = time.time()


def _fmt(sec):
    sec = int(sec)
    d, sec = divmod(sec, 86400)
    h, sec = divmod(sec, 3600)
    m, s = divmod(sec, 60)
    parts = []
    if d: parts.append(f"{d} يوم")
    if h: parts.append(f"{h} ساعه")
    if m: parts.append(f"{m} دقيقه")
    parts.append(f"{s} ثانيه")
    return " و ".join(parts)


@zahid.on(admin_cmd(pattern="بنك$"))
async def _ping(event):
    t = time.time()
    await event.edit("• جاري القياس ..")
    await event.edit(f"• سرعة الاستجابه : {(time.time() - t) * 1000:.0f} ms")


@zahid.on(admin_cmd(pattern="مدة التشغيل$"))
async def _uptime(event):
    await event.edit(f"• السورس شغال منذ : {_fmt(time.time() - _START)}")


@zahid.on(admin_cmd(pattern="(?:اعاده|اعادة) تشغيل$"))
async def _restart(event):
    await event.edit("• جاري اعادة التشغيل ..")
    os._exit(0)  # المشغّل يعيد التشغيل تلقائياً


@zahid.on(admin_cmd(pattern="ايقاف$"))
async def _stop(event):
    await event.edit("• تم ايقاف السورس")
    os._exit(42)  # 42 = ايقاف نهائي بدون اعادة تشغيل


@zahid.on(admin_cmd(pattern="(?:الاوامر|اوامر)$"))
async def _menu(event):
    chat = event.chat_id
    try:
        res = await app.get_inline_bot_results(bot_user, query="الاوامر")
        await event.delete()
        await app.send_inline_bot_result(chat, res.query_id, res.results[0].id)
    except Exception:
        await event.edit("• فعل الانلاين من @BotFather")
