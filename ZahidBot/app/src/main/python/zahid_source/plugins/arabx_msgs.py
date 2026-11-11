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
    import base64
except Exception:
    base64 = _Missing('base64')
try:
    import string
except Exception:
    string = _Missing('string')
try:
    import os
except Exception:
    os = _Missing('os')
try:
    import subprocess
except Exception:
    subprocess = _Missing('subprocess')
try:
    import io
except Exception:
    io = _Missing('io')
try:
    import sys
except Exception:
    sys = _Missing('sys')
try:
    import traceback
except Exception:
    traceback = _Missing('traceback')
try:
    import random
except Exception:
    random = _Missing('random')
try:
    import textwrap
except Exception:
    textwrap = _Missing('textwrap')
try:
    import requests
except Exception:
    requests = _Missing('requests')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    from asyncio import sleep
except Exception:
    sleep = _Missing('sleep')
try:
    from geopy.geocoders import Nominatim
except Exception:
    Nominatim = _Missing('Nominatim')
try:
    from gtts import gTTS
except Exception:
    gTTS = _Missing('gTTS')
try:
    from random import choice, randint
except Exception:
    choice = _Missing('choice')
    randint = _Missing('randint')
from arabcompat import GT_LANGUAGES as LANGUAGES, GTranslator as Translator
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    Image = _Missing('Image')
    ImageDraw = _Missing('ImageDraw')
    ImageFont = _Missing('ImageFont')
LOGS = logging.getLogger(__name__)
CHAT_FLOOD = {}
ANTI_FLOOD_WARN_MODE = ChatBannedRights(
until_date=None, view_messages=None, send_messages=True)
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
ALLGROUB = gvarstatus("OR_ALLGROUB") or "للكروب"
ALLPRIVATE = gvarstatus("OR_ALLPRIVATE") or "للخاص"
FOTOSECRET = gvarstatus("OR_FOTOSECRET") or "جلب الوقتيه"


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
class FPOST:
    def __init__(self) -> None:
        self.GROUPSID = []
        self.MSG_CACHE = {}
FPOST_ = FPOST()
async def all_groups_id(cat):
    catgroups = []
    async for dialog in cat.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.megagroup:
            catgroups.append(entity.id)
    return catgroups
@zahid.on(admin_cmd(pattern="ازاله التوجيه(?: |$)(.*)"))    
async def _(event):
    try:
        await event.delete()
    except Exception as e:
        LOGS.info(str(e))
    m = await event.get_reply_message()
    if not m:
        return
    if m.media and not isinstance(m.media, MessageMediaWebPage):
        return await event.client.send_file(event.chat_id, m.media, caption=m.text)
    await event.client.send_message(event.chat_id, m.text)
@zahid.on(admin_cmd(pattern=f"{ALLGROUB} ?(.*)$"))    
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "هـذا الامـر مقـيد ")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "**🝳 ⦙   يجـب وضـع نـص مع الامـر للتوجيـه**")
    tt = event.text
    msg = tt[6:]
    event = await edit_or_reply(event, "** 🝳 ⦙   يتـم الـتوجيـة للـمجموعـات انتـظر قليلا**")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"🝳 ⦙   تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات")
async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
            break
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result
@zahid.on(admin_cmd(pattern=f"{ALLPRIVATE} ?(.*)$"))    
async def gucast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "هـذا الامـر مقـيد ")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "** 🝳 ⦙   يجـب وضـع نـص مع الامـر للتوجيـه**")
    tt = event.text
    msg = tt[7:]
    await edit_or_reply(event, "** 🝳 ⦙   يتـم الـتوجيـة للخـاص انتـظر قليلا**")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await event.edit(f"🝳 ⦙   تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات")
