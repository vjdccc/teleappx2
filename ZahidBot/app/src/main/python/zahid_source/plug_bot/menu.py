# -*- coding: utf-8 -*-
# Telethon Zahid - قائمة الأوامر (انلاين) بأزرار ملونة.
# تيليجرام يسمح بثلاثة الوان فقط: primary (ازرق) / success (اخضر) / danger (احمر).
# مكتبة Pyrogram العادية لا تدعم لون الزر، لذلك الرد يُرسل عبر Bot API مباشرة.
# (الالوان تظهر في تطبيقات تيليجرام المحدثة؛ في القديمة تظهر الازرار بلا لون.)
import asyncio
import importlib
import json
import shutil
import urllib.request
import html as _h
import re as _re

from pyrogram import Client, filters, enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *

API = f"https://api.telegram.org/bot{token}/"


def _call(method, payload):
    req = urllib.request.Request(
        API + method,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


async def api(method, payload):
    """يستدعي Bot API دون حجب البوت. يرجع True عند النجاح."""
    try:
        res = await asyncio.to_thread(_call, method, payload)
        return bool(res.get("ok"))
    except Exception as e:
        print(f"Bot API {method}: {e}")
        return False


from arabstyle import MARK, LINE

TITLE = f"╮•• قائمه الاوامر ••╰\n{LINE}\n\n{MARK} اختر القسم الذي تريده من الازرار"

# (لون الزر, الاسم, الاوامر)
_RAW = {
    "help1": ("success", 'الحساب', """
• احصائيات حسابي ، اطار ، قلب الصوره ، فلتر رصاصي ، زوم
• قائمه ، حفض كتابه ، حفض توجيه ، وضع بايو ، وضع اسم
• وضع صوره ، شوت ، معرفاتي ، رابطه
• اسمه ، صورته ، الملفات ، كتابه ، عد الردود
• زاجل ، سمول ، عكس الالوان ، فلتر احمر ، يمين الصوره"""),

    "help2": ("success", 'الخدمات', """
• جلب لقطات ، رابط تطبيق ، العمر ، الوقت ، وقتي
• الاذان ، فيديو ، البحث العام
• تخزين الصوت ، اضف الصوت ، تحويل صوره ، تحويل ملصق ، تحويل
• تحويل متحركة ، تحويل فديو دائري ، تحويل ملصق دائري ، تحويل ملف ، بورن
• تحويل رساله ، تحويل ملف صوره ، تحويل متحركه ، مدينه الطقس ، تحويل فديو متحركه
• طقوس"""),

    "help3": ("success", 'البوتات', """
• حالتي ، بوتي ، ملصقي ، اسم الاغنيه ، انشاء بريد
• سجل الاسماء ، تيك توك ، زخرفه_عربي ، زخرفه_انكليزي ، انستا
• كشف الفايروسات ، تقويم"""),

    "help5": ("success", 'التسليه', """
• غبي ، تفجير ، قتل ، رابط الحذف ، طوبه
• مربعات ، حلويات ، نار ، هلكوبتر ، اشكال مربع
• دائره ، يوغا ، مزاج ، قرد ، ايد
• العد التنازلي ، الوان قلوب ، عين ، غنيلي ، قران
• ثعبان ، شعر ، رجل ، رموز شيطانيه ، قطار
• موسيقى ، رسم ، فراشه ، مكعبات ، مربعاتي
• مطر ، تحركات ، ايموجيات ، اسعاف ، طائره
• شرطي ، النضام الشمسي ، افكر ، ضحك ، ضايج
• اوصفلي ، مهنته ، زوجه ، زوجها ، ركصله
• طبخله ، ساعه متحركه ، بوسه ، رياضه ، فواكه
• الارض ، قمور ، زرفه ، بيبي ، /start
• تفاعلات ، اخذ قلبي ، اشوفج السطح ، احبك ، اركض
• روميو ، بوسات ، رسم قلوب ، رسم شعار ، البنك
• تهكير ، اذكار ، اذكار عشر ، كلام متحرك ، حمامه
• طياره ، مصاصه ، نص ثري دي ، نسبه الحب ، نسبه الانوثه
• نسبه الغباء ، نسبه الانحراف ، نسبه المثليه ، نسبه النجاح ، نسبه الكراهيه
• صفق ، حضر وهمي ، رفع كحبه ، رفع مطي ، رفع زباله
• رفع منشئ ، رفع مدير ، رفع مطور ، رفع كواد ، رفع مرتبط
• رفع مثلي ، رفع زوجتي ، رفع صاك ، رفع صاكه ، كت
• هينه ، سمايلي ، الحياه ، مصه ، اركضلي
• جكه ، فايروس ، هلو ، رئيك ، رفع شيخ
• رفع فرخ ، رفع تاج ، رفع مكبسل ، رفع غبي ، رفع سعلوه"""),

    "help6": ("success", 'المجموعات', """
• تشفير الملف ، المشرفين ، البوتات ، الأعضاء ، المحذوفين
• احصائيات الاعضاء ، معلومات تخزين المجموعه ، تخزين الخاص ، تخزين الكروبات ، الغاء التثبيت
• all ، ايقاف التاك ، zip ، unzip ، معرفه
• جلب الصور"""),

    "help7": ("success", 'الرسائل', """
• ازاله التوجيه ، موقع ، تنظيف ، ترجمه ، تاريخ الرساله
• حذف ، معرفات 100 ، معرفات 200 ، ابلاغ الادمنيه ، خط ملصق
• ضفدع ، تاك بالكلام ، لافته"""),

    "help8": ("success", 'السورس', """
• رابط التنصيب ، حساب كيثاب ، حذف جميع الملفات ، فارات تنصيبي ، مساعده
• اطفاء مؤقت ، تاريخ التنصيب ، استخدامي ، سرعه الانترنيت ، م9
• م10 ، م11 ، م12 ، م13 ، م14
• م15 ، م16 ، م1 ، م2 ، م3
• م4 ، م5 ، م6 ، م7 ، م8
• هاش ، م21 ، م22 ، م23 ، فتح همسه"""),

    "help9": ("success", 'الملصقات', """
• صنع ملصق ، انشاء حزمه ملصقات ، ملصق"""),

    "help10": ("success", 'الزخرفه والقوالب', """
• رموز1 ، رموز2 ، تمبلريه ، البايو ، الاختصارات
• اشهر مزغرفه ، المواليد ، اختصارات1 ، اختصارات2 ، اختصارات3
• اختصارات4 ، اختصارات5 ، بايو1 ، بايو2 ، بايو3
• بايو4 ، بايو5 ، بايوهات1 ، بايوهات2"""),

    "help11": ("success", 'الصوتيات', """
• ص1 الى ص94"""),

    "help12": ("success", 'النظام', """
• الاوامر ، بنك ، مدة التشغيل
• اعاده تشغيل ، ايقاف"""),
}


def _cmd_html(seg):
    """يحوّل مقطع امر واحد الى <code>.الامر</code> + شرحه كنص عادي (الضغط على الامر ينسخه)."""
    seg = seg.strip()
    m = _re.match(r"^(.*?)(\s+\+.*|\s*\(.*|\s*:.*)?$", seg)
    cmd, rest = (m.group(1).strip(), m.group(2) or "") if m else (seg, "")
    if not cmd:
        return _h.escape(seg)
    return f"<code>.{_h.escape(cmd)}</code>" + _h.escape(rest)


# أوامر تحتاج مكتبات اختيارية: اذا لم تُثبَّت المكتبة (او لا تعمل) يُحذف الامر من القائمة تلقائياً.
_DEPS = {
    "تحويل رساله": ["fitz"],
    "اضف الصوت": ["moviepy.editor"],
    "تحويل فديو دائري": ["pymediainfo", "bin:ffmpeg"],
    "تحويل ملصق دائري": ["pymediainfo", "bin:ffmpeg"],
    "جلب لقطات": ["bin:ffmpeg"],
    "تحويل متحركة": ["bin:ffmpeg"],
    "تحويل متحركه": ["bin:ffmpeg"],
    "تحويل فديو متحركه": ["bin:ffmpeg"],
    "تشفير الملف": ["pyminizip"],
    "معلومات تخزين المجموعه": ["prettytable"],
    "نص ثري دي": ["pyfiglet"],
    "موقع": ["geopy"],
    "حساب كيثاب": ["github"],
    "سرعه الانترنيت": ["speedtest"],
    "ملصق": ["cloudscraper"],
    "نبذه وقتيه": ["cv2"],
    "صوره وقتية": ["pySmartDL"],
}
_ok_cache = {}


def _can_import(mod):
    if mod not in _ok_cache:
        try:
            if mod.startswith("bin:"):  # برنامج خارجي (مثل ffmpeg) غير موجود في اندرويد
                _ok_cache[mod] = shutil.which(mod[4:]) is not None
            else:
                importlib.import_module(mod)
                _ok_cache[mod] = True
        except Exception:
            _ok_cache[mod] = False
    return _ok_cache[mod]


def _cmd_name(seg):
    m = _re.match(r"^(.*?)(\s+\+.*|\s*\(.*|\s*:.*)?$", seg.strip())
    return (m.group(1) if m else seg).strip()


def _available(seg):
    return all(_can_import(mod) for mod in _DEPS.get(_cmd_name(seg), []))


def _body(raw):
    out = []
    for l in raw.strip().split("\n"):
        if not l.startswith("• "):
            out.append(_h.escape(l))
            continue
        parts = _re.split(r"\s*(?:،|--)\s*", l[2:])
        parts = [x for x in parts if x.strip() and _available(x)]
        if parts:
            out.append(f"{MARK} " + " ، ".join(_cmd_html(x) for x in parts))
    return "\n".join(out)


# (ايقونه, لون الزر, الاسم, النص)
SECTIONS = {
    k: ("", style, name, f"╮•• {name} ••╰\n{LINE}\n\n{_body(raw)}")
    for k, (style, name, raw) in _RAW.items()
}


def _rows(cls_button, with_style):
    """يبني صفوف الازرار (زرين في كل صف)."""
    rows, row = [], []
    for key, (icon, style, name, _) in SECTIONS.items():
        text = name
        if with_style:
            row.append({"text": text, "callback_data": key, "style": style})
        else:
            row.append(cls_button(text, callback_data=key))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    return rows


def main_markup():
    """نسخة Pyrogram (بدون لون) تُستخدم احتياطاً."""
    return InlineKeyboardMarkup(_rows(InlineKeyboardButton, False))


def main_keyboard():
    """نسخة Bot API (بالالوان)."""
    return {"inline_keyboard": _rows(None, True)}


BACK = InlineKeyboardMarkup([[InlineKeyboardButton("عوده", callback_data="help")]])
BACK_KB = {"inline_keyboard": [[{"text": "عوده", "callback_data": "help", "style": "danger"}]]}


@bot.on_inline_query(filters.regex("^الاوامر$"))
async def answer(client, inline_query):
    ok = await api("answerInlineQuery", {
        "inline_query_id": inline_query.id,
        "cache_time": 1,
        "results": [{
            "type": "article",
            "id": "commands",
            "title": "اوامر البوت",
            "description": "اضغط لعرض الاوامر",
            "input_message_content": {"message_text": _h.escape(TITLE), "parse_mode": "HTML"},
            "reply_markup": main_keyboard(),
        }],
    })
    if not ok:  # احتياط: ازرار بدون لون
        await inline_query.answer(
            results=[InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(TITLE),
                description="اضغط لعرض الاوامر",
                reply_markup=main_markup(),
            )],
            cache_time=1,
        )


async def _show(callback_query, text, keyboard, fallback_markup):
    payload = {"text": text, "reply_markup": keyboard, "parse_mode": "HTML"}
    if callback_query.inline_message_id:
        payload["inline_message_id"] = callback_query.inline_message_id
    elif callback_query.message:
        payload["chat_id"] = callback_query.message.chat.id
        payload["message_id"] = callback_query.message.id
    ok = await api("editMessageText", payload)
    await api("answerCallbackQuery", {"callback_query_id": callback_query.id})
    if not ok:  # احتياط: ازرار بدون لون
        await callback_query.edit_message_text(text, reply_markup=fallback_markup, parse_mode=enums.ParseMode.HTML)


@bot.on_callback_query(filters.regex(r"^help\d+$"))
async def section(client, callback_query):
    text = SECTIONS[callback_query.data][3]
    await _show(callback_query, text, BACK_KB, BACK)


@bot.on_callback_query(filters.regex("^help$"))
async def back(client, callback_query):
    await _show(callback_query, _h.escape(TITLE), main_keyboard(), main_markup())
