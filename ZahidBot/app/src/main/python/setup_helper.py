# -*- coding: utf-8 -*-
"""ادوات استخراج المتطلبات من داخل التطبيق. كل الدوال ترجع JSON نصياً: {"ok": bool, "msg": ...}.

لا يُحفظ رقم الهاتف ولا الكود ولا كلمة السر؛ الناتج الوحيد هو الجلسة (يحفظها التطبيق مشفّرة).
"""
import asyncio
import json
import re
import time
import urllib.request

import zloop

_st = {}

_ERRORS = {
    "ApiIdInvalid": "API ID او API HASH غير صحيح",
    "PhoneNumberInvalid": "رقم الهاتف غير صحيح (اكتبه مع رمز الدولة مثل +9647...)",
    "PhoneNumberBanned": "هذا الرقم محظور من تيليجرام",
    "PhoneCodeInvalid": "الكود خاطئ",
    "PhoneCodeExpired": "انتهت صلاحية الكود، اعد المحاولة من البداية",
    "PasswordHashInvalid": "كلمة سر التحقق بخطوتين خاطئة",
    "SessionPasswordNeeded": "الحساب محمي بكلمة سر (تحقق بخطوتين)",
}


def _err(e):
    name = type(e).__name__
    if name.startswith("FloodWait"):
        return f"محاولات كثيرة، انتظر {getattr(e, 'value', '')} ثانية ثم حاول مجدداً"
    return _ERRORS.get(name) or f"{name}: {e}"


def _out(ok, **kw):
    return json.dumps(dict(ok=ok, **kw), ensure_ascii=False)


async def _drop_client():
    c = _st.pop("client", None)
    if c is not None:
        try:
            await c.disconnect()
        except Exception:
            pass


# ───────────── تسجيل الدخول واستخراج الجلسة ─────────────
async def _send_code(api_id, api_hash, phone):
    from pyrogram import Client
    await _drop_client()
    c = Client("zsetup", api_id=int(api_id), api_hash=api_hash, in_memory=True)
    await c.connect()
    sent = await c.send_code(phone)
    _st.update(client=c, phone=phone, hash=sent.phone_code_hash)


async def _finish():
    c = _st["client"]
    session = await c.export_session_string()
    me = await c.get_me()
    await _drop_client()
    return dict(session=session, user_id=me.id, name=me.first_name or "")


async def _sign_in(code):
    from pyrogram.errors import SessionPasswordNeeded
    c = _st["client"]
    try:
        await c.sign_in(_st["phone"], _st["hash"], code)
    except SessionPasswordNeeded:
        return dict(need_password=True)
    return await _finish()


async def _check_password(pw):
    await _st["client"].check_password(pw)
    return await _finish()


def send_code(api_id, api_hash, phone):
    try:
        zloop.run_coro(_send_code(api_id, api_hash, phone), 60)
        return _out(True)
    except Exception as e:
        return _out(False, msg=_err(e))


def sign_in(code):
    try:
        if "client" not in _st:
            return _out(False, msg="ابدأ من جديد: اطلب الكود مرة اخرى")
        return _out(True, **zloop.run_coro(_sign_in(code.replace(" ", "")), 60))
    except Exception as e:
        return _out(False, msg=_err(e))


def check_password(pw):
    try:
        return _out(True, **zloop.run_coro(_check_password(pw), 60))
    except Exception as e:
        return _out(False, msg=_err(e))


# ───────────── انشاء بوت عبر @BotFather ─────────────
_TOKEN = re.compile(r"\d{6,}:[A-Za-z0-9_-]{30,}")


async def _create_bot(session, api_id, api_hash, name, username):
    from pyrogram import Client
    async with Client("zsetup_bot", api_id=int(api_id), api_hash=api_hash,
                      session_string=session, in_memory=True) as c:

        async def ask(text, wait=25):
            sent = await c.send_message("BotFather", text)
            t0 = time.time()
            while time.time() - t0 < wait:
                await asyncio.sleep(1.5)
                async for m in c.get_chat_history("BotFather", limit=5):
                    if m.id > sent.id and not m.outgoing:
                        return m.text or ""
            return ""

        r = await ask("/newbot")
        if "name" not in r.lower() and "اسم" not in r:
            return dict(ok=False, msg="رد BotFather: " + (r or "لا يوجد رد"))
        await ask(name)
        r = await ask(username)
        m = _TOKEN.search(r)
        if not m:
            await c.send_message("BotFather", "/cancel")
            return dict(ok=False, msg="رد BotFather: " + (r or "لا يوجد رد"))
        return dict(ok=True, token=m.group(0), bot_user=username)


def create_bot(session, api_id, api_hash, name, username):
    try:
        res = zloop.run_coro(_create_bot(session, api_id, api_hash, name, username), 120)
        return json.dumps(res, ensure_ascii=False)
    except Exception as e:
        return _out(False, msg=_err(e))


# ───────────── جلب يوزر البوت من التوكن ─────────────
def fetch_bot(token):
    try:
        with urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getMe", timeout=20) as r:
            data = json.loads(r.read().decode("utf-8"))
        if not data.get("ok"):
            return _out(False, msg="التوكن غير صحيح")
        return _out(True, bot_user=data["result"]["username"])
    except urllib.error.HTTPError as e:
        return _out(False, msg="التوكن غير صحيح" if e.code in (401, 404) else f"خطأ {e.code}")
    except Exception as e:
        return _out(False, msg=f"تعذر الاتصال: {e}")
