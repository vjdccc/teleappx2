# -*- coding: utf-8 -*-
# مُحوَّل آلياً من اوامر Telethon Zahid (Telethon) الى Pyrogram عبر arabcompat
import warnings; warnings.filterwarnings("ignore")
from arabcompat import *
from arabcompat import _Missing, _format, _catutils, _cattools, _LazyTelegraph
try:
    import re
except Exception:
    re = _Missing('re')
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import calendar
except Exception:
    calendar = _Missing('calendar')
try:
    import json
except Exception:
    json = _Missing('json')
try:
    import os
except Exception:
    os = _Missing('os')
try:
    from asyncio.exceptions import TimeoutError
except Exception:
    TimeoutError = _Missing('TimeoutError')
try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = _Missing('BeautifulSoup')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    from urllib.parse import quote
except Exception:
    quote = _Missing('quote')
try:
    import barcode
except Exception:
    barcode = _Missing('barcode')
try:
    import qrcode
except Exception:
    qrcode = _Missing('qrcode')
try:
    import requests
except Exception:
    requests = _Missing('requests')
try:
    from barcode.writer import ImageWriter
except Exception:
    ImageWriter = _Missing('ImageWriter')
try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = _Missing('BeautifulSoup')
try:
    from PIL import Image, ImageColor
except Exception:
    Image = _Missing('Image')
    ImageColor = _Missing('ImageColor')
LOGS = logging.getLogger(__name__)
IQMOG = re.compile(
    "[" 
    "\U0001F1E0-\U0001F1FF"      "\U0001F300-\U0001F5FF"      "\U0001F600-\U0001F64F"   "\U0001F680-\U0001F6FF"  
    "\U0001F700-\U0001F77F"      "\U0001F780-\U0001F7FF"      "\U0001F800-\U0001F8FF"     "\U0001F900-\U0001F9FF"      "\U0001FA00-\U0001FA6F"  
    "\U0001FA70-\U0001FAFF"      "\U00002702-\U000027B0"      
    "]+")

def iqtfy(inputString: str) -> str:
    return re.sub(IQMOG, "", inputString)

@zahid.on(admin_cmd(pattern="حالتي ?(.*)"))
async def iq(zahid):
    await zahid.edit("جاري الفحص")
    async with bot.conversation("@SpamBot") as l5:
        try:
            dontTag = l5.wait_event(
                events.NewMessage(incoming=True, from_users=178220800))
            await l5.send_message("/start")
            dontTag = await dontTag
            await bot.send_read_acknowledge(l5.chat_id)
        except YouBlockedUserError:
            await zahid.edit("**قم بفك حظر @SpamBot للاكمال**")
            return
        await zahid.edit(f"~ {dontTag.message.message}")    
@zahid.on(admin_cmd(pattern="بوتي$"))
async def iq(iqbot):
    TG_BOT_USERNAME = Config.TG_BOT_USERNAME
    await iqbot.reply(f"**بوت تليثون الخاص بك : {TG_BOT_USERNAME}**")
@zahid.on(admin_cmd(pattern="ملصقي ?(.*)"))
async def iq(zahid):
    if zahid.fwd_from:
        return
    if not zahid.reply_to_msg_id:
        await edit_delete(zahid, "**الرجاء الرد على الرسالة**")
        return
    reply_message = await zahid.get_reply_message()
    warna = zahid.pattern_match.group(1)
    chat = "@QuotLyBot"
    await edit_or_reply(zahid, "**جاري...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1031952739))
            first = await conv.send_message(f"/start")
            ok = await conv.get_response()
            await asyncio.sleep(2)
            second = await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await zahid.reply("**قم بفك الحظر من البوت : @QuotLyBot **")
            return
        if response.text.startswith("Hi!"):
            await edit_or_reply(
                zahid, "**الرجاء تعطيل إعادة توجيه إعدادات الخصوصية الخاصة بك**")
        else:
            await zahid.delete()
            await bot.forward_messages(zahid.chat_id, response.message)
    await bot.delete_messages(conv.chat_id, [first.id, ok.id, second.id, response.id])
@zahid.on(admin_cmd(pattern="اسم الاغنيه ?(.*)"))
async def iq(zahid):
    if not zahid.reply_to_msg_id:
        return await zahid.edit("**الرجاء الرد على الرسالة**")
    reply_message = await zahid.get_reply_message()
    chat = "@auddbot"
    try:
        async with zahid.client.conversation(chat) as conv:
            try:
                await zahid.edit("**التعرف على الأغاني...**")
                start_msg = await conv.send_message("/start")
                await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await zahid.edit(
                        "**حدث خطأ أثناء تحديد الأغنية. حاول استخدام رسالة صوتية تتراوح مدتها من 5 إلى 10 ثوانٍ.**")
                await zahid.edit("**انتظر لحظة...**")
                result = await conv.get_response()
                await zahid.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await zahid.edit("**قم بفك الحظر من البوت : @auddbot dan coba lagi:")
                return
            namem = f"**إسم الأغنية : {result.text.splitlines()[0]}**\
        \n\n**تفاصيل : {result.text.splitlines()[2]}**"
            await zahid.edit(namem)
            await zahid.client.delete_messages(                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id]            )
    except TimeoutError:
        return await zahid.edit(            "**هناك خطا نعتذر**")
