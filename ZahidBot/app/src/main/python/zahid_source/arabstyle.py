# -*- coding: utf-8 -*-
"""ستايل الردود (على طريقة Telethon Zahid) + تخزين بسيط في ملف JSON + دوال مشتركة."""
import json
import os
import re
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "styles")

MARK = "🝳 ⦙"
LINE = "★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★"


def st(text):
    """رد بالستايل: **🝳 ⦙   النص**"""
    return f"**{MARK}   {text}**"


def box(title, lines):
    """عنوان مزخرف + سطر فاصل + قائمة نقاط."""
    body = "\n".join(f"{MARK} {l}" for l in lines)
    return f"**╮•• {title} ••╰**\n{LINE}\n\n{body}"


# ───────────── تخزين دائم (data.json) ─────────────
_DATA = os.path.join(os.getcwd(), "data.json")
_lock = threading.Lock()


def _read():
    try:
        with open(_DATA, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def dget(key, default=None):
    return _read().get(key, default)


def dset(key, value):
    with _lock:
        d = _read()
        d[key] = value
        try:
            with open(_DATA, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False)
        except Exception as e:
            print("data.json:", e)


# ───────────── دوال مشتركة ─────────────
def mention(user):
    name = (getattr(user, "first_name", None) or "المستخدم").replace("[", "").replace("]", "")
    return f"[{name}](tg://user?id={user.id})"


async def get_target(client, message, arg=None):
    """المستخدم المقصود: بالرد، أو بالمعرف/الايدي، أو None."""
    rep = message.reply_to_message
    if rep is not None and rep.from_user:
        return rep.from_user
    if arg:
        arg = arg.strip().split()[0]
        key = int(arg) if re.fullmatch(r"-?\d+", arg) else arg.lstrip("@")
        try:
            return await client.get_users(key)
        except Exception:
            return None
    return None


def parse_time(text):
    """5s / 10m / 2h / 1d -> ثواني (أو None)."""
    m = re.fullmatch(r"(\d+)\s*([smhd]?)", (text or "").strip().lower())
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2) or "m"
    return n * {"s": 1, "m": 60, "h": 3600, "d": 86400}[unit]