async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(event.chat_id, sandy, caption=sandy.text)
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
        if BOTLOG:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التڪـرار  ♽**\n" + f"**🝳 ⦙   تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه**")
                else:
                    await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التڪـرار  ♽**\n" + f"**🝳 ⦙   تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه**")
            elif event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التكرار الوقتي 💢**\n" + f"**🝳 ⦙   تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")
            else:
                await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التكرار الوقتي 💢**\n" + f"**🝳 ⦙   تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **مـع** {counter} **عدد المرات مع الرسالة أدناه مع التأخير** {sleeptimet} ** الثوانـي ⏱**")

            sandy = await event.client.send_file(BOTLOG_CHATID, sandy)
            await _catutils.unsavegif(event, sandy)
        return
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التڪـرار  ♽**\n" + f"**🝳 ⦙   تم تنفيذ التكرار بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n" + f"🝳 ⦙   `{spam_message}`")
            else:
                await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التڪـرار  ♽**\n" + f"**🝳 ⦙   تم تنفيذ التكرار بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {counter} **رسائـل الـ  ✉️ :** \n" + f"🝳 ⦙   `{spam_message}`")
    elif BOTLOG:
        if event.is_private:
            await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التكرار الوقتي 💢**\n" + f"**🝳 ⦙   تم تنفيذ التكرار الوقتي  بنجاح في ▷** [User](tg://user?id={event.chat_id}) **الدردشـة مـع** {sleeptimet} seconds and with {counter} **رسائـل الـ  ✉️ :** \n" + f"🝳 ⦙   `{spam_message}`")
        else:
            await event.client.send_message(BOTLOG_CHATID, "**🝳 ⦙   التكرار الوقتي 💢**\n" + f"**🝳 ⦙   تم تنفيذ التكرار الوقتي  بنجاح في ▷** {get_display_name(await event.get_chat())}(`{event.chat_id}`) **الدردشـة مـع** {sleeptimet} **الثوانـي و مـع** {counter} **رسائـل الـ  ✉️ :** \n" + f"🝳 ⦙   `{spam_message}`")
def zahidveFile(input_file_name):
    headers = {"X-API-Key": "paMkgkpsm4EYbDi4AKh4Nu9G",}
    files = {"image_file": (input_file_name, open(input_file_name, "rb")),}
    return requests.post("https://api.remove.bg/v1.0/removebg", headers=headers, files=files, allow_redirects=True, stream=True)
def zahidveURL(input_url):
    headers = {"X-API-Key": "paMkgkpsm4EYbDi4AKh4Nu9G",}
    data = {"image_url": input_url}
    return requests.post("https://api.remove.bg/v1.0/removebg",headers=headers,data=data,allow_redirects=True,stream=True)
Tnsmeetst = {}
Tnsmeet = {"ا": InputMessagesFilterVideo, "ل": InputMessagesFilterGif, "و": InputMessagesFilterUrl, "س": InputMessagesFilterPhotos, "ئ": InputMessagesFilterDocument, "ط": InputMessagesFilterVoice}
@zahid.on(admin_cmd(pattern="موقع(?: |$)(.*)"))    
async def gps(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "** 🝳 ⦙   جاري العثـور على الموقع  … **")
    geolocator = Nominatim(user_agent="catzahid")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**🝳 ⦙   الموقـع 𖠕  : **`{input_str}`", reply_to=reply_to_id)
        await catevent.delete()
    else:
        await catevent.edit("🝳 ⦙   عـذراً، لـم أستطـع إيجـاده  ⚠️")
async def ocr_zahid(filename, overlay=False,api_key="K88942796188957", language="eng"):
    payload = {"isOverlayRequired": overlay,"apikey": api_key,"language": language}
    with open(filename, "rb") as f:
        r = requests.post("https://api.ocr.space/parse/image",files={filename: f},data=payload)
    return r.json()
@zahid.on(admin_cmd(pattern="تنظيف(?:\s|$)([\s\S]*)"))
async def iq(cloneiq):  
    chat = await cloneiq.get_input_chat()
    msgs = []
    count = 0
    input_str = cloneiq.pattern_match.group(1)
    iqype = re.findall(r"\w+", input_str)
    try:
        p_type = iqype[0].replace("-", "")
        input_str = input_str.replace(iqype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await cloneiq.delete()
    reply = await cloneiq.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in Tnsmeet:
                        async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), offset_id=reply.id - 1, reverse=True, filter=Tnsmeet[ty]):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await cloneiq.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await cloneiq.client.delete_messages(chat, msgs)
                    elif ty == "s":
                        error += f"\n**🝳 ⦙   هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
                    else:
                        error += f"\n\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
            else:
                count += 1
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=(int(input_str) - 1), offset_id=reply.id, reverse=True):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
        elif input_str and p_type is not None:
            if p_type == "s":
                try:
                    cont, inputstr = input_str.split(" ")
                except ValueError:
                    cont = "error"
                    inputstr = input_str
                cont = cont.strip()
                inputstr = inputstr.strip()
                if cont.isnumeric():
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), offset_id=reply.id - 1, reverse=True, search=inputstr):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                else:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, offset_id=reply.id - 1, reverse=True, search=input_str):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            else:
                error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :** "
        elif input_str:
            error += f"\n🝳 ⦙   **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type is not None:
            for ty in p_type:
                if ty in Tnsmeet:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, min_id=cloneiq.reply_to_msg_id - 1, filter=Tnsmeet[ty]):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                else:
                    error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        else:
            async for msg in cloneiq.client.iter_messages(chat, min_id=cloneiq.reply_to_msg_id - 1 ):
                count += 1
                msgs.append(msg)
                if len(msgs) == 50:
                    await cloneiq.client.delete_messages(chat, msgs)
                    msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
    elif p_type is not None and input_str:
        if p_type != "s" and input_str.isnumeric():
            for ty in p_type:
                if ty in Tnsmeet:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), filter=Tnsmeet[ty]):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                elif ty == "s":
                    error += f"\n**🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
                else:
                    error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type == "s":
            try:
                cont, inputstr = input_str.split(" ")
            except ValueError:
                cont = "error"
                inputstr = input_str
            cont = cont.strip()
            inputstr = inputstr.strip()
            if cont.isnumeric():
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), search=inputstr):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            else:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, search=input_str):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
        else:
            error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif p_type is not None:
        for ty in p_type:
            if ty in Tnsmeet:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, filter=Tnsmeet[ty]
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            elif ty == "s":
                error += f"\n**🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
            else:
                error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif input_str.isnumeric():
        async for msg in cloneiq.client.iter_messages(chat, limit=int(input_str) + 1):
            count += 1
            msgs.append(msg)
            if len(msgs) == 50:
                await cloneiq.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await cloneiq.client.delete_messages(chat, msgs)
    else:
        error += "\n**🝳 ⦙   لم يتـم تحـديد الرسـالة أرسل  (.الاوامر ) و رؤية اوامر التنظيف  📌**"
    if msgs:
        await cloneiq.client.delete_messages(chat, msgs)
    if count > 0:
        result += "🝳 ⦙   تـم الأنتـهاء من التـنظيف السـريع  ✅  \n 🝳 ⦙   لقـد  تـم حـذف \n  🝳 ⦙   عـدد  " + str(count) + " من الـرسائـل 🗑️"
    if error != "":
        result += f"\n\n**🝳 ⦙  عـذرا هنـاك خطـأ ❌:**{error}"
    if result == "":
        result += "**🝳 ⦙   لا تـوجد رسـائل لـتنظيفها ♻️**"
    hi = await cloneiq.client.send_message(cloneiq.chat_id, result)
    if BOTLOG:
        await cloneiq.client.send_message(BOTLOG_CHATID, f"**🝳 ⦙   حـذف الـرسائل 🗳️** \n{result}")
    await sleep(5)
    await hi.delete()
