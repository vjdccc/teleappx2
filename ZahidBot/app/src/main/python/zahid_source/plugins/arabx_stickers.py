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
try:
    import io
except Exception:
    io = _Missing('io')
try:
    import math
except Exception:
    math = _Missing('math')
try:
    import random
except Exception:
    random = _Missing('random')
try:
    import re
except Exception:
    re = _Missing('re')
try:
    import string
except Exception:
    string = _Missing('string')
try:
    import urllib.request
except Exception:
    urllib = _Missing('urllib')
try:
    from os import remove
except Exception:
    remove = _Missing('remove')
try:
    import cloudscraper
except Exception:
    cloudscraper = _Missing('cloudscraper')
try:
    import emoji as catemoji
except Exception:
    catemoji = _Missing('catemoji')
try:
    from bs4 import BeautifulSoup as bs
except Exception:
    bs = _Missing('bs')
try:
    from PIL import Image
except Exception:
    Image = _Missing('Image')
combot_stickers_url = "https://combot.org/telegram/stickers?q="
EMOJI_SEN = [    "يمكنك إدراج عدة رموز تعبيرية في رسالة واحدة ، ولكني أوصي باستخدام ما لا يزيد عن اثنين لكل ملصق" ,]
KANGING_STR = [    "جيد ملصق جميل " ]
def verify_cond(catarray, text):
    return any(i in text for i in catarray)
def pack_name(userid, pack, is_anim):
    if is_anim:
        return f"zahidbot_{userid}_{pack}_anim"
    return f"zahidbot_{userid}_{pack}"
def char_is_emoji(character):
    return character in catemoji.UNICODE_EMOJI["en"]
def pack_nick(username, pack, is_anim):
    if gvarstatus("CUSTOM_STICKER_PACKNAME"):
        if is_anim:
            packnick = f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} Vol.{pack} (Animated)"
        else:
            packnick = f"{gvarstatus('CUSTOM_STICKER_PACKNAME')} Vol.{pack}"
    elif is_anim:
        packnick = f"@{username} Vol.{pack} (Animated)"
    else:
        packnick = f"@{username} Vol.{pack}"
    return packnick
async def resize_photo(photo):
    image = Image.open(photo)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        maxsize = (512, 512)
        image.thumbnail(maxsize)
    return image
async def newpacksticker(    catevent,    conv,    cmd,    args,    pack,    packnick,    stfile,    emoji,    packname,    is_anim,    otherpack=False,    pkang=False):
    await conv.send_message(cmd)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packnick)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.text):
        await catevent.edit(            f"فشلت إضافة الملصق ، استخدم @Stickers بوت لإضافة الملصق يدويًا .\n** خطأ :**{rsp}"        )
        return
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/publish")
    if is_anim:
        await conv.get_response()
        await conv.send_message(f"<{packnick}>")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("/skip")
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message(packname)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return otherpack, packname, emoji
    return pack, packname
async def add_to_pack(    catevent,    conv,    args,    packname,    pack,    userid,    username,    is_anim,    stfile,    emoji,    cmd,    pkang=False ):
    await conv.send_message("/addsticker")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    x = await conv.get_response()
    while ("50" in x.text) or ("120" in x.text):
        try:
            val = int(pack)
            pack = val + 1
        except ValueError:
            pack = 1
        packname = pack_name(userid, pack, is_anim)
        packnick = pack_nick(username, pack, is_anim)
        await catevent.edit(            f"**- التحول إلى حزمة {str(pack)} بسبب مساحة غير كافية **"        )
        await conv.send_message(packname)
        x = await conv.get_response()
        if x.text == "Invalid pack selected.":
            return await newpacksticker(                catevent,                conv,                cmd,                args,                pack,                packnick,                stfile,                emoji,                packname,                is_anim,                otherpack=True,                pkang=pkang            )
    if is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.text):
        await catevent.edit(            f"فشلت إضافة الملصق ، استخدم @Stickers بوت لإضافة الملصق يدويًا .\n** خطأ :**{rsp}"        )
        return
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/done")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return packname, emoji
    return pack, packname
