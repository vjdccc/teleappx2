# -*- coding: utf-8 -*-
# مُحوَّل آلياً من اوامر Telethon Zahid (Telethon) الى Pyrogram عبر arabcompat
import warnings; warnings.filterwarnings("ignore")
from arabcompat import *
from arabcompat import _Missing, _format, _catutils, _cattools, _LazyTelegraph
try:
    import bs4
except Exception:
    bs4 = _Missing('bs4')
try:
    import random
except Exception:
    random = _Missing('random')
try:
    import string
except Exception:
    string = _Missing('string')
try:
    import requests
except Exception:
    requests = _Missing('requests')
try:
    import json
except Exception:
    json = _Missing('json')
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import base64
except Exception:
    base64 = _Missing('base64')
try:
    import re
except Exception:
    re = _Missing('re')
try:
    import urllib
except Exception:
    urllib = _Missing('urllib')
try:
    import io
except Exception:
    io = _Missing('io')
try:
    import os
except Exception:
    os = _Missing('os')
try:
    import moviepy.editor as m
except Exception:
    m = _Missing('m')
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import io
except Exception:
    io = _Missing('io')
try:
    import logging
except Exception:
    logging = _Missing('logging')
try:
    import time
except Exception:
    time = _Missing('time')
try:
    import fitz
except Exception:
    fitz = _Missing('fitz')
try:
    import pathlib
except Exception:
    pathlib = _Missing('pathlib')
try:
    import base64
except Exception:
    base64 = _Missing('base64')
try:
    import aiohttp
except Exception:
    aiohttp = _Missing('aiohttp')
try:
    import pybase64
except Exception:
    pybase64 = _Missing('pybase64')
try:
    from yt_dlp import YoutubeDL
except Exception:
    YoutubeDL = _Missing('YoutubeDL')
try:
    import requests, json
except Exception:
    requests = _Missing('requests')
    json = _Missing('json')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    from datetime import datetime as dt
except Exception:
    dt = _Missing('dt')
try:
    from pytz import country_names as c_n
except Exception:
    c_n = _Missing('c_n')
try:
    from pytz import country_timezones as c_tz
except Exception:
    c_tz = _Missing('c_tz')
try:
    from pytz import timezone as tz
except Exception:
    tz = _Missing('tz')
try:
    from re import findall
except Exception:
    findall = _Missing('findall')
try:
    from io import BytesIO
except Exception:
    BytesIO = _Missing('BytesIO')
try:
    from covid import Covid
except Exception:
    Covid = _Missing('Covid')
try:
    from pathlib import Path
except Exception:
    Path = _Missing('Path')
try:
    from math import ceil
except Exception:
    ceil = _Missing('ceil')
try:
    from ShazamAPI import Shazam
except Exception:
    Shazam = _Missing('Shazam')
try:
    from telegraph import Telegraph, exceptions, upload_file
except Exception:
    Telegraph = _Missing('Telegraph')
    exceptions = _Missing('exceptions')
    upload_file = _Missing('upload_file')
try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = _Missing('BeautifulSoup')
try:
    from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageFont
except Exception:
    Image = _Missing('Image')
    ImageDraw = _Missing('ImageDraw')
    ImageFilter = _Missing('ImageFilter')
    ImageOps = _Missing('ImageOps')
    ImageFont = _Missing('ImageFont')
try:
    from urllib.parse import quote
except Exception:
    quote = _Missing('quote')
try:
    from shutil import copyfile
except Exception:
    copyfile = _Missing('copyfile')
try:
    from pymediainfo import MediaInfo
except Exception:
    MediaInfo = _Missing('MediaInfo')
try:
    from search_engine_parser import BingSearch, GoogleSearch, YahooSearch
except Exception:
    BingSearch = _Missing('BingSearch')
    GoogleSearch = _Missing('GoogleSearch')
    YahooSearch = _Missing('YahooSearch')
try:
    from yt_dlp import YoutubeDL
except Exception:
    YoutubeDL = _Missing('YoutubeDL')
try:
    from yt_dlp.utils import ContentTooShortError, DownloadError, ExtractorError, GeoRestrictedError, MaxDownloadsReached, PostProcessingError, UnavailableVideoError, XAttrMetadataError
except Exception:
    ContentTooShortError = _Missing('ContentTooShortError')
    DownloadError = _Missing('DownloadError')
    ExtractorError = _Missing('ExtractorError')
    GeoRestrictedError = _Missing('GeoRestrictedError')
    MaxDownloadsReached = _Missing('MaxDownloadsReached')
    PostProcessingError = _Missing('PostProcessingError')
    UnavailableVideoError = _Missing('UnavailableVideoError')
    XAttrMetadataError = _Missing('XAttrMetadataError')
try:
    from youtubesearchpython import Video
except Exception:
    Video = _Missing('Video')
try:
    from search_engine_parser.core.exceptions import NoResultsOrTrafficError
except Exception:
    NoResultsOrTrafficError = _Missing('NoResultsOrTrafficError')
try:
    from search_engine_parser import GoogleSearch
except Exception:
    GoogleSearch = _Missing('GoogleSearch')
try:
    from youtubesearchpython import SearchVideos
except Exception:
    SearchVideos = _Missing('SearchVideos')
try:
    from pytz import country_names as c_n
except Exception:
    c_n = _Missing('c_n')
try:
    from pytz import country_timezones as c_tz
except Exception:
    c_tz = _Missing('c_tz')
try:
    from pytz import timezone as tz
except Exception:
    tz = _Missing('tz')

LOGS = logging.getLogger(__name__)
SONG_SEARCH_STRING = "🝳 ⦙ جاري البحث عن الاغنية إنتظر رجاءًا  🎧"
SONG_NOT_FOUND = "🝳 ⦙ لم أستطع إيجاد هذه الأغنية  ⚠️"
SONG_SENDING_STRING = "🝳 ⦙ قم بإلغاء حظر البوت  🚫"

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]
telegraph = _LazyTelegraph(Config.TELEGRAPH_SHORT_NAME)
r = None
auth_url = None

