# -*- coding: utf-8 -*-
# مُحوَّل آلياً من اوامر Telethon Zahid (Telethon) الى Pyrogram عبر arabcompat
import warnings; warnings.filterwarnings("ignore")
from arabcompat import *
from arabcompat import _Missing, _format, _catutils, _cattools, _LazyTelegraph
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import base64
except Exception:
    base64 = _Missing('base64')

plugin_category = "extra"
MUQT = gvarstatus("OR_MUQT") or "مؤقت"
UNMUQT = gvarstatus("OR_UNMUQT") or "ستوب"

async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
  
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            sandy = await event.client.send_file(event.chat_id, sandy, caption=sandy.text)
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه**")
                else:
                    await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه**")
            elif event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التكرار الوقتي 💢**\n" + f"**⌔︙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")
            else:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التكرار الوقتي 💢**\n" + f"**⌔︙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await _catutils.unsavegif(event, sandy)
        return
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**⎈ ⦙ التڪـرار  ♽**\n" + f"**⌔︙ تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n" + f"⌔︙ `{spam_message}`")
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "**⎈ ⦙ التڪـرار  ♽**\n"
                    + f"**⎈ ⦙ تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n"
                    + f"⎈ ⦙ `{spam_message}`",
                )
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⎈ ⦙ التكرار الوقتي 💢**\n"
                + f"**⎈ ⦙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {sleeptimet} seconds and with {counter} **رسائـل الـ  ✉️ :** \n"
                + f"⎈ ⦙ `{spam_message}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⎈ ⦙ التكرار الوقتي 💢**\n"
                + f"**⎈ ⦙ تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {sleeptimet} **الثوانـي و مـع** {counter} **رسائـل الـ  ✉️ :** \n"
                + f"⎈ ⦙ `{spam_message}`",
            )








@zahid.iq_cmd(pattern=f"{MUQT} ([\s\S]*)",)
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = float(input_str[0])
    except Exception:
        return await edit_delete(            event, "عذرا طريقه كتابة الأمر خطأ - شرح الارسال الوقتي او مؤقت للكروبات هنا : https:///4483"        )
    cat = input_str[1:]
    try:
        int(cat[0])
    except Exception:
        return await edit_delete(            event, "عذرا طريقه كتابة الأمر خطأ - شرح الارسال الوقتي او مؤقت للكروبات هنا : https:///4483"        )
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
   

