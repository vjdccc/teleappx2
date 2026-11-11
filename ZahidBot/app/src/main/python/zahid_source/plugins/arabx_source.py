# -*- coding: utf-8 -*-
# مُحوَّل آلياً من اوامر Telethon Zahid (Telethon) الى Pyrogram عبر arabcompat
import warnings; warnings.filterwarnings("ignore")
from arabcompat import *
from arabcompat import _Missing, _format, _catutils, _cattools, _LazyTelegraph
try:
    import os
except Exception:
    os = _Missing('os')
try:
    import aiohttp
except Exception:
    aiohttp = _Missing('aiohttp')
try:
    import requests
except Exception:
    requests = _Missing('requests')
try:
    import random
except Exception:
    random = _Missing('random')
try:
    import re
except Exception:
    re = _Missing('re')
try:
    import time
except Exception:
    time = _Missing('time')
try:
    import sys
except Exception:
    sys = _Missing('sys')
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import math
except Exception:
    math = _Missing('math')
try:
    import urllib3
except Exception:
    urllib3 = _Missing('urllib3')
try:
    import speedtest
except Exception:
    speedtest = _Missing('speedtest')
try:
    import base64
except Exception:
    base64 = _Missing('base64')
try:
    import psutil
except Exception:
    psutil = _Missing('psutil')
try:
    import platform
except Exception:
    platform = _Missing('platform')
try:
    import json
except Exception:
    json = _Missing('json')
try:
    from subprocess import PIPE
except Exception:
    PIPE = _Missing('PIPE')
try:
    from subprocess import run as runapp
except Exception:
    runapp = _Missing('runapp')
try:
    from asyncio.exceptions import CancelledError
except Exception:
    CancelledError = _Missing('CancelledError')
try:
    from time import sleep
except Exception:
    sleep = _Missing('sleep')
try:
    from platform import python_version
except Exception:
    python_version = _Missing('python_version')
try:
    from github import Github
except Exception:
    Github = _Missing('Github')
try:
    from pySmartDL import SmartDL
except Exception:
    SmartDL = _Missing('SmartDL')
try:
    from pathlib import Path
except Exception:
    Path = _Missing('Path')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    from urlextract import URLExtract
except Exception:
    URLExtract = _Missing('URLExtract')
ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"
UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"
ORDERS = gvarstatus("OR_ORDERS") or "(اوامري|أوامري|م)"
ZAHIDPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/74066cb3ddb0bdba1c4b7.mp4"
LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Heroku = None
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [    "ALIVE_PIC",    "ALIVE_EMOJI",    "ALIVE_TELETHONIQ",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP","OR_UNMUQT"]
DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}
IQPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/74066cb3ddb0bdba1c4b7.mp4"
def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

fahs = """‎⿻┊My 𖠄 {my_mention} ٫
‌‎⿻┊BoT 𖠄 {tg_bot} ٫
‌‎⿻┊TimE 𖠄 {TM} ٫
‌‎⿻┊UpTimE 𖠄 {uptime} ٫
‌‎⿻┊‌‎PinG 𖠄 {ping} ٫
‌‎⿻┊‌‎VeRsIoN 𖠄 (7.7) ,
‌‎⿻┊‌‎Telethon Zahid"""

@zahid.on(admin_cmd(pattern="رابط التنصيب(?: |$)(.*)"))    
async def source(e):
    await edit_or_reply(e, "https://github.com/TelethonArab/TelethonAr",)
@zahid.on(admin_cmd(pattern="حساب كيثاب( -l(\d+))? ([\s\S]*)"))    
async def _(event):
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, "`" + username + " not found`")
            catevent = await edit_or_reply(event, "**🝳︙  جـاري إحضـار معلومـات حساب كيثاب ↯**")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**🝳︙  معلومـات الكيثاب لـ :** `{username}`\
                \n**🝳︙  الإسـم 👤:** [{name}]({html_url})\
                \n**🝳︙  النـوع 🔧:** `{type}`\
                \n**🝳︙  الشرڪـة 🏢:** `{company}`\
                \n**🝳︙  المدونـة 🔭:**  {blog}\
                \n**🝳︙  الموقـع 📍:**  `{location}`\
                \n**🝳︙  النبـذة 📝:**  `{bio}`\
                \n**🝳︙  عـدد المتابعيـن ❤️:**  `{followers}`\
                \n**🝳︙  الذيـن يتابعهـم 👁:**  `{following}`\
                \n**🝳︙   عدد ريبو العام 📊:**  `{public_repos}`\
                \n**🝳︙  الجمهـور 📄:**  `{public_gists}`\
                \n**🝳︙  تم إنشـاء الملـف الشخصـي ✓** 🔗: `{created_at}`\
                \n**🝳︙  تم تحديـث الملـف الشخصـي ✓** ✏️: `{updated_at}`".format(
                username=username, **result            )
            if repos:
                REPLY += "\n**🝳︙  بعـض الريبوات 🔍 :** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(event.chat_id, ppath, caption=REPLY, reply_to=reply_to)
            os.remove(ppath)
            await catevent.delete()