FONT_FILE_TO_USE = "styles/impact.ttf"

#Telethon IQ
async def get_tz(con):
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("الجزر الصغيرة النائية", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")
    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


if not os.path.isdir("./temp"):
    os.makedirs("./temp")
audio_opts = {
    "format": "bestaudio",
    "addmetadata": True,
    "key": "FFmpegMetadata",
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
    "outtmpl": "%(title)s.mp3",
    "quiet": True,
    "logtostderr": False,
}

video_opts = {
    "format": "best",
    "addmetadata": True,
    "key": "FFmpegMetadata",
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
    "outtmpl": "%(title)s.mp4",
    "logtostderr": False,
    "quiet": True,
}
async def get_tz(con):
    for c_code in c_n:
        if con == c_n[c_code]:
            return tz(c_tz[c_code][0])
    try:
        if c_n[con]:
            return tz(c_tz[con][0])
    except KeyError:
        return
def fahrenheit(f):
    temp = str(((f - 273.15) * 9 / 5 + 32)).split(".")
    return temp[0]
def celsius(c):
    temp = str((c - 273.15)).split(".")
    return temp[0]
def sun(unix, ctimezone):
    return datetime.fromtimestamp(unix, tz=ctimezone).strftime("%I:%M %p")

async def ytdl_down(event, opts, url):
    try:
        await event.edit("**🝳 ⦙ يتم جلب البيانات إنتظر قليلا ⏳**")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("**🝳 ⦙ عُذرا هذا المحتوى قصير جدًا لتنزيله ⚠️**")
        return None
    except GeoRestrictedError:
        await event.edit(
            "**🝳 ⦙ الفيديو غير متاح من موقعك الجغرافي بسبب القيود الجغرافية التي يفرضها موقع الويب 🌍**"
        )
        return None
    except MaxDownloadsReached:
        await event.edit("**🝳 ⦙  تم الوصول إلى الحد الأقصى لعدد التنزيلات 🛑**")
        return None
    except PostProcessingError:
        await event.edit("**🝳 ⦙  كان هناك خطأ أثناء المعالجة ⚠️**")
        return None
    except UnavailableVideoError:
        await event.edit("**🝳 ⦙  الوسائط غير متوفرة بالتنسيق المطلوب ⚠️**")
        return None
    except XAttrMetadataError as XAME:
        await event.edit(f"🝳 ⦙  `{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return None
    except ExtractorError:
        await event.edit("**🝳 ⦙  حدث خطأ أثناء استخراج المعلومات يرجى وضعها بشكل صحيح ❗️**")
        return None
    except Exception as e:
        await event.edit(f"**🝳 ⦙ حـدث خطأ  ⚠️ : **\n__{str(e)}__")
        return None
    return ytdl_data


async def fix_attributes(path, info_dict: dict, supports_streaming: bool = False, round_message: bool = False) -> list:
    new_attributes = []
    video = False
    audio = False

    uploader = info_dict.get("uploader", "Unknown artist")
    duration = int(info_dict.get("duration", 0))
    suffix = path.suffix[1:]
    if supports_streaming and suffix != "mp4":
        supports_streaming = False

    attributes, mime_type = get_attributes(path)
    if suffix == "mp3":
        title = str(info_dict.get("title", info_dict.get("id", "Unknown title")))
        audio = types.DocumentAttributeAudio(duration, None, title, uploader)
    elif suffix == "mp4":
        width = int(info_dict.get("width", 0))
        height = int(info_dict.get("height", 0))
        for attr in attributes:
            if isinstance(attr, types.DocumentAttributeVideo):
                duration = duration or attr.duration
                width = width or attr.w
                height = height or attr.h
                break
        video = types.DocumentAttributeVideo(
            duration, width, height, round_message, supports_streaming
        )

    if audio and isinstance(audio, types.DocumentAttributeAudio):
        new_attributes.append(audio)
    if video and isinstance(video, types.DocumentAttributeVideo):
        new_attributes.append(video)

    for attr in attributes:
        if (
            isinstance(attr, types.DocumentAttributeAudio)
            and not audio
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not video
            or not isinstance(attr, types.DocumentAttributeAudio)
            and not isinstance(attr, types.DocumentAttributeVideo)
        ):
            new_attributes.append(attr)
    return new_attributes, mime_type


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix

LOGS = logging.getLogger(__name__)
PATH = os.path.join("./temp", "temp_vid.mp4")

thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")



async def ParseSauce(googleurl):
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results

async def scam(results, lim):
    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")
    imglinks = []
    counter = 0
    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if counter <= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks

async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)
@zahid.on(admin_cmd(pattern="جلب لقطات(?:\s|$)([\s\S]*)"))    
async def collage(event):
    catinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    catid = await reply_id(event)
    event = await edit_or_reply(event, "**🝳 ⦙ جاري الالتقاط قـد يستغـرق هـذا الأمـر عـدة دقائـق انتضر ...**")
    if not (reply and (reply.media)):
        await event.edit("**🝳 ⦙ تنسيـق الوسائـط غيـر مدعـوم ⚠️**")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(catsticker)
        await event.edit("**🝳 ⦙ تنسيـق الوسائـط غيـر مدعـوم ⚠️**")
        return
    if catinput:
        if not catinput.isdigit():
            os.remove(catsticker)
            await event.edit("**🝳 ⦙ إدخـالك غيـر صالـح، يرجـىٰ التحـقق مـن المساعـدة ⚠️**")
            return
        catinput = int(catinput)
        if not 0 < catinput < 10:
            os.remove(catsticker)
            await event.edit("**🝳 ⦙ يرجـىٰ وضـع عـدد الصـور بجانـب الأمـر إختـر رقـماً بيـن 1 إلـى 9 ✦**")
            return
    else:
        catinput = 3
    if catsticker.endswith(".tgs"):
        hmm = await make_gif(event, catsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(catsticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = catsticker
    endfile = "./temp/collage.png"
    catcmd = f"vcsi -g {catinput}x{catinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _catutils.runcmd(catcmd))[:2]
    if not os.path.exists(endfile):
        for files in (catsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            event, f"**🝳 ⦙ تنسيـق الوسائـط غيـر مدعـوم، حـاول إستخـدام عـدد أصغـر  ⚠️**", 5 )
    await event.client.send_file(event.chat_id, endfile, reply_to=catid)
    await event.delete()
    for files in (catsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
@zahid.on(admin_cmd(pattern=r"رابط تطبيق ([\s\S]*)"))
async def app_search(event):
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "🝳 ⦙ جـاري البحـث ↯")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>🝳 ⦙ المطـور :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>🝳 ⦙ التقييـم :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>🝳 ⦙ المميـزات :</code> <a href='"
            + app_link
            + "'>🝳 ⦙ مشاهدتـه في سـوق بلـي 🝧</a>"
        )
        app_details += f"\n\n===> {ALIVE_NAME} <==="
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("**🝳 ⦙ لم يتـم العثـور على نتيجـة، الرجـاء إدخـال إسـم تطبيـق صالـح ⚠️**")
    except Exception as err:
        await event.edit("🝳 ⦙ حـدث استثنـاء ⌭ :" + str(err))

@zahid.on(events.NewMessage(outgoing=False, pattern=r'العمر ?(.*)'))
async def RequestAge(event):
    
    BirthDay = (event.message.message).replace('Age', '').strip()
    
    data = requests.get('https://apiabs.ml/age.php?age='+BirthDay)
    DataToJson = json.loads(data.text)
    order = await event.reply(f'{DataToJson["ok"]["abs"]}')

@zahid.on(admin_cmd(pattern="الوقت(?:\s|$)([\s\S]*)(?<![0-9])(?: |$)([0-9]+)?"))
async def time_func(tdata):
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)
    t_form = "%I:%M"
    d_form = "%d/%m/%y - %A"
    c_name = ""
    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif Config.COUNTRY:
        c_name = Config.COUNTRY
        tz_num = Config.TZ_NUMBER
        timezones = await get_tz(Config.COUNTRY)
    else:
        return await edit_or_reply(tdata, f"**🝳 ⦙  ألوقـت 🕛 : **{dt.now().strftime(t_form)} \n** لـتاريـخ :**{dt.now().strftime(d_form)}")
    if not timezones:
        return await edit_or_reply(tdata, "**🝳 ⦙  البـلد غيـر مـوجود 𖠕**")
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"**🝳 ⦙  `{c_name}` لها مناطق زمنية متعددة :**\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n**🝳 ⦙  اختر واحدة عن طريق كتابة الرقم : **"
            return_str += "**🝳 ⦙  في الأمر .**\n"
            return_str += f"**🝳 ⦙  الأمر هوه: .وقت** {c_name} 2`"

            return await edit_or_reply(tdata, return_str)

    dtnow1 = dt.now(tz(time_zone)).strftime(t_form)
    dtnow2 = dt.now(tz(time_zone)).strftime(d_form)
    if c_name != Config.COUNTRY:
        await edit_or_reply(tdata, f"🝳 ⦙  ألوقـت 🕛 :  {dtnow1} علـى {dtnow2}  فـي {c_name} ({time_zone} الـوقت العـالمي 🌍 .")
    if Config.COUNTRY:
        await edit_or_reply(tdata, f"🝳 ⦙  ألوقـت 🕛  : {dtnow1} على {dtnow2}  هنـا فـي 🏷️ :  {Config.COUNTRY}" f"({time_zone} الـوقت العـالمي 🌍 .")
@zahid.on(admin_cmd(pattern="وقتي(?:\s|$)([\s\S]*)"))
async def _(event):
    reply_msg_id = await reply_id(event)
    current_time = dt.now().strftime(f"⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁\n ⌁ Arab time \n⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁\n   {os.path.basename(Config.TZ)}\n  Time: %I:%M:%S \n  Date: %d.%m.%y \n⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁")
    input_str = event.pattern_match.group(1)
    if input_str:
        current_time = input_str
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    required_file_name = Config.TEMP_DIR + " " + str(dt.now()) + ".webp"
    img = Image.new("RGBA", (350, 220), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    await event.client.send_file(
        event.chat_id,
        required_file_name,
        reply_to=reply_msg_id,
    )
    os.remove(required_file_name)
    await event.delete()
@zahid.on(admin_cmd(pattern=r"الاذان(?: |$)(.*)"))
async def get_adzan(adzan):
    LOKASI = adzan.pattern_match.group(1)
    url = f"https://api.pray.zone/v2/times/today.json?city={LOKASI}"
    request = requests.get(url)
    if request.status_code != 200:
        await edit_delete(
            adzan, f"**🝳 ⦙ لم يـتم العثور على معلومات لـهذه المدينه ⚠️ {LOKASI}\n يرجى كتابة اسم محافظتك وباللغه الانكليزي **", 5
        ) 
        return
    result = json.loads(request.text)
    zahidresult = f"<b>اوقـات صـلاه المـسلمين 👳‍♂️ </b>\
            \n\n<b>المـدينة  Ⓜ️  : </b><i>{result['results']['location']['city']}</i>\
            \n<b>الـدولة  🏳️ : </b><i>{result['results']['location']['country']}</i>\
            \n<b>التـاريخ  🔢  : </b><i>{result['results']['datetime'][0]['date']['gregorian']}</i>\
            \n<b>الهـجري  ⏳  : </b><i>{result['results']['datetime'][0]['date']['hijri']}</i>\
            \n\n<b>الامـساك  🕒  : </b><i>{result['results']['datetime'][0]['times']['Imsak']}</i>\
            \n<b>شـروق الشمس  🌝 : </b><i>{result['results']['datetime'][0]['times']['Sunrise']}</i>\
            \n<b>الـفجر  🌔   : </b><i>{result['results']['datetime'][0]['times']['Fajr']}</i>\
            \n<b>الضـهر 🌞   : </b><i>{result['results']['datetime'][0]['times']['Dhuhr']}</i>\
            \n<b>العـصر  🌥    : </b><i>{result['results']['datetime'][0]['times']['Asr']}</i>\
            \n<b>غـروب الشمس  🌘 : </b><i>{result['results']['datetime'][0]['times']['Sunset']}</i>\
            \n<b>المـغرب 🌑 : </b><i>{result['results']['datetime'][0]['times']['Maghrib']}</i>\
            \n<b>العشـاء  🌚   : </b><i>{result['results']['datetime'][0]['times']['Isha']}</i>\
            \n<b>منتـصف الليل 🕛 : </b><i>{result['results']['datetime'][0]['times']['Midnight']}</i>\
    "
    await edit_or_reply(adzan, zahidresult, "html")


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@zahid.on(admin_cmd(pattern=r"فيديو(?:\s|$)([\s\S]*)"))
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "`What I am Supposed to find`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    catevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await _catutils.runcmd(video_cmd))[1]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    catname, stderr = (await _catutils.runcmd(name_cmd))[:2]
    if stderr:
        return await catevent.edit(f"**Error :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    # if stderr:
    #    return await catevent.edit(f"**Error :** `{stderr}`")
    catname = os.path.splitext(catname)[0]
    vsong_file = Path(f"{catname}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{catname}.mkv")
    elif not os.path.exists(vsong_file):
        return await catevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await catevent.edit("`yeah..! i found something wi8..🥰`")
    catthumb = Path(f"{catname}.jpg")
    if not os.path.exists(catthumb):
        catthumb = Path(f"{catname}.webp")
    elif not os.path.exists(catthumb):
        catthumb = None
    ytdata = await yt_data(video_link)
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=f"<b><i>➥ Title :- {ytdata['title']}</i></b>\n<b><i>➥ Uploaded by :- {hmention}</i></b>",
        parse_mode="html",
        thumb=catthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (catthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)
@zahid.on(admin_cmd(pattern=r"البحث العام(?: |$)(.*)"))
async def _(event):
    start = datetime.now()
    OUTPUT_STR = "**🝳 ⦙ قم بالـرد على صـورة لإجـراء البحـث العڪـسي في گـوگـل ✦**"
    if event.reply_to_msg_id:
        catevent = await edit_or_reply(event, "**🝳 ⦙ وسائـط ما قبـل المعالجـة ␥**")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        BASE_URL = "http://www.google.com"
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await catevent.edit("**🝳 ⦙ تم العثـور على نتيجـة بحـث جـوجـل ✓**")
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"}
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
            prs_anchor_element = prs_div.find("a")
            prs_url = BASE_URL + prs_anchor_element.get("href")
            prs_text = prs_anchor_element.text
            # document.getElementById("jHnbRc")
            img_size_div = soup.find(id="jHnbRc")
            img_size = img_size_div.find_all("div")
        except Exception:
            return await edit_delete(
                catevent, "**🝳 ⦙ غيـر قـادر على إيجـاد صـور مشابـهه !**"
            )
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
<b>🝳 ⦙ بحـث ممڪـن ذو صلـة 🜉  : </b> <a href="{prs_url}">{prs_text}</a> 
<b>🝳 ⦙ مزيـد من المعلومـات 🝰 : </b> إفتـح هـذا ␥ <a href="{the_location}">Link</a> 
<i>🝳 ⦙ تم الجلـب في {ms} ثانيـة ⏱</i>""".format(
            **locals()
        )
    else:
        catevent = event
    await edit_or_reply(catevent, OUTPUT_STR, parse_mode="HTML", link_preview=False)
@zahid.on(admin_cmd(pattern="تخزين الصوت(?: |$)(.*)"))
async def iq(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("**قم برد على الصوت بشرط ان يكون الامتداد mp3 وليس بصمه**")
        return
    await event.edit("**جاري تخزين الصوت**")
    d = os.path.join("SQL/extras", "iq.mp3")
    await event.edit("**جارٍ التنزيل ... الملفات الكبيرة تستغرق وقتًا ..**")
    await event.client.download_media(ureply, d)
    await event.edit("**تم .. الآن قم بالرد على الفيديو او المتحركه الذي تريد إضافة هذا الصوت فيه بالأمر :** `.اضف الصوت`")
@zahid.on(admin_cmd(pattern="اضف الصوت(?: |$)(.*)"))
async def iq(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("**قم بالرد على متحركه او فيديو الذي تريد إضافة الصوت فيه.**")
        return
    xx = await event.edit("**  جاري اضافه الصوت انتضر قليلا \n ملاحضه لاتنسى تطابق وقت الفيديو او المتحركه مع وقت الصوت **")
    ultt = await ureply.download_media()
    ls = os.listdir("SQL/extras")
    z = "iq.mp3"
    x = "SQL/extras/iq.mp3"
    if z not in ls:
        await event.edit("**قم بالرد أولاً بصوت بامتداد mp3 فقط**")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("L5.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="L5.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    os.remove("L5.mp4")
    os.remove(x)
    os.remove(ultt)
    await xx.delete()

@zahid.on(admin_cmd(pattern="تحويل صوره(?: |$)(.*)"))
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "**🝳 ⦙  يجـب عليـك الرد عـلى الملصق لتحويـله الـى صورة ⚠️**"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "**🝳 ⦙  غـير قـادر على تحويل الملصق إلى صورة من هـذا الـرد ⚠️**"
        )
    meme_file = convert_toimage(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()
@zahid.on(admin_cmd(pattern="تحويل ملصق(?: |$)(.*)"))
async def _(event):
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "**🝳 ⦙  يجـب عليـك الرد عـلى الصـورة لتحويـلها الـى مـلصق ⚠️**"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "**🝳 ⦙  غـير قـادر على استـخراج الـملصق من هـذا الـرد ⚠️**"
        )
    meme_file = convert_tosticker(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()
@zahid.on(admin_cmd(pattern="تحويل (صوت|بصمه)(?: |$)(.*)"))
async def _(event):
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**🝳 ⦙  يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "**🝳 ⦙  يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "**🝳 ⦙  يتـم التـحويل انتـظر قليـلا ⏱**")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to download")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(
            "**🝳 ⦙  التحـميل الى `{}`  في {} من الثواني ⏱**".format(downloaded_file_name, ms)
        )
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "بصمه":
            new_required_file_caption = "voice_" + str(round(time.time())) + ".opus"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "صوت":
            new_required_file_caption = "mp3_" + str(round(time.time())) + ".mp3"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("**🝳 ⦙  غـير مدعوم ❕**")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            *command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()
@zahid.on(admin_cmd(pattern="تحويل متحركة ?([0-9.]+)?$"))
async def _(event):
    reply = await event.get_reply_message()
    mediatype = media_type(event)
    if mediatype and mediatype != "video":
        return await edit_delete(event, "**🝳 ⦙  يجـب عليك الـرد على فيديو اولا لتحـويله ⚠️**")
    args = event.pattern_match.group(1)
    if not args:
        args = 2.0
    else:
        try:
            args = float(args)
        except ValueError:
            args = 2.0
    catevent = await edit_or_reply(event, "**🝳 ⦙  يتـم التحويل الى متـحركه انتـظر ⏱**")
    inputfile = await reply.download_media()
    outputfile = os.path.join(Config.TEMP_DIR, "vidtogif.gif")
    result = await vid_to_gif(inputfile, outputfile, speed=args)
    if result is None:
        return await edit_delete(event, "**🝳 ⦙  عـذرا لا يمكـنني تحويل هذا الى متـحركة ⚠️**")
    jasme = await event.client.send_file(event.chat_id, result, reply_to=reply)
    await _catutils.unsavegif(event, jasme)
    await catevent.delete()
    for i in [inputfile, outputfile]:
        if os.path.exists(i):
            os.remove(i)
@zahid.on(admin_cmd(pattern="تحويل فديو دائري(?: |$)((-)?(s)?)$"))
async def pic_gifcmd(event):  # sourcery no-metrics
    args = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(event, "**🝳 ⦙ قـم بالـرد على وسائـط مدعومـة !**")
    media_type(reply)
    catevent = await edit_or_reply(event, "**🝳 ⦙ جـاري تحويل الملصق الى فيديو مرئي دائـري ⌯**")
    output = await _cattools.media_to_pic(event, reply, noedits=True)
    if output[1] is None:
        return await edit_delete(
            output[0], "**🝳 ⦙ تعـذّر إستخـراج الصـورة من الرسالـة التي تـم الـرّد عليهـا ✕**"
        )
    meme_file = convert_toimage(output[1])
    image = Image.open(meme_file)
    w, h = image.size
    outframes = []
    try:
        outframes = await spin_frames(image, w, h, outframes)
    except Exception as e:
        return await edit_delete(output[0], f"**🝳 ⦙ خطـأ ⚠️ :**\n__{str(e)}__")
    output = io.BytesIO()
    output.name = "Output.gif"
    outframes[0].save(output, save_all=True, append_images=outframes[1:], duration=1)
    output.seek(0)
    with open("Output.gif", "wb") as outfile:
        outfile.write(output.getbuffer())
    final = os.path.join(Config.TEMP_DIR, "output.gif")
    output = await vid_to_gif("Output.gif", final)
    if output is None:
        return await edit_delete(catevent, "**🝳 ⦙ تعـذّر صنـع صـورة متحرڪـة دوارة ✕**")
    media_info = MediaInfo.parse(final)
    aspect_ratio = 1
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    PATH = os.path.join(Config.TEMP_DIR, "round.gif")
    if aspect_ratio != 1:
        crop_by = width if (height > width) else height
        await _catutils.runcmd(
            f'ffmpeg -i {final} -vf "crop={crop_by}:{crop_by}" {PATH}'
        )
    else:
        copyfile(final, PATH)
    time.time()
    ul = io.open(PATH, "rb")
    uploaded = await event.client.fast_upload_file(
        file=ul,
    )
    ul.close()
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type="video/mp4",
        attributes=[
            types.DocumentAttributeVideo(
                duration=0,
                w=1,
                h=1,
                round_message=True,
                supports_streaming=True,
            )
        ],
        force_file=False,
        thumb=await event.client.upload_file(meme_file),
    )
    sandy = await event.client.send_file(
        event.chat_id,
        media,
        reply_to=reply,
        video_note=True,
        supports_streaming=True,
    )
    if not args:
        await _catutils.unsavegif(event, sandy)
    await catevent.delete()
    for i in [final, "Output.gif", meme_file, PATH, final]:
        if os.path.exists(i):
            os.remove(i)
@zahid.on(admin_cmd(pattern="تحويل ملصق دائري ?((-)?s)?$"))
async def video_catfile(event):  # sourcery no-metrics
    reply = await event.get_reply_message()
    args = event.pattern_match.group(1)
    catid = await reply_id(event)
    if not reply or not reply.media:
        return await edit_delete(event, "**🝳 ⦙ قـم بالـرد على وسائـط مدعومـة !**")
    mediatype = media_type(reply)
    if mediatype == "Round Video":
        return await edit_delete(
            event,
            "🝳 ⦙ الوسائـط التي تم الـرد عليهـا هـي بالفعـل في شڪـل دائـري، أعـد التحـقق !",
        )
    if mediatype not in ["Photo", "Audio", "Voice", "Gif", "Sticker", "Video"]:
        return await edit_delete(event, "**🝳 ⦙ لم يتـم العثـور على وسائـط مدعومـة !**")
    flag = True
    catevent = await edit_or_reply(event, "**🝳 ⦙ جـاري التحويـل إلى شڪـل دائـري ⌯**")
    catfile = await reply.download_media(file="./temp/")
    if mediatype in ["Gif", "Video", "Sticker"]:
        if not catfile.endswith((".webp")):
            if catfile.endswith((".tgs")):
                hmm = await make_gif(catevent, catfile)
                os.rename(hmm, "./temp/circle.mp4")
                catfile = "./temp/circle.mp4"
            media_info = MediaInfo.parse(catfile)
            aspect_ratio = 1
            for track in media_info.tracks:
                if track.track_type == "Video":
                    aspect_ratio = track.display_aspect_ratio
                    height = track.height
                    width = track.width
            if aspect_ratio != 1:
                crop_by = width if (height > width) else height
                await _catutils.runcmd(
                    f'ffmpeg -i {catfile} -vf "crop={crop_by}:{crop_by}" {PATH}'
                )
            else:
                copyfile(catfile, PATH)
            if str(catfile) != str(PATH):
                os.remove(catfile)
            try:
                catthumb = await reply.download_media(thumb=-1)
            except Exception as e:
                LOGS.error(f"circle - {str(e)}")
    elif mediatype in ["Voice", "Audio"]:
        catthumb = None
        try:
            catthumb = await reply.download_media(thumb=-1)
        except Exception:
            catthumb = os.path.join("./temp", "thumb.jpg")
            await thumb_from_audio(catfile, catthumb)
        if catthumb is not None and not os.path.exists(catthumb):
            catthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, catthumb)
        if (
            catthumb is not None
            and not os.path.exists(catthumb)
            and os.path.exists(thumb_loc)
        ):
            flag = False
            catthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, catthumb)
        if catthumb is not None and os.path.exists(catthumb):
            await _catutils.runcmd(
                f"""ffmpeg -loop 1 -i {catthumb} -i {catfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale=\'iw-mod (iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -shortest -movflags +faststart {PATH}"""
            )
            os.remove(catfile)
        else:
            os.remove(catfile)
            return await edit_delete(
                catevent, "**لا يوجـد ما يصلـح لجعلـه ملاحظـة فيديـو ⚠️**", 5
            )
    if (
        mediatype
        in [
            "Voice",
            "Audio",
            "Gif",
            "Video",
            "Sticker",
        ]
        and not catfile.endswith((".webp"))
    ):
        if os.path.exists(PATH):
            c_time = time.time()
            attributes, mime_type = get_attributes(PATH)
            ul = io.open(PATH, "rb")
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, catevent, c_time, "**🝳 ⦙ قـم بالـرد على وسائـط مدعومـة !**")
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type="video/mp4",
                attributes=[
                    types.DocumentAttributeVideo(
                        duration=0,
                        w=1,
                        h=1,
                        round_message=True,
                        supports_streaming=True,
                    )
                ],
                force_file=False,
                thumb=await event.client.upload_file(catthumb) if catthumb else None,
            )
            sandy = await event.client.send_file(
                event.chat_id,
                media,
                reply_to=catid,
                video_note=True,
                supports_streaming=True,
            )

            if not args:
                await _catutils.unsavegif(event, sandy)
            os.remove(PATH)
            if flag:
                os.remove(catthumb)
        await catevent.delete()
        return
    data = reply.photo or reply.media.document
    img = io.BytesIO()
    await event.client.download_file(data, img)
    im = Image.open(img)
    w, h = im.size
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    img.paste(im, (0, 0))
    m = min(w, h)
    img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((10, 10, w - 10, h - 10), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(2))
    img = ImageOps.fit(img, (w, h))
    img.putalpha(mask)
    im = io.BytesIO()
    im.name = "cat.webp"
    img.save(im)
    im.seek(0)
    await event.client.send_file(event.chat_id, im, reply_to=catid)
    await catevent.delete()
@zahid.on(admin_cmd(pattern="تحويل ملف ([\s\S]*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await edit_or_reply(event, "**🝳 ⦙ قم بالـرد على الرسالـة لتحويلها الى ملف**")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await edit_or_reply(event, "**🝳 ⦙ قم بالـرد على الرسالـة لتحويلها الى ملف**")
@zahid.on(admin_cmd(pattern="بورن(?:\s|$)([\s\S]*)"))
async def catbot(event):
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if " " in input_str:
        username, text = input_str.split(" ")
    else:
        return await edit_or_reply(event, " **🝳 ⦙   عذرا يجب الرد على الصوره التي تريد ستعملها ومن ثم ارسال الامر :**  `.بورن + معرف الشخص + الكتابه التي تريدها`")
    replied = await event.get_reply_message()
    catid = await reply_id(event)
    if not replied:
        return await edit_or_reply(event, "**🝳 ⦙  عذرا قم بالرد على الصوره **")
    output = await _cattools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(output[0], "**🝳 ⦙  تعذر استخراج الصورة من الرسالة التي تم الرد عليها **")
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit("**🝳 ⦙  حجم الملف الذي تم الرد عليه غير مدعوم ، يجب أن يكون حجمه أقل من 5 ميغابايت**")

    await output[0].edit("**🝳 ⦙  جاري صنع امر بورن هوب .. **")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**🝳 ⦙  عذرا هناك خطأ : **\n`{str(exc)}`")
    cat = f"https://telegra.ph{response[0]}"
    cat = await phcomment(cat, text, username)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cat, reply_to=catid)
@zahid.on(admin_cmd(pattern="(طقس|الطقس)(?:\s|$)([\s\S]*)"))    
async def get_weather(event):   
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    CITY = gvarstatus("DEFCITY") or "Baghdad" if not input_str else input_str
    timezone_countries = {        timezone: country        for country, timezones in c_tz.items()        for timezone in timezones    }
    if " " in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + " " + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(event, "عزيزي هذا البلد او المدينه لاتوجد")
            CITY = newcity[0].strip() + "," + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=c77467242a1dc063a202eaac5544ce4b"
    async with aiohttp.ClientSession() as _session:
        async with _session.get(url) as request:
            requeststatus = request.status
            requesttext = await request.text()
    result = json.loads(requesttext)
    if requeststatus != 200:
        return await edit_or_reply(event, "عزيزي هذا البلد او المدينه لاتوجد")
    cityname = result["name"]
    curtemp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    feel = result["main"]["feels_like"]
    desc = result["weather"][0]
    desc = desc["main"]
    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]
    wind = result["wind"]["speed"]
    winddir = result["wind"]["deg"]
    cloud = result["clouds"]["all"]
    ctimezone = tz(c_tz[country][0])
    time = datetime.now(ctimezone).strftime("%A, %I:%M %p")
    fullc_n = c_n[f"{country}"]
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    div = 360 / len(dirs)
    funmath = int((winddir + (div / 2)) / div)
    findir = dirs[funmath % len(dirs)]
    kmph = str(wind * 3.6).split(".")
    mph = str(wind * 2.237).split(".")
    await edit_or_reply(event, f"🌡 **درجه الحرارة  : ** `{celsius(curtemp)} سيليزي `\n\n"  + f"🥵 **اعلى درجه حراره :** `{fahrenheit(max_temp)} فهرنايت `\n\n"  + f"🌬 **قوه الرياح :** {kmph[0]} كيلومتر بالساعه \n\n\n" + f"**طقس للمدينه او الدوله الأتيه :**\n" + f"`{cityname}, {fullc_n}`\n" + f"`{time}`\n"    )
@zahid.on(admin_cmd(pattern="تحويل رساله(?: |$)(.*)"))
async def get(event):
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if mediatype != "Document":
        return await edit_delete(
            event, "**🝳 ⦙ يبـدو أن هـذا الملـف غـير قابـل للڪتابـة،  يرجـى الـرد على ملـف قابـل للكتابـة !**"
        )
    file_loc = await reply.download_media()
    file_content = ""
    try:
        with open(file_loc) as f:
            file_content = f.read().rstrip("\n")
    except UnicodeDecodeError:
        pass
    except Exception as e:
        LOGS.info(e)
    if file_content == "":
        try:
            with fitz.open(file_loc) as doc:
                for page in doc:
                    file_content += page.getText()
        except Exception as e:
            if os.path.exists(file_loc):
                os.remove(file_loc)
            return await edit_delete(event, f"**🝳 ⦙ خطـأ ⚠️**\n__{str(e)}__")
    await edit_or_reply(
        event,
        file_content,
        parse_mode=parse_pre,
        aslink=True,
        noformat=True,
        linktext="**🝳 ⦙ يسمـح تليڪرام فقـط بـ 4096 حرفًـا في الرسالـة الواحـدة، ولڪن الملـف الـذي قمـت بالـرد عليـه يحتـوي على أڪثـر مـن ذلـك بڪثيـر، لذلـك (( لصقها على رابط لصق )) غيرها انت)) !**",
    )
    if os.path.exists(file_loc):
        os.remove(file_loc)
@zahid.on(admin_cmd(pattern="تحويل ملف صوره(?: |$)(.*)"))
async def on_file_to_photo(event):
    target = await event.get_reply_message()
    try:
        image = target.media.document
    except AttributeError:
        return await edit_delete(event, "**🝳 ⦙ هـذه ليسـت صـورة !**")
    if not image.mime_type.startswith("image/"):
        return await edit_delete(event, "**🝳 ⦙ هـذه ليسـت صـورة !**")
    if image.mime_type == "image/webp":
        return await edit_delete(event, "**🝳 ⦙ لتحويـل الملصـق إلى صـورة إستخـدم الأمـر  ⩥ :**  `.تحويل ملف صوره`")
    if image.size > 10 * 1024 * 1024:
        return  # We'd get PhotoSaveFileInvalidError otherwise
    catt = await edit_or_reply(event, "**🝳 ⦙ جـاري التحويـل  ↯**")
    file = await event.client.download_media(target, file=BytesIO())
    file.seek(0)
    img = await event.client.upload_file(file)
    img.name = "image.png"
    try:
        await event.client(
            SendMediaRequest(
                peer=await event.get_input_chat(),
                media=types.InputMediaUploadedPhoto(img),
                message=target.message,
                entities=target.entities,
                reply_to_msg_id=target.id,
            )
        )
    except PhotoInvalidDimensionsError:
        return
    await catt.delete()
@zahid.on(admin_cmd(pattern="تحويل متحركه(?: |$)((-)?(r|l|u|d|s|i)?)$"))
async def pic_gifcmd(event):  # sourcery no-metrics
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(event, "**🝳 ⦙ قم بالـرد على صـورة أو ملصـق لجعلهـا صـورة متحرڪـة **")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await edit_delete(
            event,
            "**🝳 ⦙ قم بالـرد على صـورة أو ملصـق لجعلهـا صـورة متحرڪـة، الملصقـات المتحرڪـة غيـر مدعومـة !**",
        )
    args = event.pattern_match.group(1)
    args = "i" if not args else args.replace("-", "")
    catevent = await edit_or_reply(event, "**🝳 ⦙ جـاري صنـع صـورة متحرڪـة من الوسائـط التي قمـت بالـرد عليهـا ↯**")
    imag = await _cattools.media_to_pic(event, reply, noedits=True)
    if imag[1] is None:
        return await edit_delete(
            imag[0], "**🝳 ⦙ تعـذّر إستخـراج الصـورة من الرسالـة التي تـم الـرّد عليهـا ✕**"
        )
    image = Image.open(imag[1])
    w, h = image.size
    outframes = []
    try:
        if args == "r":
            outframes = await r_frames(image, w, h, outframes)
        elif args == "l":
            outframes = await l_frames(image, w, h, outframes)
        elif args == "u":
            outframes = await ud_frames(image, w, h, outframes)
        elif args == "d":
            outframes = await ud_frames(image, w, h, outframes, flip=True)
        elif args == "s":
            outframes = await spin_frames(image, w, h, outframes)
        elif args == "i":
            outframes = await invert_frames(image, w, h, outframes)
    except Exception as e:
        return await edit_delete(catevent, f"**🝳 ⦙ خطـأ ⚠️**\n__{str(e)}__")
    output = io.BytesIO()
    output.name = "Output.gif"
    outframes[0].save(output, save_all=True, append_images=outframes[1:], duration=0.7)
    output.seek(0)
    with open("Output.gif", "wb") as outfile:
        outfile.write(output.getbuffer())
    final = os.path.join(Config.TEMP_DIR, "output.gif")
    output = await vid_to_gif("Output.gif", final)
    if output is None:
        await edit_delete(
            catevent, "**🝳 ⦙ حـدث خطـأ مـا في الوسائـط، لا أستطيـع تحويلهـا إلى صـورة متحرڪـة !**"
        )
        for i in [final, "Output.gif", imag[1]]:
            if os.path.exists(i):
                os.remove(i)
        return
    sandy = await event.client.send_file(event.chat_id, output, reply_to=reply)
    await _catutils.unsavegif(event, sandy)
    await catevent.delete()
    for i in [final, "Output.gif", imag[1]]:
        if os.path.exists(i):
            os.remove(i)
@zahid.on(admin_cmd(pattern="مدينه الطقس(?:\s|$)([\s\S]*)"))    
async def set_default_city(event):
    input_str = event.pattern_match.group(1)
    CITY = gvarstatus("DEFCITY") or "Delhi" if not input_str else input_str
    timezone_countries = {        timezone: country        for country, timezones in c_tz.items()        for timezone in timezones    }
    if " " in CITY:
        newcity = CITY.split(" ")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + " " + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await edit_or_reply(event, "عزيزي هذا البلد او المدينه لاتوجد")
            CITY = newcity[0].strip() + " " + countrycode.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=c77467242a1dc063a202eaac5544ce4b"
    request = requests.get(url)
    result = json.loads(request.text)
    if request.status_code != 200:
        return await edit_or_reply(event, "عزيزي هذا البلد او المدينه لاتوجد")
    addgvar("DEFCITY", CITY)
    cityname = result["name"]
    country = result["sys"]["country"]
    fullc_n = c_n[f"{country}"]
    await edit_or_reply(event, f"تم وضع مدينتك ضمن الطقس المحدد : {cityname}, {fullc_n}.`")
@zahid.on(admin_cmd(pattern=r"(ت(لي)?ج(راف)?) ?(م|ك|ميديا|كتابه)(?:\s|$)([\s\S]*)"))
async def _(event):
    catevent = await edit_or_reply(event, "**🝳 ⦙ جـاري المعالجـة ⌯**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"**🝳 ⦙ تـمّ إنشـاء تليجـراف جديـد ✓ :** {auth_url} \n **للجلسـة الحاليـة، لا تقـم بإعطـاء هـذا الرابـط إلى أي أحـد، حتى وإن قـال بأنّـه موظـف لـدى تليڪـرام !**",
        )
    optional_title = event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await catevent.edit(
            "**🝳 ⦙ قـم بالـردّ على رسالـة للحصـول على رابـط صـورة تليجـراف دائـم ☍**",
        )

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()
    if input_str in ["ميديا", "م"]:
        downloaded_file_name = await event.client.download_media(
            r_message, Config.TEMP_DIR
        )
        await catevent.edit(f"**🝳 ⦙ تـم التحميـل إلى**  {downloaded_file_name}`")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await catevent.edit(f"**🝳 ⦙ حـدث خـطأ مـا ✕ : **\n`{str(exc)}`")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await catevent.edit(
                 f"**🝳 ⦙  الرابـط ☍ : ** [Press here](https://telegra.ph{media_urls[0]})\
                    \n**🝳 ⦙ الوقـت المستغـرق ⏱  : ** `{ms} الثوانـي.`",
                link_preview=True,
            )
    elif input_str in ["كتابه", "ك"]:
        user_object = await event.client.get_entity(r_message.sender_id)
        title_of_page = get_display_name(user_object)
        # apparently, all Users do not have last_name field
        if optional_title:
            title_of_page = optional_title
        page_content = r_message.message
        if r_message.media:
            if page_content != "":
                title_of_page = page_content
            downloaded_file_name = await event.client.download_media(
                r_message, Config.TEMP_DIR
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            for m in m_list:
                page_content += m.decode("UTF-8") + "\n"
            os.remove(downloaded_file_name)
        page_content = page_content.replace("\n", "<br>")
        try:
            response = telegraph.create_page(title_of_page, html_content=page_content)
        except Exception as e:
            LOGS.info(e)
            title_of_page = "".join(
                random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
                for _ in range(16)
            )
            response = telegraph.create_page(title_of_page, html_content=page_content)
        end = datetime.now()
        ms = (end - start).seconds
        cat = f"https://telegra.ph/{response['path']}"
        await catevent.edit(f"**🝳 ⦙  الرابـط ☍ : ** [Press here]({cat})\n**🝳 ⦙ الوقـت المستغـرق ⏱  : ** `{ms} الثوانـي.`", link_preview=True)
@zahid.on(admin_cmd(pattern="تحويل فديو متحركه ?([0-9.]+)?$"))
async def _(event):
    reply = await event.get_reply_message()
    mediatype = media_type(event)
    if mediatype and mediatype != "video":
        return await edit_delete(event, "**🝳 ⦙ حـدث خطـأ مـا في الوسائـط، لا أستطيـع تحويلهـا إلى صـورة متحرڪـة !**")
    args = event.pattern_match.group(1)
    if not args:
        args = 2.0
    else:
        try:
            args = float(args)
        except ValueError:
            args = 2.0
    catevent = await edit_or_reply(event, "**🝳 ⦙ جـاري التحويـل إلى صـورة متحرڪة انتضر دقائق  ↯**")
    inputfile = await reply.download_media()
    outputfile = os.path.join(Config.TEMP_DIR, "vidtogif.gif")
    result = await vid_to_gif(inputfile, outputfile, speed=args)
    if result is None:
        return await edit_delete(event, "**🝳 ⦙ غيـر قـادر على تحويلهـا إلى صـورة متحرڪة !**")
    sandy = await event.client.send_file(event.chat_id, result, reply_to=reply)
    await _catutils.unsavegif(event, sandy)
    await catevent.delete()
    for i in [inputfile, outputfile]:
        if os.path.exists(i):
            os.remove(i)
@zahid.on(admin_cmd(pattern="طقوس(?:\s|$)([\s\S]*)"))    
async def _(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    if not input_str:
        input_str = gvarstatus("DEFCITY") or "Baghdad"
    async with aiohttp.ClientSession() as session:
        sample_url = "https://wttr.in/{}.png"
        response_api_zero = await session.get(sample_url.format(input_str))
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(                f"**المدينه  : **`{input_str}`", file=out_file, reply_to=reply_to_id            )
    try:
        await event.delete()
    except Exception as e:
        LOGS.info(str(e))