Tnsmeet1 = {}
Tnsmeet1 = {"ا": InputMessagesFilterPhotos, "ل": InputMessagesFilterDocument, "ر": InputMessagesFilterUrl, "س": InputMessagesFilterEmpty, "ئ": InputMessagesFilterGif,"ج": InputMessagesFilterVideo,  "م": InputMessagesFilterMusic, "ي": InputMessagesFilterMyMentions, "ع": InputMessagesFilterGeo}
@zahid.on(admin_cmd(pattern="ترجمه ([\s\S]*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(event, "**🝳 ⦙   للترجمه يجـب الـرد على الرساله واكتب .ترجمه ar**", time=5)
    text = deEmojify(text.strip())
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**🝳 ⦙   تمت الترجمه مـن  :** {LANGUAGES[translated.src].title()}\n **🝳 ⦙   الـى ** {LANGUAGES[lan].title()} \n\n{after_tr_text}"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"**خـطأ:**\n`{str(exc)}`", time=5)
@zahid.on(admin_cmd(pattern=f"{FOTOSECRET}(?: |$)(.*)"))    
async def iq(event):
  if not event.is_reply:
    return await event.edit('**يجـب عـليك الـرد عـلى صـورة ذاتيـة الـتدمير**')
  ogtah = await event.get_reply_message()
  pic = await ogtah.download_media()
  await bot.send_file('me', pic, caption=f"""**الصـورة الوقتيه ✅**\- So : Telethon Zahid""")
  await event.delete()
@zahid.on(admin_cmd(pattern="تاريخ الرساله(?: |$)(.*)"))    
async def _(event):
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(event, f"**هذا تاريخ الرساله والوقت  👁‍🗨 :** `{yaml_format(result)}`")
@zahid.on(admin_cmd(pattern="حذف(?:\s|$)([\s\S]*)"))
async def iq(cloneiq):  
    chat = await cloneiq.get_input_chat()
    msgs = []
    count = 0
    input_str = cloneiq.pattern_match.group(1)
    iqype = re.findall(r"\w+", input_str)
    try:
        p_type = iqype[0].replace("-", "")
        input_str = input_str.replace(iqype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await cloneiq.delete()
    reply = await cloneiq.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in Tnsmeet1:
                        async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), offset_id=reply.id - 1, reverse=True, filter=Tnsmeet1[ty]):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await cloneiq.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await cloneiq.client.delete_messages(chat, msgs)
                    elif ty == "s":
                        error += f"\n**🝳 ⦙   هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
                    else:
                        error += f"\n\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
            else:
                count += 1
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=(int(input_str) - 1), offset_id=reply.id, reverse=True):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
        elif input_str and p_type is not None:
            if p_type == "s":
                try:
                    cont, inputstr = input_str.split(" ")
                except ValueError:
                    cont = "error"
                    inputstr = input_str
                cont = cont.strip()
                inputstr = inputstr.strip()
                if cont.isnumeric():
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), offset_id=reply.id - 1, reverse=True, search=inputstr):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                else:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, offset_id=reply.id - 1, reverse=True, search=input_str):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            else:
                error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :** "
        elif input_str:
            error += f"\n🝳 ⦙   **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type is not None:
            for ty in p_type:
                if ty in Tnsmeet1:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, min_id=cloneiq.reply_to_msg_id - 1, filter=Tnsmeet1[ty]):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                else:
                    error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        else:
            async for msg in cloneiq.client.iter_messages(chat, min_id=cloneiq.reply_to_msg_id - 1 ):
                count += 1
                msgs.append(msg)
                if len(msgs) == 50:
                    await cloneiq.client.delete_messages(chat, msgs)
                    msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
    elif p_type is not None and input_str:
        if p_type != "s" and input_str.isnumeric():
            for ty in p_type:
                if ty in Tnsmeet1:
                    async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(input_str), filter=Tnsmeet1[ty]):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                elif ty == "s":
                    error += f"\n**🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
                else:
                    error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type == "s":
            try:
                cont, inputstr = input_str.split(" ")
            except ValueError:
                cont = "error"
                inputstr = input_str
            cont = cont.strip()
            inputstr = inputstr.strip()
            if cont.isnumeric():
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, limit=int(cont), search=inputstr):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            else:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, search=input_str):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
        else:
            error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif p_type is not None:
        for ty in p_type:
            if ty in Tnsmeet1:
                async for msg in cloneiq.client.iter_messages(cloneiq.chat_id, filter=Tnsmeet1[ty]
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            elif ty == "s":
                error += f"\n**🝳 ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
            else:
                error += f"\n🝳 ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif input_str.isnumeric():
        async for msg in cloneiq.client.iter_messages(chat, limit=int(input_str) + 1):
            count += 1
            msgs.append(msg)
            if len(msgs) == 50:
                await cloneiq.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await cloneiq.client.delete_messages(chat, msgs)
    else:
        error += "\n**🝳 ⦙   لم يتـم تحـديد الرسـالة أرسل  (.الاوامر ) و رؤية اوامر التنظيف  📌**"
    if msgs:
        await cloneiq.client.delete_messages(chat, msgs)
    if count > 0:
        result += "🝳 ⦙   تـم الأنتـهاء من التـنظيف السـريع  ✅  \n 🝳 ⦙   لقـد  تـم حـذف \n  🝳 ⦙   عـدد  " + str(count) + " من الـرسائـل 🗑️"
    if error != "":
        result += f"\n\n**🝳 ⦙  عـذرا هنـاك خطـأ ❌:**{error}"
    if result == "":
        result += "**🝳 ⦙   لا تـوجد رسـائل لـتنظيفها ♻️**"
    hi = await cloneiq.client.send_message(cloneiq.chat_id, result)
    if BOTLOG:
        await cloneiq.client.send_message(BOTLOG_CHATID, f"**🝳 ⦙   حـذف الـرسائل 🗳️** \n{result}")
    await sleep(5)
    await hi.delete()
@zahid.on(admin_cmd(pattern="معرفات 100(?: |$)(.*)"))
async def iq(zahid):
    mentions = zahid.text[8:]
    chat = await zahid.get_input_chat()
    async for x in zahid.client.iter_participants(chat, 100):
        mentions += f" - @{x.username} ⦙ "
    await zahid.client.send_message(zahid.chat_id, mentions)
    await zahid.delete()
@zahid.on(admin_cmd(pattern="معرفات 200(?: |$)(.*)"))
async def iq(zahid):
    mentions = zahid.text[8:]
    chat = await zahid.get_input_chat()
    async for x in zahid.client.iter_participants(chat, 200):
        mentions += f" - @{x.username} ⦙ "
    await zahid.client.send_message(zahid.chat_id, mentions)
    await zahid.delete()

async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)
@zahid.iq_cmd(pattern="(ازاله الخلفيه بالملصق|ازاله الخلفيه)(?:\s|$)([\s\S]*)",)
async def remove_iq(event):
    cmd = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    message_id = await reply_id(event)
    if event.reply_to_msg_id and not input_str:
        reply_message = await event.get_reply_message()
        catevent = await edit_or_reply(event, "`تحليل هذه الصورة / الملصق...`")
        file_name = os.path.join(Config.TEMP_DIR, "rmbg.png")
        try:
            await event.client.download_media(reply_message, file_name)
        except Exception as e:
            await edit_delete(catevent, f"`{str(e)}`", 5)
            return
        else:
            await catevent.edit("إزالة خلفية هذه الوسائط")
            file_name = convert_toimage(file_name)
            response = zahidveFile(file_name)
            os.remove(file_name)
    elif input_str:
        catevent = await edit_or_reply(event, "إزالة خلفية هذه الوسائط")
        response = zahidveURL(input_str)
    else:
        await edit_delete(event, "قم بالرد على أي صورة أو ملصق باستخدام rmbg / srmbg للحصول على خلفية أقل من ملف png أو تنسيق webp أو توفير رابط الصورة مع الأمر", 5)
        return
    contentType = response.headers.get("content-type")
    remove_bg_image = "zahid.png"
    if "image" in contentType:
        with open("zahid.png", "wb") as removed_bg_file:
            removed_bg_file.write(response.content)
    else:
        await edit_delete(catevent, f"`{response.content.decode('UTF-8')}`", 5)
        return
    if cmd == "ازاله الخلفيه بالملصق":
        file = convert_tosticker(remove_bg_image, filename="zahid.webp")
        await event.client.send_file(event.chat_id,file,reply_to=message_id)
    else:
        file = remove_bg_image
        await event.client.send_file(event.chat_id,file,force_document=True,reply_to=message_id)
    await catevent.delete()