@zahid.on(admin_cmd(pattern="صنع ملصق(?:\s|$)([\s\S]*)"))    
async def kang(args):  
    photo = None
    emojibypass = False
    is_anim = False
    emoji = None
    message = await args.get_reply_message()
    user = await args.client.get_me()
    if not user.username:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"zahid_{user.id}"
    else:
        username = user.username
    userid = user.id
    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            photo = await args.client.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            await args.client.download_file(message.media.document, photo)
            if (                DocumentAttributeFilename(file_name="sticker.webp")                in message.media.document.attributes            ):
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            catevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            await args.client.download_file(                message.media.document, "AnimatedSticker.tgs"            )

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await edit_delete(args, "** ملف غير مدعوم ! **")
            return
    else:
        await edit_delete(args, "** لا أستطيع أن كان ذلك ... **")
        return
    if photo:
        splat = ("".join(args.text.split(maxsplit=1)[1:])).split()
        emoji = emoji if emojibypass else "😂"
        pack = 1
        if len(splat) == 2:
            if char_is_emoji(splat[0][0]):
                if char_is_emoji(splat[1][0]):
                    return await catevent.edit("تأكد من قائمه الاوامر أرسل : `.الاوامر`")
                pack = splat[1]  # User sent both
                emoji = splat[0]
            elif char_is_emoji(splat[1][0]):
                pack = splat[0]  # User sent both
                emoji = splat[1]
            else:
                return await catevent.edit("تأكد من قائمه الاوامر أرسل : `.الاوامر`")
        elif len(splat) == 1:
            if char_is_emoji(splat[0][0]):
                emoji = splat[0]
            else:
                pack = splat[0]
        packnick = pack_nick(username, pack, is_anim)
        packname = pack_name(userid, pack, is_anim)
        cmd = "/newpack"
        stfile = io.BytesIO()
        if is_anim:
            cmd = "/newanimated"
        else:
            image = await resize_photo(photo)
            stfile.name = "sticker.png"
            image.save(stfile, "PNG")
        response = urllib.request.urlopen(            urllib.request.Request(f"http://t.me/addstickers/{packname}")        )
        htmlstr = response.read().decode("utf8").split("\n")
        if ("  A <strong>Telegram</strong> قام المستخدم بإنشاء <strong>Sticker&nbsp;Set</strong>." not in htmlstr ):
            async with args.client.conversation("Stickers") as conv:
                packname, emoji = await add_to_pack(                    catevent,                    conv,                    args,                    packname,                    pack,                    userid,                    username,                    is_anim,                    stfile,                    emoji,                    cmd                 )
            await edit_delete(catevent, f"** إنشاء ملصق بنجاح ! ** : [ملصقك هنا](t.me/addstickers/{packname}) ", parse_mode="md",  time=10 )
        else:
            await catevent.edit("** جاري انشاء حافضه جديده ... **")
            async with args.client.conversation("Stickers") as conv:
                otherpack, packname, emoji = await newpacksticker(                    catevent,                    conv,                    cmd,                    args,                    pack,                    packnick,                    stfile,                    emoji,                    packname,                    is_anim,                )
            if otherpack:
                await edit_delete(                    catevent,                    f"ملصق لحزمة مختلفة ! \n والحزمة التي تم إنشاؤها حديثًا هي : [ملصقك هنا](t.me/addstickers/{packname}) ",                    parse_mode="md",                    time=10   )
            else:
                await edit_delete(                    catevent,                    f"إنشاء ملصق بنجاح !  \n الحزمه هيه :  [ هنا](t.me/addstickers/{packname}) ",                    parse_mode="md",                    time=10   )
@zahid.on(admin_cmd(pattern="انشاء حزمه ملصقات(?:\s|$)([\s\S]*)"))   
async def pic2packcmd(event):
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await edit_delete(event, " الرد على الصورة أو الملصق لعمل حزمة ")
    if mediatype == "Sticker" and reply.document.mime_type == "application/x-tgsticker":
        return await edit_delete(            event,            "الرد على الصورة أو الملصق لعمل حزمة. الملصق المتحرك غير مدعوم",        )
    args = event.pattern_match.group(1)
    if not args:
        return await edit_delete(            event, "قم باضافه اسم الحزمه"        )
    catevent = await edit_or_reply(event, "... جاري قص وتعديل الصورة ")
    try:
        emoji = (re.findall(r"-e[\U00010000-\U0010ffff]+", args))[0]
        args = args.replace(emoji, "")
        emoji = emoji.replace("-e", "")
    except Exception:
        emoji = "▫️"
    chat = "@Stickers"
    name = "zahidbot_" + "".join(        random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
        for _ in range(16)    )
    image = await _cattools.media_to_pic(catevent, reply, noedits=True)
    if image[1] is None:
        return await edit_delete(            image[0], "تعذر استخراج الصورة من الرسالة التي تم الرد عليها"        )
    image = Image.open(image[1])
    w, h = image.size
    www = max(w, h)
    img = Image.new("RGBA", (www, www), (0, 0, 0, 0))
    img.paste(image, ((www - w) // 2, 0))
    newimg = img.resize((100, 100))
    new_img = io.BytesIO()
    new_img.name = name + ".png"
    images = await crop_and_divide(img)
    newimg.save(new_img)
    new_img.seek(0)
    catevent = await event.edit("جاري صنع الحزمه ")
    async with event.client.conversation(chat) as conv:
        i = 0
        try:
            await event.client.send_message(chat, "/cancel")
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_message(chat, "/newpack")
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_message(chat, args)
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            for im in images:
                img = io.BytesIO(im)
                img.name = name + ".png"
                img.seek(0)
                await event.client.send_file(chat, img, force_document=True)
                await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
                await event.client.send_message(chat, emoji)
                await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
                await event.client.send_read_acknowledge(conv.chat_id)
                await asyncio.sleep(1)
                i += 1
                await catevent.edit(                    f"صنع الحزمه \nتقدم : {i}/{len(images)}__"                )
            await event.client.send_message(chat, "/publish")
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_file(chat, new_img, force_document=True)
            await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.send_message(chat, name)
            ending = await conv.wait_event(                events.NewMessage(incoming=True, from_users=chat)            )
            await event.client.send_read_acknowledge(conv.chat_id)
            for packname in ending.raw_text.split():
                if packname.startswith("https://t.me/"):
                    break
            await catevent.edit(                f"نجح في إنشاء حزمة الوسائط التي تم الرد عليها : [{args}]({packname})"            )

        except YouBlockedUserError:
            await catevent.edit(                "قم بارسال رساله الى : @Stickers "            )
@zahid.on(admin_cmd(pattern="ملصق ?([\s\S]*)"))    
async def cb_sticker(event):
    split = event.pattern_match.group(1)
    if not split:
        return await edit_delete(event, "أدخل اسمًا للبحث عن الحزمة", 5)
    catevent = await edit_or_reply(event, "البحث في حزم الملصقات ....")
    scraper = cloudscraper.create_scraper()
    text = scraper.get(combot_stickers_url + split).text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await edit_delete(catevent, "`No results found :(.`", 5)
    reply = f"**تم العثور على حزم ملصقات لـ {split}  :**"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            packid = (pack.button).get("data-popup")
            reply += f"\n **• الايدي : **`{packid}`\n [{packtitle}]({packlink})"
    await catevent.edit(reply)

