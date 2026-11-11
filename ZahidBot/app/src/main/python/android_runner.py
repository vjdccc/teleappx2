# -*- coding: utf-8 -*-
"""جسر بين تطبيق اندرويد وبوت Telethon Zahid.

يستدعيه BotService:   android_runner.run(config_json, files_dir)   <- يبقى شغالاً حتى stop()
                      android_runner.stop()
"""
import asyncio
import json
import os
import shutil
import signal
import sys
import threading
import time
import traceback

import zloop

_state = {"loop": None, "stop": None}


# ───────────── السجل: stdout/stderr الى ملف تقرأه الواجهة ─────────────
class _LogFile:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        if os.path.exists(path) and os.path.getsize(path) > 512 * 1024:
            os.remove(path)  # لا يكبر السجل بلا حدود
        self.f = open(path, "a", encoding="utf-8", buffering=1)

    def write(self, s):
        if not s:
            return 0
        with self.lock:
            self.f.write(s)
        return len(s)

    def flush(self):
        with self.lock:
            self.f.flush()

    def isatty(self):
        return False


# ───────────── تجهيز المجلد والملفات ─────────────
def _config_text(c):
    return f'''from pyrogram import Client,filters,enums
import fakeredis
r = fakeredis.FakeRedis(decode_responses=True)

sudo_id = {int(c["sudo_id"])}
bot_user = {c["bot_user"]!r}
api_id = {int(c["api_id"])}
api_hash = {c["api_hash"]!r}
session = {c["session"]!r}
token = {c["token"]!r}
sudo_command = [{int(c["sudo_id"])}]
pm = {str(c["sudo_id"])!r}
mention = {str(c["sudo_id"])!r}
plugins = dict(root="plugins")
app = Client("user:" + bot_user, api_id, api_hash, in_memory=True, session_string=session, plugins=plugins)
bot = Client(bot_user, api_id=api_id, api_hash=api_hash, bot_token=token, plugins=dict(root="plug_bot"))
'''


def _prepare(cfg, base):
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "zahid_source")
    run = os.path.join(base, "zahid_run")
    os.makedirs(run, exist_ok=True)
    # ننسخ الاكواد في كل تشغيل (تحديث التطبيق = تحديث الاكواد) ونبقي بيانات المستخدم (temp, data.json)
    for name in os.listdir(src):
        s, d = os.path.join(src, name), os.path.join(run, name)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    with open(os.path.join(run, "config.py"), "w", encoding="utf-8") as f:
        f.write(_config_text(cfg))
    os.makedirs(os.path.join(run, "temp"), exist_ok=True)
    os.chdir(run)
    if run not in sys.path:
        sys.path.insert(0, run)
    return run


def _patch_process():
    """اشياء تقتل تطبيق اندرويد او تفشل خارج الخيط الرئيسي."""
    orig = signal.signal

    def safe_signal(sig, handler):
        try:
            return orig(sig, handler)
        except ValueError:  # ليس الخيط الرئيسي
            return None
    signal.signal = safe_signal

    def android_exit(code=0):  # اوامر (ايقاف / اعاده تشغيل) تستدعي os._exit
        try:
            from java import jclass
            jclass("com.zahid.bot.BotService").requestExit(int(code))
        except Exception:
            traceback.print_exc()
    os._exit = android_exit


async def _main():
    from config import app, bot
    await app.start()
    await bot.start()
    print("✅ البوت شغّال")
    try:
        from arabcompat import start_background
        start_background()
    except Exception as e:
        print("background:", e)
    await _state["stop"].wait()
    for c in (bot, app):
        try:
            await c.stop()
        except Exception:
            pass
    print("تم ايقاف البوت")


async def _make_event():
    return asyncio.Event()


def run(config_json, files_dir):
    """يُستدعى من خيط في الخدمة؛ يبقى شغالاً حتى stop(). كل العمل على الحلقة المشتركة (zloop)."""
    sys.stdout = sys.stderr = _LogFile(os.path.join(files_dir, "zahid.log"))
    print("=" * 30, time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        cfg = json.loads(config_json)
        _prepare(cfg, files_dir)
        _patch_process()
        _state["loop"] = zloop.get_loop()
        _state["stop"] = zloop.run_coro(_make_event())
        zloop.run_coro(_main())
    except BaseException:
        traceback.print_exc()
        raise
    finally:
        sys.stdout.flush()


def stop():
    loop, ev = _state.get("loop"), _state.get("stop")
    if loop and ev:
        loop.call_soon_threadsafe(ev.set)