@zahid.on(admin_cmd(pattern="انشاء بريد(?: |$)(.*)"))
async def _(zahid):
    chat = "@TempMailBot"
    geez = await zahid.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(                incoming=True,                from_users=220112646            )            )            
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            zahidbot = ((response).reply_markup.rows[2].buttons[0].url)
            await zahid.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**قم بفتح الحظر عن : @TempMailBot للأستمرار بانشاء البريدات**")
            return
        await zahid.edit(f"بريدك الخاص هوه : ~ `{response.message.message}`\n[انقر هنا للتحقق من رسائل بريدك]({zahidbot})")
@zahid.on(admin_cmd(pattern="سجل الاسماء(ألف)?(?:\s|$)([\s\S]*)"))
async def _(zahid):  # sourcery no-metrics
    input_str = "".join(zahid.text.split(maxsplit=1)[1:])
    reply_message = await zahid.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(zahid, "**♛ ⦙ قم بالـرد على رسالـة لمستخـدم للحصـول على إسمـه/سجل يوزراتـه أو قم بإعطـاء آيـدي المستخـدم/يـوزر المستخـدم ✦**")
    user, rank = await get_user_from_event(zahid, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    iqevent = await edit_or_reply(zahid, "**♛ ⦙ جـاري المعالجـة ↯**")
    async with zahid.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(zahid, "**♛ ⦙ قم بإلغـاء حظـر @Sangmatainfo_bot ثم حـاول !!**")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await zahid.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(zahid, "**♛ ⦙ لا يستطيـع البـوت جلـب النتائـج ⚠️**")
    if "No records found" in responses:
        await edit_delete(zahid, "**♛ ⦙ المستخـدم ليـس لديـه أيّ سجـل ✕**")
    names, usernames = await sanga_seperator(responses)
    cmd = zahid.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == "u" else names
    for i in check:
        if sandy:
            await zahid.reply(i, parse_mode=_format.parse_pre)
        else:
            sandy = True
            await iqevent.edit(i, parse_mode=_format.parse_pre)
@zahid.on(admin_cmd(pattern="تيك توك(?: |$)(.*)"))
async def _(zahid):
    reply_message = await zahid.get_reply_message()
    if not reply_message:
        await edit_or_reply(zahid, "**♛ ⦙  الرد على الرابط.**")
        return
    if not reply_message.text:
        await edit_or_reply(zahid, "**♛ ⦙  الرد على الرابط.**")
        return
    chat = "@fs0bot"
    iqevent = await edit_or_reply(zahid, "**♛ ⦙  جاري تحميل الرابط**")
    async with zahid.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1354606430))
            await zahid.client.forward_messages(chat, reply_message)
            response = await response
            await zahid.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("**♛ ⦙  فك الحظر من البوت : @fs0bot**")
            return
        if response.text.startswith("؟"):
            await iqevent.edit("?")
        else:
            await iqevent.delete()
            await zahid.client.send_message(zahid.chat_id, response.message)