@zahid.on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**🝳︙  تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
@zahid.on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    
async def _(event):
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (f"🝳︙  وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب سورس تليثون Telethon Zahid :**\n\n{o}")
    await edit_or_reply(event, OUTPUT)

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await zahid.get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"zahid/plugins/{plugin_name}"):
                return
            downloaded_file_name = await zahid.download_media(                await zahid.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "zahid/plugins/",            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await zahid.send_message(                    BOTLOG_CHATID,                    f"**🝳︙   تحـميل المـلف 🗂️  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )

    zahid.loop.create_task(install())
@zahid.on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def _(event):
    sandy = await edit_or_reply(event ,                                 "%10 ▰▱▱▱▱▱▱▱▱▱ " ,)
    await asyncio.sleep(1)
    await edit_or_reply(event , "%20 ▰▰▱▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%30 ▰▰▰▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%40 ▰▰▰▰▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%50 ▰▰▰▰▰▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%60 ▰▰▰▰▰▰▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%70 ▰▰▰▰▰▰▰▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%80 ▰▰▰▰▰▰▰▰▱▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%90 ▰▰▰▰▰▰▰▰▰▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%100 ▰▰▰▰▰▰▰▰▰▰ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , """🝳︙ جـاري تـحديث تليثـون العـرب (7.7)
⌚ انتضر من 5 الى 10 دقائق""")
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS1.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS1.error(e)
    try:
        delgvar("ipaddress")
        await zahid.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS1.error(e)
@zahid.on(admin_cmd(pattern="مساعده(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"""• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
  • لتغير نبذه الوقتيه اضغط هنا ↶
  • لتغير صوره وقتيه اضغط هنا ↶
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
• لتغير امر من الاوامر اضغط هنا ↶
• لكيفيه حذف الفار اضغط هنا ↶

قناة الكلايش  : @FGFFG
""")
@zahid.on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "🝳︙  بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            "**🝳︙   تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **🝳︙  عـدد الثوانـي ⏱**",        )
    event = await edit_or_reply(event, f"`🝳︙   حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")
    sleep(counter)
    await event.edit("** 🝳︙  حسنـاً، أنـا نشـط الآن ᯤ **")
@zahid.on(admin_cmd(pattern="تاريخ التنصيب$"))
async def psu(event):
    uname = platform.uname()
    softw = "**تاريخ تنصيب **\n ** بوت تليثون لديك :**"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"` {bt.year}/{bt.month}/{bt.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    help_string = f"{str(softw)}\n"
    await event.edit(help_string)
@zahid.on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(event, f"**🝳︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"**🝳︙  📑 يرجى متابع قناه الفارات تجدها هنا : Telethon Zahid")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(event, f"**🝳︙ قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")
            if not vinfo:
                return await edit_delete(event, f"**🝳︙ يـجب وضع القـيمـة الصحـيحه**")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**🝳︙ يـجـب وضـع رابـط صحـيح **")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID,f"**🝳︙ اضف فـار\n🝳︙ {vname} الفارالذي تم تعديله :")
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(event, f"**🝳︙  📑 القيـمة لـ {vname} \n🝳︙   تـم تغييـرها لـ :-** `{vinfo}`", time=20)
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(event, f"**🝳︙  📑 قيـمة الـ {vname}** \n🝳︙   هية  `{var_data}`", time=20)
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"**🝳︙ حـذف فـار **\n**🝳︙ {vname}** تـم حـذف هـذا الفـار **")
            await edit_delete(event,f"**🝳︙  📑 قيـمة الـ {vname}** \n**🝳︙   تم حذفها ووضع القيمه الاصلية لها**",time=20)
    else:
        await edit_delete(event, f"**🝳︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)

def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )
    return indentitems(items, indent, level=0)
@zahid.on(admin_cmd(pattern="استخدامي$"))
async def psu(event):
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu = "**حجم استخدامك لتليثون :**\n"
    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"
    svmem = psutil.virtual_memory()
    help_string = f"{str(cpuu)}\n"
    await event.edit(help_string)
@zahid.on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    catevent = await edit_or_reply(event, "**🝳︙   جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")
    start = time.time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time.time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await catevent.edit(                """**🝳︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🝳︙   التنزيل 📶 :** `{} (or) {} ميغا بايت`
**🝳︙   الرفع 📶 :** `{} (or) {} ميغا بايت`
**🝳︙   البنك :** {}` بالثانية`
**🝳︙   مزود خدمة الإنترنت 📢 :** `{}`
**🝳︙   تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )
        else:
            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )
            await event.delete()
    except Exception as exc:
        await catevent.edit(            
"""**🝳︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🝳︙   التنزيل 📶:** `{} (or) {} ميغا بايت`
**🝳︙   الرفع 📶:** `{} (or) {} ميغا بايت`
**🝳︙   البنك :** {}` بالثانية`
**🝳︙  مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("تنصيب") and zahid.query.user_id == bot.uid:
            buttons = [[Button.url("1- شرح التنصيب", "https://youtu.be/44tYK_yV02Q"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("4- بوت فاذر", "http://t.me/BotFather"),],]
            if ZAHIDPC and ZAHIDPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(ZAHIDPC, text=help1, buttons=buttons, link_preview=False)
            elif ZAHIDPC:
                result = builder.document(ZAHIDPC,title="zahid",text=help1,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="zahid",text=help1,buttons=buttons,link_preview=False)
            await zahid.answer([result] if result else None)






@zahid.on(admin_cmd(pattern=f"{ORDERS}(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **
❨ Order telethon Arab  ❩
———————×———————
🝳  اوامر السورس ↢ ( .م1 )
🝳  اوامر الحساب ↢ ( .م2 )
🝳  اوامر الكروب  ↢ ( .م3 )
🝳  اوامر الكروب² ↢ ( .م4 )
🝳  اوامر التحويلات ↢ ( .م5 )
🝳  اوامر الالعاب ↢ ( .م6 )
🝳  اوامر الميمز  ↢ ( .م7 )
🝳  اوامر التسلية ↢ ( .م8 )
🝳  اوامر الوقتية ↢ ( .م9 )
🝳  اوامر الفارات ↢ ( .م10 )
🝳  اوامر السوبرات ↢ ( .م11 )
🝳  اوامر الاغاني ↢ ( .م12 )
🝳  اوامر التكرار ↢ ( .م13 )
🝳  اوامر الزخرفة ↢ ( .م14 )
🝳  اوامر الوسائط ↢ ( .م15 )
🝳  اوامر الملصقات ↢ ( .م16 )
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة . **""")
@zahid.on(admin_cmd(pattern="م9(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوقتي   ⦒  :**
———————×———————
 الأمر  ⦙ ( .اسم وقتي )
الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
———————×———————
 الأمر  ⦙ ( .نبذه وقتيه )
الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
———————×———————
الأمر ⦙ ( .صوره وقتيه )
الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
———————×———————
**شرح الايقاف :**
( .ايقاف صوره وقتيه )
( .ايقاف نبذه وقتيه )
( .ايقاف اسم وقتي )
———————×———————
""")
@zahid.on(admin_cmd(pattern="م10(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ( اوامر الفارات وتغيرات ) :
———————×———————
• لتغير شكل امر السورس او  الفحص اضغط هنا  ↶
  • لتغير صوره او فيديو امر الفحص اضغط هنا ↶
  • لتغير كليشة امر حماية الخاص اضغط هنا ↶
  • لوضع صوره او فيديو حماية الخاص اضغط هنا ↶
  • لتغير عدد تحذيرات حماية الخاص اضغط هنا ↶
  • لتغير نبذه الوقتيه اضغط هنا ↶
  • لتغير صوره وقتيه اضغط هنا ↶
  • لتغير خط زخرفه اسم وقتي اضغط هنا ↶
  •  لوضع ايموجي بجانب اسم وقتي اضغط هنا ↶
• لتغير امر من الاوامر اضغط هنا ↶
• لكيفيه حذف الفار اضغط هنا ↶
———————×——————— 
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@zahid.on(admin_cmd(pattern="م11(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑  اوامر السوبرات  ⦒  :**
———————×———————
 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله
الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
———————×———————
 الأمر  ⦙ .للكروب + الرد على الرساله
الشرح :  يرسل الرسالها الى جميع المجموعات
———————×———————
 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )
الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
———————×———————
الأمر  ⦙  ( .ستوب )
الشرح  ⦙  ايقاف النشر التلقائي المؤقت
———————×———————
 الأمر  ⦙ .اضافه + رابط الكروب
الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
 ———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@zahid.on(admin_cmd(pattern="م12(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر  الاغاني. ⦒  : **
———————×———————
الأمر  ⦙ .بحث صوت + اسم الاغنيه
الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————×——————— 
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 
الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
———————×——————— 
الأمر  ⦙ .تخزين الصوت + الرد ع البصمه
الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
———————×———————
الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو
الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
———————×——————— 
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه
الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
———————×———————
الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )
الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@zahid.on(admin_cmd(pattern="م13(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **⦑   اوامر التكرار    ⦒  : **
———————×——————— 
الشرح  ⦙ ( .تكرار + الكلمة + العدد )
الأمر :  يرسل الكلمة يكررها على عدد المرات  
———————×———————  
الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )
الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
———————×———————
الأمر  ⦙ ( .تكرار_احرف  + الكلمة )
الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
———————×———————
الأمر  ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————×——————— 
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )
الشرح : يرسل اليك الجملة كل وقت معين 
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .
""")
@zahid.on(admin_cmd(pattern="م14(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   لأوامر الزخرفة   ⦒  : **
———————×———————
⑴  ⦙ .غمق + الرد على رساله 
✐ :  يحول خط الرسالة غامقه  
———————×——————— 
⑵  ⦙ .ينسخ + الرد على رساله 
✐ :  يحول خط الرساله الى كلام ينسخ  
———————×———————
⑶  ⦙ .خط سفلي + الرد على رساله 
✐ :   يضيف الى خط رساله خط سفلي 
———————×——————— 
⑷  ⦙ .كتابه + الكلام بالانكلش 
✐ : يكتب الكلام على ورقه بخط اليد 100% ❝ 
 ———————×——————— 
⑸  ⦙ .زخرفه_انكليزي + الاسم 
✐ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
———————×———————
⑹ ⦙ .زخرفه_عربي + الاسم 
✐ : يزخرف الاسم العربي لعده زخرفات 
———————×———————
⑺ ⦙  .بايوهات1
✐ :  يعطيك بايو انستا متعدده 1 
———————×———————
⑻ ⦙ .بايوهات2
✐ :  يعطيك بايو انستا متعدده 2 
———————×———————
⑼ ⦙  .رموز1
✐ :  يعطيك رموز للزخرفه 1 
———————×———————
10 ⦙ .رموز2
✐ :  يعطيك رموز للزخرفه2 
———————×———————
""")



if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and zahid.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]
            result = builder.article(title="zahid", text=help2, buttons=buttons, link_preview=False)
            await zahid.answer([result] if result else None)
@zahid.on(admin_cmd(pattern="م15(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوسائـط   ⦒  :**
———————×———————
⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 
✐  : يقوم بتصغير الوسائط 
———————×———————
⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو
✐  : يعكس الالوان الموجودة في الوسائط
———————×———————
⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو
✐  : يقوم باضافه فلتر احمر الى وسائط
———————×———————
⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو
✐  :  يقوم باضافه فلتر رصاصي الى وسائط
———————×———————
⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )
✐  : يقوم بتحويل وجهه الوسائط الى اليمين
———————×———————
⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو
✐  : يقلب الوسائط من فوق لتحت
———————×———————
⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو
✐  :  يقوم بتقريب على الوسائط
———————×———————
⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو
✐  : يضيف اطار الى الوسائط
———————×———————
⑼ ⦙ .لوقو + الاسم
✐  : يقوم بصنع logo خاص بك
———————×———————
""")
@zahid.on(admin_cmd(pattern="م16(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر الملصقات   ⦒  : **
———————×———————
 ⑴ ⦙ .جلب الملصقات + الرد على الملصق
✐  : يجلب اليك ملصقات الحزمه
———————×———————
⑵ ⦙  .انشاء حزمه ملصقات + الرد على الملصق
✐  : يضع الملصق بحزمه بشكل مقصوص
———————×———————
⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )
✐  : يجلب لك جميع معلومات الملصق
———————×———————
⑷ ⦙ .ملصق + اسم الحزمه او الملصق
✐  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
———————×———————
""")

@zahid.on(admin_cmd(pattern="م1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ** ⦑   اوامر السورس   ⦒  :**
———————×———————
الأمر ⦙ ( .السورس )
الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
———————×——————— 
الأمر ⦙ ( .رابط التنصيب )
الشرح  : سوف يعطيك رابط التنصيب ❝ 
———————×——————— 
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )
الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝ 
———————×——————— 
الأمر ⦙ ( .المده )
الشرح  : يضهر لك مدة تشغيل بوت تليثون لديك 
———————×———————
الأمر ⦙ ( .تحميل ملف + الرد ع الملف )
الشرح : يحمل ملفات تليثون 
———————×———————
الأمر ⦙ ( .مسح ملف + الرد ع الملف )
الشرح :  يمسح الملف الي حملته  
———————×———————
الأمر ⦙ ( .تحديث )
الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون 
———————×———————
الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )
الشرح : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون 
———————×———————
الأمر ⦙ ( .الاوامر ) 
الشرح :   لأضهار جميع اوامر السورس اونلاين
———————×———————
الأمر ⦙ ( .اوامري )
الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
———————×———————
الأمر ⦙ ( .استخدامي )
الشرح :   يضهر لك كمية استخدامك لتليثون
———————×———————
الأمر ⦙ ( .تاريخ التنصيب )
الشرح :   يضهر لك تاريخ تنصيبك
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")

@zahid.on(admin_cmd(pattern="م2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,
"""**  ⦑   اوامـر الحـسـاب  ⦒ : **
———————×———————
الأمر︙( .معرفه + الرد ع الشخص )
شرح︙سيجلب لك معرف الشخص 
———————×———————
الأمر︙( .سجل الاسماء + الرد ع الشخص ) 
شرح︙يجلب لك اسماء الشخص القديمه 
———————×———————
الأمر︙( .انشاء بريد )
شرح︙ينشئ لك بريد وهمي 
———————×———————
الأمر︙( .ايدي + الرد ع الشخص )
شرح︙سيعطيك معلومات الشخص 
———————×———————
الأمر︙( . الايدي الرد ع الشخص )
شرح︙سوف يعطيك ايدي المجموعه او ايدي حسابك 
———————×———————
الأمر︙( .معلومات تخزين المجموعه )
شرح︙يجلب لك جميع معلومات الوسائط  
———————×———————
الأمر︙( .تخزين الخاص تشغيل )
شرح︙يخزن لك جميع الرسائل التي  في الخاص 
———————×———————
الأمر︙( .تخزين الخاص ايقاف )
شرح︙يوقف  تخزين الرسائل اليك في الخاص 
———————×———————
الأمر︙( .تخزين الكروبات تشغيل )
شرح︙يخزم جميع الرسائل التي يتم رد عليك 
———————×———————
الأمر︙( .تخزين الكروبات ايقاف )
شرح︙يوقف لك جميع تخزين رسائل
———————×———————
 الأمر  ︙( .صورته + الرد ع الشخص )
شرح︙يجلب صوره الشخص
———×———
الأمر︙( .رابطه + الرد ع الشخص )
شرح︙يجلب لك رابط الشخص
———×———
الأمر︙( .اسمه + الرد ع الشخص )
شرح︙يجلب لك اسم الشخص الذي تم رد عليه 
———×———
الأمر︙( .نسخ + الرد ع الرساله )
شرح︙يرسل الرساله التي تم رد عليها 
———×———
الأمر︙( .كورونا + اسم المدينه )
شرح︙يجلب لك مرض كورونا و معلومات
———×———
الأمر︙( .الاذان + اسم المدينه )
شرح︙يجلب لك معلومات الاذان 
———×———
الأمر︙( .رابط تطبيق + اسم التطبيق )
شرح︙يرسل رابط التطبيق مع معلوماته 
———×———
الأمر︙( .تاريخ الرساله + الرد ع الرساله )
شرح︙يجلب لك تاريخ الرساله بالتفصيل 
———×———
الأمر︙( .بنك )
شرح︙يقيس سرعه استجابه 
———×———
الأمر︙( .سرعه الانترنيت )
شرح︙يجلب لك سرعه الانترنيت لديك 
———×———
الأمر︙( .الوقت )
شرح︙يضهر لك الوقت والتاريخ 
———×———
الأمر︙( .وقتي )
شرح︙الوقت والتاريخ شكل اخر
———×———
الأمر︙.حالتي 
✐  :  لفحص الحظر
———×———
الأمر︙.طقس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———×———
الأمر︙ .طقوس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———×———
الأمر︙ .مدينه الطقس + اسم المدينه 
شرح︙ لتحديد طقس المدينه تلقائي
———×———
الأمر︙ .ازاله التوجيه + الرد على رساله
شرح︙ يرسل اليك الرساله بدون توجية
———×———
الأمر︙.كشف + الرد على شخص
شرح︙ رد على شخص يفحص الحظر
———×———
الأمر︙.وضع بايو + الرد على البايو
شرح︙ يضع الكلمه في البايو الخاص بك
———×———
الأمر︙.وضع اسم + الرد على الاسم
شرح︙ يضع الاسم في اسمك
———×———
الأمر︙.وضع صوره + الرد على صوره
شرح︙يضع الصوره في حسابك
———×———
الأمر︙.معرفاتي
شرح︙يجلب جميع معرفاتك
———×———
الأمر︙ .تحويل ملكية + معرف الشخص
شرح︙يحول ملكيه القناه او المجموعه 
———×———
الأمر︙ .انتحال + الرد على الشخص
شرح︙ ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك
———×———
الأمر︙.الغاء الانتحال + الرد على الشخص
شرح︙ يقوم بالغاء الانتحال 
———×———
الأمر︙.ازعاج + الرد على شخص
شرح︙يقوم بتكرار الرسائل الشخص 
———×———
الأمر︙.الغاء الازعاج
شرح : يوقف جميع الازعاجات في المجموعه 
 ———×———
 الأمر︙.المزعجهم
شرح︙ يضهر اليك جميع الذين مفعل عليهم الازعاج 
———×———
الأمر︙( .الحماية تشغيل )
شرح︙ يقوم بتشغيل رساله الحمايه اي شخص يراسلك سوف يقوم بتنبيه
———×———
الأمر︙( .الحماية ايقاف )
شرح︙يقوم بتعطيل رساله الحماية الخاص
———×———
الأمر︙( .قبول )
شرح︙ يقوم بقبول الشخص للأرسال اليك
———×———
الأمر︙( .رفض )
شرح︙الغاء قبول الشخص من الارسال 
———×———
الأمر︙( .مرفوض )
شرح︙حظر الشخص 
———×———
الأمر︙( .المقبولين )
شرح︙عرض قائمة المقبولين ي الحماية 
———×———
الأمر︙( .جلب الوقتيه + الرد على الصورة )
شرح︙حفض صوره وقتيه في الحافضة 
———×———
الأمر︙( .تاك بالكلام + الكلمه + معرف الشخص )
شرح︙ يسوي تاك للشخص بالرابط جربه وتعرف 
———×———
الأمر︙( .نسخ + الرد على رساله )
شرح︙ يرسل الرساله التي رديت عليها
———×———
الأمر︙.احسب + المعادله
شرح︙يجمع او يطرح او يقسم
———×———
الأمر  ⦙  ( .كول + الكلمة )
الشرح : يجب اضافه بوتك يتكلم بدلا عنك 
———×———
الأمر  ⦙ ( .وضع النائم + السبب )
الشرح : اي شخص يعملك تاك او يراسلك او يرد عليك يرد عليه تليثون بكليشة انا حاليا غير موجود ويضع له السبب الي نتة وضعته
———×———
الأمر  ⦙  .الصور + الرد على الشخص 
الشرح : يجلب لك جميع صور الشخص و يمكن وضع رقم بجانب الأمر
———×———
الأمر  ⦙  .زاجل + معرف الشخص + الرساله 
الشرح : يرسل الرساله الى الشخص 
———×———
الأمر ⦙ .فيديو
الشرح  : يرسل فيديو عشوائي
———×———
الأمر  ⦙ .فيديو2
الشرح :  يرسل فيديو عشوائي
———×———
الأمر ⦙ .فايروس
الشرح :  يرسل فايروس
———×———
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .
""")

@zahid.on(admin_cmd(pattern="م3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 1  ⦒  :**

———————×——————— 
 الأمر  ⦙  ( .كتم + الرد ع الشخص )
الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 
الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )
الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  
 ———————×——————— 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
———————×——————— 
الأمر ⦙  ( .معلومات )
الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
 ———————×——————— 
الأمر ⦙  ( .المحذوفين )
الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
———————×——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
———————×——————— 
الأمر ⦙  ( .انتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  
الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
———————×———————
الأمر  ⦙  ( .ترحيب + الرساله )
الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  
الأمر  ⦙   ( .مسح الترحيبات )
الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
———————×——————— 
الأمر  ⦙  ( .ترحيباتي )
الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
———————×——————— 
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 
الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 
الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )
الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
———————×——————— 
الأمر ⦙  ( .اضف رد + الكلمه )
الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 
الأمر ⦙  ( .مسح رد + الكلمه )
الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 
الأمر ⦙  ( .جميع الردود )
 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  
الأمر ⦙  ( .مسح جميع الردود )
الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
———————×——————— 
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )
الشرح  ⦙ يقوم بعمل مجموعه خارقه 
الأمر ⦙  ( .صنع قناه +  اسم القناة )
الشرح  ⦙ يقوم بعمل قناه خاصه  
———————×——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
———————×———————
الأمر  ⦙  ( .تفعيل حمايه المجموعه )
الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل
الأمر  ⦙ تعطيل حمايه المجموعه
الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
———————×——————— 
الأمر  ⦙  ( .صلاحيات المجموعه )
الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
———————×———————
الأمر  ⦙  ( .رفع مشرف + الرد على شخص )
الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
———————×——————— 
الأمر  ⦙  ( .منع + كلمة )
الشرح  ⦙ منع كلمه من الارسال في الكروب
الأمر ⦙  ( .الغاء منع + كلمه )
الشرح  ⦙ يقوم بالغاء منع الكلمه  
———————×——————— 
الأمر ⦙  ( .قائمه المنع )
الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
———————×——————— 
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
———————×——————— 
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
———————×———————
الأمر  ⦙  ( .تنظيف الوسائط )
 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
———————×——————— 
الأمر  ⦙  ( .حذف الرسائل )
الشرح  ⦙ يحذف جميع الرسائل بلكروب  
  او  .حذف الرسائل + العدد 
———————×——————— 
الأمر  ⦙  ( .مسح + الرد على رسالة )
الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
———————×——————— 
الأمر  ⦙  ( .غادر )
الشرح  ⦙ يغادر من المجموعه او من القناة
———————×——————— 
الأمر  ⦙  ( .تفليش )
الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
———————×——————— 
الأمر ⦙  ( .اضافه + رابط الكروب )
الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 
 ( يجب ان تتاكد انك  لست محضور ارسل ⬅️
( .فحص الحظر ) من اجل التاكد
———————×——————— 
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )
الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
———————×——————— 
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")
@zahid.on(admin_cmd(pattern="م4(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 2  ⦒  : **
———————×——————— 
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )
الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
———————×——————— 
الأمر ⦙  ( .نسخ + الرد على رساله )
الشرح  ⦙ يرسل الرساله التي رديت عليها 
———————×——————— 
الأمر ⦙  ( .ابلاغ الادمنيه )
الشرح  ⦙ يعمل تاك لجميع الادمنيه  
———————×——————— 
الأمر ⦙  ( .المشرفين )
الشرح  ⦙ يجلب اليك جميع المشرفين 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
———————×———————
الأمر ⦙  ( .حظر + الرد على شخص )
الشرح  ⦙ حظر الشخص من المجموعه 
الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )
الشرح  ⦙ يلغي حظر الشخص من المجموعه
———————×——————— 
الأمر  ⦙  ( .بدء مكالمه )
الشرح  ⦙ يقوم بتشغيل مكالمه 
الأمر ⦙  ( .دعوه للمكالمه )
الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
———————×——————— 
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )
الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
———————×——————— 
الأمر  ⦙  ( .تثبيت + الرد على رساله )
 شرح : تثبيت الرساله التي رديت عليها
———————×——————— 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
———————×——————— 
الأمر ⦙  ( .تفليش )
الشرح  ⦙  أزاله جميع اعضاء المجموعه
 ———————×——————— 
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين 
———————×——————— 
الأمر  ⦙  ( .المحذوفين )
الشرح  ⦙  يجلب لك الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ مسح الحسابات المحذوفه
———————×——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
———————×——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ يقوم بحساب عدد رسائلك 
———————×——————— 
الأمر ⦙  ( .جلب الاحداث )
الشرح  ⦙ يجلب اخر 20 رساله محذوفه
———————×———————
الأمر  ⦙ ( .حظر عام + الرد على شخص ) 
الشرح  ⦙ حظر من جميع الكروبات   
———————×———————
الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )
الشرح  ⦙ الغاء حضر العام  
———————×———————
الأمر  ⦙ ( .المحظورين عام )
الشرح ⦙  يضهر المحضورين عام 
———————×———————
الشرح  ⦙ ( .تقيد + الرد على شخص )
الأمر  ⦙ يقيد الشخص من المجموعة 
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")
@zahid.on(admin_cmd(pattern="م5(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑  اوامر تحويل الصيغ  ⦒  :**
———————×——————
الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3
الشرح : يحول صوت mp3 الى بصمه 
———————×——————
الأمر ⦙  .تحويل صوت + الرد ع الصوت 
الشرح  :  يحول البصمه الى صوت   mp3
———————×——————
الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 
الشرح :  يحول الصوره الى ملصق 
———————×——————
الأمر  ⦙ . تحويل صوره + الرد ع الملصق 
الشرح :  يحول الملصق الى صوره 
———————×——————
الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 
الشرح :  يقوم بتحويل الفيديو الى متحركه 
———————×——————
الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره
الشرح :  يحول الملف الى بي دي اف 
———————×—————— 
الأمر  ⦙ .ملصقي + الرد ع الرساله 
الشرح  : يحول رساله الى ملصق 
———————×——————
الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره
الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
———————×——————
الأمر ⦙  ( .تحويل رساله + الرد ع الملف )
الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
———————×——————
الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )
الشرح : يحول الفيديو الى فيديو دائري مرئي 
———————×——————
الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )
الشرح :  يحول الملصق الى ملصق دائري
———————×——————
 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )
الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
———————×——————
الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )
الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
———————×——————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")
@zahid.on(admin_cmd(pattern="م6(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
**  ⦑   اوامر الالعاب 1   ⦒  :**
———————×———————
شرح  ⦙   نسبة وهميه - الأوامر :
الأمر  ⦙ ( .نسبه الحب + الرد ع الشخص )
الأمر  ⦙ ( . نسبه الانحراف + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الكراهيه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه المثليه +الرد ع الشخص )
الأمر  ⦙ ( . نسبه النجاح + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الانوثه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الغباء + الرد ع الشخص )
———————×———————
شرح  ⦙  رفع وهمي - الأوامر  :
الأمر  ⦙ ( .رفع زباله + الرد ع الشخص )
الأمر  ⦙ ( .رفع منشئ + الرد ع الشخص )
الأمر  ⦙ ( .رفع مدير + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطور + الرد ع الشخص )
الأمر  ⦙ ( .رفع مثلي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كواد + الرد ع الشخص )
الأمر  ⦙ ( .رفع مرتبط + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كحبه + الرد ع الشخص )
الأمر  ⦙ ( .رفع زوجتي + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاك + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاكه + الرد ع الشخص )
———————×———————
الأمر  ⦙ ( .كت )
الشرح ⦙ لعبه اسأله كت تويت عشوائيه 
———————×———————
الأمر  ⦙ ( .اكس او )
الشرح ⦙  لعبه اكس او دز الامر و اللعب ويا صديقك 
———————×———————
الأمر  ⦙  ( .همسه + الكلام + معرف الشخص )
الشرح  ⦙  يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  
———————×———————
الأمر  ⦙  ( .رسم شعار + الاسم )
الشرح ⦙  يرسم شعار للأسم  
———————×———————
الأمر  ⦙ ( .نص ثري دي + الكلمه )
الشرح ⦙ يقوم بكتابه الكلمه بشكل ثلاثي الابعاد 
———————×———————
الأمر  ⦙  ( .كلام متحرك + الكلام )
الشرح ⦙ يقوم بكتابه الكلام حرف حرف  
———————×———————
الأمر ⦙ ( .ملصق متحرك + الكلام )
الشرح  ⦙ يقوم بكتابه الكلام بملصق متحرك  
———————×———————
الأمر  ⦙  ( .بورن + معرف الشخص + الكلام + الرد ع اي صوره )
الشرح ⦙  قم بتجربه الامر لتعرفه +18  
———————×———————
الأمر  ⦙ ( .رسم قلوب + الاسم )
الشرح  ⦙  يكتب الاسم ع شكل قلوب  
———————×———————

⑴  ⦙  ( .كتابه وهمي + عدد الثواني )
⑵  ⦙  ( .فيديو وهمي + عدد الثواني )
⑶  ⦙  ( .صوره وهمي + عدد الثواني )
⑷  ⦙  ( .جهه اتصال وهمي + عدد الثواني )
⑸  ⦙  ( .موقع وهمي + عدد الثواني )
⑹  ⦙  ( .لعب وهمي + عدد الثواني )

الشرح  ⦙ هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني
———————×———————
⑴  ⦙ ( .شوت + الكلمة )
✐ :  امر تسليه جربه وتعرف  
———————×———————
⑵  ⦙ ( .كتابه + الكلام بالانكلش )
✐ :   يكتب الكلام على ورقه بخط اليد 100%   
———————×———————
الشرح  ⦙   العـاب اخـرى فقط قم بنسخ الأمر وارسالـة   :- الأوامر :
1. - ( .لعبه تيك توك اربعه )
2. - ( .لعبه تيك توك اثنان 3 )
3. - ( .لعبه ربط أربعة )
4. - ( .لعبه قرعة )
5. - ( .لعبه حجر-ورقة-مقص )
6. - ( .لعبه روليت )
7. - ( .لعبه داما )
8. - ( .لعبه داما تجمع )
———————×———————
الأمر  ⦙ ( .هديه + الكلام )
الشرح :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  
———————×——————— 
الأمر  ⦙ ( .ضفدع + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   
———————×——————— 
الأمر  ⦙  ( .لافته + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف    
———————×——————— 
الأمر ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
———————×——————— 
الأمر ⦙  (.صفق + الرد على الكلام )
الشرح : جربه وتعرف مضحك 
———————×——————— 
الأمر  ⦙ ( .حضر وهمي + الرد على شخص )
الشرح : حظر وهمي جربه وتعرف 
———————×———————
الأمر ⦙ ( .خط ملصق + الكلمه )
الشرح : يدعم انكليزي فقط + يحول الكتابه لملصق 
———————×———————
الأمر  ⦙ ( .شعر )
الشرح : يرسل الك شعر ميمز او مضحك 
———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")
@zahid.on(admin_cmd(pattern="م7(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑   بصمات تحشيش 1   ⦒  :**
———————×———————
(.ص1) ⦙  ابو  عباس  لو  تاكل  خره
(.ص2) ⦙  استمر  نحن  معك
(.ص3) ⦙  افحط  بوجه
(.ص4) ⦙  اكعد  لا  اسطرك  سطره  العباس
(.ص5) ⦙  اللهم  لا  شماته
(.ص6) ⦙  امرع  دينه
(.ص7) ⦙  امشي  بربوك
(.ص8) ⦙  انت  اسكت  انت  اسكت
(.ص9) ⦙  انت  سايق  زربه
(.ص10) ⦙  اوني  تشان
(.ص11) ⦙  برافو  عليك  استادي 
(.ص12) ⦙  بلوك  محترم
(.ص13) ⦙  بووم  في  منتصف  الجبهة 
(.ص14) ⦙  بيتش 
(.ص15) ⦙  تخوني  ؟
(.ص16) ⦙  تره  متكدرلي
(.ص17) ⦙  تعبان  اوي
(.ص18) ⦙  تكذب
(.ص19) ⦙  حسبي  الله
(.ص20) ⦙  حشاش 
(.ص21) ⦙  حقير  
(.ص22) ⦙  خاص  
(.ص23) ⦙  خاله  ما  تنامون  
(.ص24) ⦙  خرب  شرفي  اذا  ابقى  بالعراق 
(.ص25) ⦙  دكات  الوكت  الاغبر  
(.ص26) ⦙  ررردح  
(.ص27) ⦙  سلامن  عليكم  
(.ص28) ⦙  بوم منتصف جبهه   
(.ص29) ⦙  شكد  شفت  ناس  مدودة
(.ص30) ⦙ شلون  ، 
(.ص31) ⦙ صح  لنوم  
(.ص32) ⦙ صمت  
(.ص33) ⦙ ضحكة  مصطفى  الحجي  
(.ص34) ⦙ طماطه  
(.ص35) ⦙ طيح  الله  حضك  
(.ص36) ⦙ فاك  يوو  
(.ص37) ⦙ اني فرحان وعمامي فرحانين
(.ص38) ⦙ لا  تضل  تضرط  
(.ص39) ⦙ لا  تقتل  المتعه  يا  مسلم  
(.ص40) ⦙ لا  مستحيل  
(.ص41) ⦙ لا  والله  شو  عصبي  
(.ص42) ⦙ لش  
(.ص43) ⦙ لك  اني  شعليه  
(.ص44) ⦙ ما  اشرب  
(.ص45) ⦙ مع  الاسف  
(.ص46) ⦙ مقتدى  
(.ص47) ⦙ من  رخصتكم  
(.ص48) ⦙ منو  انت  
(.ص49) ⦙ منورني  
(.ص50) ⦙  نتلاكه  بالدور  الثاني 
(.ص51) ⦙  نستودعكم  الله  
(.ص52) ⦙  ها  شنهي  
(.ص53) ⦙  ههاي  الافكار  حطها ب
(.ص54) ⦙  ليش شنو سببها ليش
(.ص55) ⦙  يموتون  جهالي
(.ص56) ⦙  اريد انام
(.ص57) ⦙  افتحك فتح
(.ص58) ⦙  اكل خره لدوخني
(.ص59) ⦙  السيد شنهو السيد
(.ص60) ⦙  زيج2
(.ص61) ⦙  زيج لهارون
(.ص62) ⦙  زيج الناصرية
(.ص63) ⦙  راقبو اطفالكم
(.ص64) ⦙  راح اموتن
(.ص65) ⦙  ذس اس مضرطة
(.ص66) ⦙  دروح سرسح منا
(.ص67) ⦙  خويه ما دكوم بيه
(.ص68) ⦙  خلصت تمسلت ديلة كافي انجب
(.ص69) ⦙  بعدك تخاف
(.ص70) ⦙  بسبوس
(.ص71) ⦙  اني بتيتة كحبة
(.ص72) ⦙  انعل ابوكم لابو اليلعب وياكم طوبة
(.ص73) ⦙  انت شدخلك
(.ص74) ⦙  انا ماشي بطلع
(.ص75) ⦙  امداك وامده الخلفتك
(.ص76) ⦙  امبيههههه
(.ص77) ⦙  هدي بيبي
(.ص78) ⦙  هاه صدك تحجي
(.ص79) ⦙  مو كتلك رجعني
(.ص80) ⦙  مامرجية منك هاية
(.ص81) ⦙  ليش هيجي
(.ص82) ⦙  كـــافـي
(.ص83) ⦙  كس اخت السيد
(.ص84) ⦙  شنو كواد ولك اني هنا
(.ص85) ⦙  شجلبت
(.ص86) ⦙  شبيك وجه الدبس
(.ص87) ⦙  سييييي
(.ص88) ⦙  زيجج1
(.ص89) ⦙  يموتون جهالي
(.ص90) ⦙  ياخي اسكت اسكت
(.ص91) ⦙  وينهم
(.ص92) ⦙  هيلو سامر وحود
(.ص93) ⦙  هو
(.ص94) ⦙  ههاي الافكار حطها
  ———————×———————
قناه السورس : ( Telethon Zahid ) .
جميع الاوامر تكون بدايتها نقطة .""")
@zahid.on(admin_cmd(pattern="م8(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑    الاوامر المتحركه للتسلية   ⦒  :**
———————×——————— 
( .غبي ) ( .تفجير ) ( .قتل ) ( .طوبه ) ( .مربعات ) ( .حلويات ) ( .نار ) ( .هلكوبتر ) ( .اشكال مربع ) ( .دائره )( .قلب ) ( .مزاج ) ( .قرد ) ( .ايد ) ( .العد التنازلي ) ( .الوان قلوب ) ( .عين ) ( .ثعبان ) ( .رجل ) ( .رموز شيطانيه ) ( .قطار ) ( .موسيقى ) ( .رسم ) ( .فراشه ) ( .مكعبات ) ( .مطر ) ( .تحركات ) ( .ايموجيات ) ( .طائره )( .شرطي ) ( .النضام الشمسي ) ( .افكر ) ( .اضحك ) ( .ضايج ) ( .ساعه متحركه )( .بوسه ) ( .قلوب ) ( .رياضه )( .الارض ) ( .قمر ) (.اقمار ) ( .قمور ) ( .زرفه ) ( .بيبي ) ( .تفاعلات ) ( .اخذ قلبي ) 
( .اشوفج السطح ) ( .احبك ) ( .اركض ) ( .روميو ) ( .البنك ) ( .تهكير ) ( .طياره ) ( .مصاصه ) ( .مصه ) ( .جكه ) ( .اركضلي ) ( .حمامه ) ( .فواكه ) ( .الحياة ) ( .هلو ) ( .مربعاتي ) ( .اسعاف ) ( .سمايلي )
———————×———————
""")


@zahid.on(admin_cmd(pattern="هاش ([\s\S]*)"))    
async def gethash(hash_q):
    hashtxt_ = "".join(hash_q.text.split(maxsplit=1)[1:])
    with open("hashdis.txt", "w+") as hashtxt:
        hashtxt.write(hashtxt_)
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = f"**Text : **\
            \n`{hashtxt_}`\
            \n**MD5 : **`\
            \n`{md5}`\
            \n**SHA1 : **`\
            \n`{sha1}`\
            \n**SHA256 : **`\
            \n`{sha256}`\
            \n**SHA512 : **`\
            \n`{sha512[:-1]}`\
         "
    await edit_or_reply(hash_q, ans)
@zahid.on(admin_cmd(pattern="هاش(ين|دي) ([\s\S]*)"))    
async def endecrypt(event):
    string = "".join(event.text.split(maxsplit=2)[2:])
    catevent = event
    if event.pattern_match.group(1) == "ين":
        if string:
            result = base64.b64encode(bytes(string, "utf-8")).decode("utf-8")
            result = f"**Shhh! It's Encoded : **\n`{result}`"
        else:
            reply = await event.get_reply_message()
            if not reply:
                return await edit_delete(event, "`What should i encode`")
            mediatype = media_type(reply)
            if mediatype is None:
                result = base64.b64encode(bytes(reply.text, "utf-8")).decode("utf-8")
                result = f"**Shhh! It's Encoded : **\n`{result}`"
            else:
                catevent = await edit_or_reply(event, "`Encoding ...`")
                c_time = time.time()
                downloaded_file_name = await event.client.download_media(                    reply,                    Config.TMP_DOWNLOAD_DIRECTORY,                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(                        progress(d, t, catevent, c_time, "trying to download")                    ),                )
                catevent = await edit_or_reply(event, "`Encoding ...`")
                with open(downloaded_file_name, "rb") as image_file:
                    result = base64.b64encode(image_file.read()).decode("utf-8")
                os.remove(downloaded_file_name)
        await edit_or_reply(            catevent, result, file_name="encodedfile.txt", caption="It's Encoded"        )
    else:
        try:
            lething = str(                base64.b64decode(                    bytes(event.pattern_match.group(2), "utf-8"), validate=True                )            )[2:]
            await edit_or_reply(event, "**Decoded text :**\n`" + lething[:-1] + "`")
        except Exception as e:
            await edit_delete(event, f"**Error:**\n__{str(e)}__")
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("اوامر الكروب(?: |$)(.*)") and zahid.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الكروب", data="ord1G"),]]
            result = builder.article(title="zahid", text=help2, buttons=buttons, link_preview=False)
            await zahid.answer([result] if result else None)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        
        if query.startswith("(صيانه|صيانه)") and zahid.query.user_id == bot.uid:
            try:
                buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]
                result = builder.article(title="zahid",text=help2,buttons=buttons,link_preview=False)
                await zahid.answer([result] if result else None)
            except BotInlineDisabledError: 
                await zahid.send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )
           
           

if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("اوامر الحساب(?: |$)(.*)") and zahid.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الحساب", data="ord1hs"),]]
            result = builder.article(title="zahid", text=help2, buttons=buttons, link_preview=False)
            await zahid.answer([result] if result else None)
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("اوامر الالعاب(?: |$)(.*)") and zahid.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الالعاب", data="ord1pl"),]]
            result = builder.article(title="zahid", text=help2, buttons=buttons, link_preview=False)
            await zahid.answer([result] if result else None)

chat = "@BotFather"
@zahid.on(events.NewMessage(outgoing=True, pattern="^.بوت ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("قم بوضع الامر + اسم البوت + معرف البوت !!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinezahid(zahid):
        builder = zahid.builder
        result = None
        query = zahid.text
        await bot.get_me()
        if query.startswith("اوامر الصيغ(?: |$)(.*)") and zahid.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الصيغ", data="ordsag1"),]]
            result = builder.article(title="zahid", text=help2, buttons=buttons, link_preview=False)
            await zahid.answer([result] if result else None)
@zahid.on(admin_cmd(pattern="م21(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 1   ⦒  :**\n\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص1`)   ⦙   ابو  عباس  لو  تاكل  خره\n(`.ص2`)   ⦙   استمر  نحن  معك\n(`.ص3`)   ⦙   افحط  بوجه\n(`.ص4`)   ⦙   اكعد  لا  اسطرك  سطره  العباس\n(`.ص5`)   ⦙   اللهم  لا  شماته\n(`.ص6`)   ⦙   امرع  دينه\n(`.ص7`)   ⦙   امشي  بربوك\n(`.ص8`)   ⦙   انت  اسكت  انت  اسكت\n(`.ص9`)   ⦙   انت  سايق  زربه\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص10`)   ⦙   اوني  تشان\n(`.ص11`)   ⦙   برافو  عليك  استادي \n(`.ص12`)   ⦙   بلوك  محترم\n(`.ص13`)   ⦙   بووم  في  منتصف  الجبهة \n(`.ص14`)   ⦙   بيتش \n(`.ص15`)   ⦙   تخوني  ؟\n(`.ص16`)   ⦙   تره  متكدرلي\n(`.ص17`)   ⦙   تعبان  اوي\n(`.ص18`)   ⦙   تكذب\n(`.ص19`)   ⦙   حسبي  الله\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص20`)   ⦙   حشاش \n(`.ص21`)   ⦙   حقير  \n(`.ص22`)   ⦙   خاص  \n(`.ص23`)   ⦙   خاله  ما  تنامون  \n(`.ص24`)   ⦙   خرب  شرفي  اذا  ابقى  بالعراق \n(`.ص25`)   ⦙   دكات  الوكت  الاغبر  \n(`.ص26`)   ⦙   ررردح  \n(`.ص27`)   ⦙   سلامن  عليكم  \n(`.ص28`)   ⦙   بوم منتصف جبهه   \n(`.ص29`)   ⦙   شكد  شفت  ناس  مدودة\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻")
@zahid.on(admin_cmd(pattern="م22(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 2   ⦒  :**\n\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص30`)   ⦙  شلون  ، \n(`.ص31`)   ⦙  صح  لنوم  \n(`.ص32`)   ⦙  صمت  \n(`.ص33`)   ⦙  ضحكة  مصطفى  الحجي  \n(`.ص34`)   ⦙  طماطه  \n(`.ص35`)   ⦙  طيح  الله  حضك  \n(`.ص36`)   ⦙  فاك  يوو  \n(`.ص37`)   ⦙  اني فرحان وعمامي فرحانين\n(`.ص38`)   ⦙  لا  تضل  تضرط  \n(`.ص39`)   ⦙  لا  تقتل  المتعه  يا  مسلم  \n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص40`)   ⦙  لا  مستحيل  \n(`.ص41`)   ⦙  لا  والله  شو  عصبي  \n(`.ص42`)   ⦙  لش  \n(`.ص43`)   ⦙  لك  اني  شعليه  \n(`.ص44`)   ⦙  ما  اشرب  \n(`.ص45`)   ⦙  مع  الاسف  \n(`.ص46`)   ⦙  مقتدى  \n(`.ص47`)   ⦙  من  رخصتكم  \n(`.ص48`)   ⦙  منو  انت  \n(`.ص49`)   ⦙  منورني  \n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص50`)  ⦙  نتلاكه  بالدور  الثاني \n(`.ص51`)  ⦙  نستودعكم  الله  \n(`.ص52`)  ⦙  ها  شنهي  \n(`.ص53`)  ⦙  ههاي  الافكار  حطها ب\n(`.ص54`)  ⦙  ليش شنو سببها ليش\n(`.ص55`)  ⦙  يموتون  جهالي\n(`.ص56`)  ⦙  اريد انام\n(`.ص57`)  ⦙  افتحك فتح\n(`.ص58`)  ⦙  اكل خره لدوخني\n(`.ص59`)  ⦙  السيد شنهو السيد\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص60`)  ⦙  زيج2\n(`.ص61`)  ⦙  زيج لهارون\n(`.ص62`)  ⦙  زيج الناصرية\n(`.ص63`)  ⦙  راقبو اطفالكم\n(`.ص64`)  ⦙  راح اموتن\n(`.ص65`)  ⦙  ذس اس مضرطة\n(`.ص66`)  ⦙  دروح سرسح منا\n(`.ص67`)  ⦙  خويه ما دكوم بيه\n(`.ص68`)  ⦙  خلصت تمسلت ديلة كافي انجب\n(`.ص69`)  ⦙  بعدك تخاف\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻")
@zahid.on(admin_cmd(pattern="م23(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 3   ⦒  :**\n\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص70`)  ⦙  بسبوس\n(`.ص71`)  ⦙  اني بتيتة كحبة\n(`.ص72`)  ⦙  انعل ابوكم لابو اليلعب وياكم طوبة\n(`.ص73`)  ⦙  انت شدخلك\n(`.ص74`)  ⦙  انا ماشي بطلع\n(`.ص75`)  ⦙  امداك وامده الخلفتك\n(`.ص76`)  ⦙  امبيههههه\n(`.ص77`)  ⦙  هدي بيبي\n(`.ص78`)  ⦙  هاه صدك تحجي\n(`.ص79`)  ⦙  مو كتلك رجعني\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص80`)  ⦙  مامرجية منك هاية\n(`.ص81`)  ⦙  ليش هيجي\n(`.ص82`)  ⦙  كـــافـي\n(`.ص83`)  ⦙  كس اخت السيد\n(`.ص84`)  ⦙  شنو كواد ولك اني هنا\n(`.ص85`)  ⦙  شجلبت\n(`.ص86`)  ⦙  شبيك وجه الدبس\n(`.ص87`)  ⦙  سييييي\n(`.ص88`)  ⦙  زيجج1\n(`.ص89`)  ⦙  يموتون جهالي\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n(`.ص90`)  ⦙  ياخي اسكت اسكت\n(`.ص91`)  ⦙  وينهم\n(`.ص92`)  ⦙  هيلو سامر وحود\n(`.ص93`)  ⦙  هو\n(`.ص94`)  ⦙  ههاي الافكار حطها\n                                                       𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n")
@zahid.on(admin_cmd(pattern="فتح همسه(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**عزيزي كل عقلك ؟  **\n**وين اكو شي اسمه فتح همسة عرض العالم ماتخاف علية ادبسزز ولي يلة 🙂💔**")