@zahid.on(admin_cmd(pattern="ابلاغ الادمنيه(?: |$)(.*)"))    
async def iq(event):
    mentions = "@تاك للادمنيه : **🝳 ⦙  تم رصـد إزعـاج ⚠️**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()
@zahid.on(admin_cmd(pattern="خط ملصق ?(?:(.*?) ?; )?([\s\S]*)"))    
async def sticklet(event):
    "your text as sticker"
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_to_id = await reply_id(event)
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    reply_message = await event.get_reply_message()
    if not sticktext:
        if event.reply_to_msg_id:
            sticktext = reply_message.message
        else:
            return await edit_or_reply(event, "need something, hmm")
    await event.delete()
    sticktext = deEmojify(sticktext)
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@catfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)    )
    image_stream = io.BytesIO()
    image_stream.name = "zahid.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    await event.client.send_file(        event.chat_id,        image_stream,        caption="zahid's Sticklet",        reply_to=reply_to_id,    )
    try:
        os.remove(FONT_FILE)
    except BaseException:
        pass
@zahid.on(admin_cmd(pattern="ضفدع(?:\s|$)([\s\S]*)"))    
async def honk(event):
    "Make honk say anything."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(                event, "__What is honk supposed to say? Give some text.__"            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)
@zahid.on(admin_cmd(pattern="تاك بالكلام ([\s\S]*)"))    
async def iq(event):
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(event.chat_id, f"<a href='tg://user?id={user.id}'>{input_str}</a>", parse_mode="HTML", reply_to=reply_to_id)
async def get_font_file(client, channel_id, search_kw=""):
    font_file_message_s = await client.get_messages(        entity=channel_id,        filter=InputMessagesFilterDocument,                limit=None,        search=search_kw,    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)
@zahid.on(admin_cmd(pattern="لافته(?:\s|$)([\s\S]*)"))    
async def waifu(animu):
    text = animu.pattern_match.group(1)
    reply_to_id = await reply_id(animu)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            return await edit_or_reply(                animu, "`You haven't written any article, Waifu is going away.`"            )
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, animu.client)