@zahid.on(admin_cmd(pattern="زخرفه_عربي ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@i0zbot"
    catevent = await edit_or_reply(event, "**جـارِ الزغـرفـه 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1229877081)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("** تحـقق من انـك لم تقـم بحظر البوت @i0zbot .. ثم اعـد استخدام الامـر ... ♥️**")
            return
        if response.text.startswith("رجاء قم بالرد على الكلمه التي تريد زخرفتها "):
            await catevent.edit("رجاء قم بالرد على الكلمه التي تريد زخرفتها")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
@zahid.on(admin_cmd(pattern="زخرفه_انكليزي ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@zagtelethonbot"
    catevent = await edit_or_reply(event, "**جـارِ الزغـرفـه 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1943073737)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("** تحـقق من انـك لم تقـم بحظر البوت @zagtelethonbot .. ثم اعـد استخدام الامـر ... ♥️**")
            return
        if response.text.startswith("رجاء قم بالرد على الكلمه التي تريد زخرفتها "):
            await catevent.edit("رجاء قم بالرد على الكلمه التي تريد زخرفتها")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
@zahid.on(admin_cmd(pattern="انستا (.*)"))
async def iq(zahidinsta):
    chat = "@instasavegrambot"
    link = zahidinsta.pattern_match.group(1)
    if "www.instagram.com" not in link:
        await edit_or_reply(zahidinsta, "يجب كتابة رابط")
    else:
        start = datetime.now()
        iqevent = await edit_or_reply(zahidinsta, "جار التحميل  🔍")
    async with zahidinsta.client.conversation(chat) as knov:
        try:
            msg_start = await knov.send_message("/start")
            response = await knov.get_response()
            msg = await knov.send_message(link)
            video = await knov.get_response()
            details = await knov.get_response()
            await zahidinsta.client.send_read_acknowledge(knov.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("بفتح الحظر  @instasavegrambot")
            return
        await iqevent.delete()
        l5 = await zahidinsta.client.send_file(zahidinsta.chat_id, video)
        end = datetime.now()
        (end - start).seconds
        await l5.edit(f"تم تنزيل", parse_mode="html")
    await zahidinsta.client.delete_messages(knov.chat_id, [msg_start.id, response.id, msg.id, video.id, details.id])
@zahid.on(admin_cmd(pattern="كشف الفايروسات( -i)?$"))    
async def _IQ(zahid):
    input_str = zahid.pattern_match.group(1)
    if not zahid.reply_to_msg_id:
        return await edit_or_reply(zahid, "الرد على أي رسالة مستخدم.")
    reply_message = await zahid.get_reply_message()
    if not reply_message.media:
        return await edit_or_reply(zahid, "الرد على الملف")
    chat = "@VS_Robot"
    IQevent = await edit_or_reply(zahid, " انتضر قليلا")
    async with zahid.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await zahid.client.forward_messages(chat, reply_message)
            response1 = await conv.get_response()
            if response1.text:
                await zahid.client.send_read_acknowledge(conv.chat_id)
                return await IQevent.edit(response1.text, parse_mode=_format.parse_pre)
            await conv.get_response()
            await zahid.client.send_read_acknowledge(conv.chat_id)
            response3 = await conv.get_response()
            response4 = await conv.get_response()
            await zahid.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await IQevent.edit("قم بفتح الحظر من : @VS_Robot")
        if not input_str:
            return await edit_or_reply(IQevent, response4.text)
        await IQevent.delete()
        await zahid.client.send_file(zahid.chat_id, response3.media, reply_to=(await reply_id(zahid)))
@zahid.on(admin_cmd(pattern="تقويم ([\s\S]*)"))    
async def _iq(zahid):
    input_str = zahid.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) != 2:
        return await edit_delete(zahid, "**تصحيح قم بكتابه الأمر هكذا : **`.تقويم السنه الشهر `", 5)

    yyyy = input_sgra[0]
    mm = input_sgra[1]
    try:
        output_result = calendar.month(int(yyyy.strip()), int(mm.strip()))
        await edit_or_reply(zahid, f"```{output_result}```")
    except Exception as e:
        await edit_delete(zahid, f"                                              **خطأ :**\n`{str(e)}`                       ", 5)

