# -*- coding: utf-8 -*-
# مُحوَّل آلياً من اوامر Telethon Zahid (Telethon) الى Pyrogram عبر arabcompat
import warnings; warnings.filterwarnings("ignore")
from arabcompat import *
from arabcompat import _Missing, _format, _catutils, _cattools, _LazyTelegraph
try:
    import random
except Exception:
    random = _Missing('random')
try:
    import re
except Exception:
    re = _Missing('re')
try:
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')
try:
    import asyncio
except Exception:
    asyncio = _Missing('asyncio')
try:
    import pyfiglet
except Exception:
    pyfiglet = _Missing('pyfiglet')
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
    from collections import deque
except Exception:
    deque = _Missing('deque')
try:
    from random import choice
except Exception:
    choice = _Missing('choice')
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
CACHE = {}
LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER
async def do_pm_permit_action(event, chat):  
    reply_to_id = await reply_id(event)
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    me = await event.client.get_me()
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    if str(chat.id) not in PM_WARNS:
        PM_WARNS[str(chat.id)] = 0
    try:
        MAX_FLOOD_IN_PMS = int(gvarstatus("MAX_FLOOD_IN_PMS") or 10)
    except (ValueError, TypeError):
        MAX_FLOOD_IN_PMS = 10
    totalwarns = MAX_FLOOD_IN_PMS + 1
    warns = PM_WARNS[str(chat.id)] + 1
    remwarns = totalwarns - warns
    if PM_WARNS[str(chat.id)] >= MAX_FLOOD_IN_PMS:
        try:
            if str(chat.id) in PMMESSAGE_CACHE:
                await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
                del PMMESSAGE_CACHE[str(chat.id)]
        except Exception as e:
            LOGS.info(str(e))
        custompmblock = gvarstatus("pmblock") or None
        if custompmblock is not None:
            USER_BOT_WARN_ZERO = custompmblock.format(mention=mention, first=first, last=last, fullname=fullname, username=username, userid=userid, my_first=my_first, my_last=my_last, my_fullname=my_fullname, my_username=my_username, my_mention=my_mention, totalwarns=totalwarns, warns=warns, remwarns=remwarns)
        else:
            USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن الـتـڪـرار . تـم حـظـرڪ ، لا يـمـڪـنـڪ ازعـاج الـمـالـڪ !**"
        msg = await event.reply(USER_BOT_WARN_ZERO)
        await event.client(functions.contacts.BlockRequest(chat.id))
        the_message = f"**🝳 ⦙  الـمـحـضـوريـن مـن الـخـاص : 📩**\n🝳 ⦙   [{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫** \n**🝳 ⦙   عـدد الـرسـائـل :** {PM_WARNS[str(chat.id)]}"
        del PM_WARNS[str(chat.id)]
        sql.del_collection("pmwarns")
        sql.del_collection("pmmessagecache")
        sql.add_collection("pmwarns", PM_WARNS, {})
        sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
        try:
            return await event.client.send_message(BOTLOG_CHATID,the_message)
        except BaseException:
            return
    custompmpermit = gvarstatus("pmpermit_txt") or None
    if custompmpermit is not None:
        USER_BOT_NO_WARN = custompmpermit.format(mention=mention,first=first,last=last,fullname=fullname,username=username,userid=userid,my_first=my_first,my_last=my_last,my_fullname=my_fullname,my_username=my_username,my_mention=my_mention,totalwarns=totalwarns,warns=warns,remwarns=remwarns)
    elif gvarstatus("pmmenu") is None:
        USER_BOT_NO_WARN = f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗᵉˡᵉᵗʰᵒᶰ ᵃʳᵃᵇˢ‌ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n❞ هـاﺂ هـݪـو٘ {mention} ❝ 🦋\nاﻧـا آݪان ﻣـﺷـغٓول ݪاتࢪﺳـݪ ݪي ࢪﺳـآئݪ ڪﺛـيࢪه وآݪآ سيٰتم حٓـظٍـࢪڪ فقـط قـࢦ سـبب مجـيٰـئڪ اوَ حٰٖـآِجٰتـڪِٰ ، عٰٖـنِ٘ـدمـا آﻋـۅد سِ٘أوافـق علـى ﻣحٰٖـآِډثـتِـك  .. ❞ \n ⤶ ❨  `{warns}/{totalwarns}` ❩\n\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗᵉˡᵉᵗʰᵒᶰ ᵃʳᵃᵇˢ‌ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
    else:
        USER_BOT_NO_WARN = f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗᵉˡᵉᵗʰᵒᶰ ᵃʳᵃᵇˢ‌ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n❞ هـاﺂ هـݪـو٘ {mention} ❝ 🦋\nاﻧـا آݪان ﻣـﺷـغٓول ݪاتࢪﺳـݪ ݪي ࢪﺳـآئݪ ڪﺛـيࢪه وآݪآ سيٰتم حٓـظٍـࢪڪ فقـط قـࢦ سـبب مجـيٰـئڪ اوَ حٰٖـآِجٰتـڪِٰ ، عٰٖـنِ٘ـدمـا آﻋـۅد سِ٘أوافـق علـى ﻣحٰٖـآِډثـتِـك  .. ❞ \n ⤶ ❨  `{warns}/{totalwarns}` ❩\n\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧᵗᵉˡᵉᵗʰᵒᶰ ᵃʳᵃᵇˢ‌ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
    addgvar("pmpermit_text", USER_BOT_NO_WARN)
    PM_WARNS[str(chat.id)] += 1
    try:
        if gvarstatus("pmmenu") is None:
            results = await event.client.inline_query(Config.TG_BOT_USERNAME, "pmpermit")
            msg = await results[0].click(chat.id, reply_to=reply_to_id, hide_via=True)
        else:
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                CAT_IMG = random.choice(PIC)
            else:
                CAT_IMG = None
            if CAT_IMG is not None:
                msg = await event.client.send_file(chat.id,CAT_IMG,caption=USER_BOT_NO_WARN,reply_to=reply_to_id,force_document=False)
            else:
                msg = await event.client.send_message(chat.id, USER_BOT_NO_WARN, reply_to=reply_to_id)
    except Exception as e:
        LOGS.error(e)
        msg = await event.reply(USER_BOT_NO_WARN)
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    PMMESSAGE_CACHE[str(chat.id)] = msg.id
    sql.del_collection("pmwarns")
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmwarns", PM_WARNS, {})
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})

async def do_pm_options_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if event.sender_id == 1226408155:
            return
    if str(chat.id) not in PM_WARNS:
        text = "**🝳 ⦙  اخـتـࢪ احـد الخـيـاࢪات فـي الأعـلى بـلا تـڪـࢪاࢪ ، وهـذا تـحـذيـࢪڪ الاخـيـࢪ !❕🤍**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل .** \n**🝳 ⦙   تـم حـظـرڪ مـن الـحـسـاب 🚫.** \n**🝳 ⦙  لـن اسـتـلـم رسـائـلـڪ الـى ان يـاتـي مـالـڪ الـحـسـاب .🧸**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"**🝳 ⦙  حـمـايـة الـخـاص  (الـبـرايـفـت)  : 📩** \n[{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫**\n**🝳 ⦙  الـسـبـب ~> اسـتـمـر بـالـتـكـرار .♻️**"
    sqllist.rm_from_list("pmoptions", chat.id)
    try:
        return await event.client.send_message(BOTLOG_CHATID, the_message)
    except BaseException:
        return

async def do_pm_enquire_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**🝳 ⦙  يـرجـى الانـتـظـار لــ حـيـن قرائة رسالتك  .🌀 \n 🝳 ⦙   مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد اسـتـطـاعـتـه .. \n 🝳 ⦙   يـرجـى عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🙂🌿**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        # await asyncio.sleep(5)
        # await msg.delete()
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل .** \n**🝳 ⦙   تـم حـظـرڪ مـن الـحـسـاب 🚫.** \n**🝳 ⦙  لـن اسـتـلـم رسـائـلـڪ الـى ان يـاتـي مـالـڪ الـحـسـاب .🧸**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"**🝳 ⦙  حـمـايـة الـخـاص  (الـبـرايـفـت)  : 📩** \n[{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫**\n**🝳 ⦙  الـسـبـب ~> اسـتـمـر بـالـتـكـرار .♻️**"
    sqllist.rm_from_list("pmenquire", chat.id)
    try:
        return await event.client.send_message(BOTLOG_CHATID,the_message)
    except BaseException:
        return

async def do_pm_request_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**🝳 ⦙  يـرجـى الانـتـظـار لــ حـيـن قرائة رسالتك  🌀. \n 🝳 ⦙   مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد اسـتـطـاعـتـه . . \n 🝳 ⦙   يـرجـى عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🙂🌿**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل .** \n**🝳 ⦙   تـم حـظـرڪ مـن الـحـسـاب 🚫.** \n**🝳 ⦙  لـن اسـتـلـم رسـائـلـڪ الـى ان يـاتـي مـالـڪ الـحـسـاب .🧸**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"**🝳 ⦙  حـمـايـة الـخـاص  (الـبـرايـفـت)  : 📩**\n[{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫**\n**🝳 ⦙  الـسـبـب ~> اسـتـمـر بـالـتـكـرار .♻️**"
    sqllist.rm_from_list("pmrequest", chat.id)
    try:
        return await event.client.send_message(BOTLOG_CHATID, the_message)
    except BaseException:
        return

async def do_pm_chat_action(event, chat):
    try:
        PM_WARNS = sql.get_collection("pmwarns").json
    except AttributeError:
        PM_WARNS = {}
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    if str(chat.id) not in PM_WARNS:
        text = "**🝳 ⦙  يـرجـى الانـتـظـار لــ حـيـن قرائة رسالتك  🌀. \n 🝳 ⦙   مـالـڪ الـحـسـاب سَــوف يـرد عـلـيـڪ عـنـد اسـتـطـاعـتـه . . \n 🝳 ⦙   يـرجـى عـدم تـڪـرار الـرسـائـل لـتـجـنـب الـحـظـر 🙂🌿**"
        await event.reply(text)
        PM_WARNS[str(chat.id)] = 1
        sql.del_collection("pmwarns")
        sql.add_collection("pmwarns", PM_WARNS, {})
        return None
    del PM_WARNS[str(chat.id)]
    sql.del_collection("pmwarns")
    sql.add_collection("pmwarns", PM_WARNS, {})
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    sql.del_collection("pmmessagecache")
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل .** \n**🝳 ⦙   تـم حـظـرڪ مـن الـحـسـاب 🚫.** \n**🝳 ⦙  لـن اسـتـلـم رسـائـلـڪ الـى ان يـاتـي مـالـڪ الـحـسـاب .🧸**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"**🝳 ⦙  حـمـايـة الـخـاص  (الـبـرايـفـت)  : 📩**\n[{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫**\n**🝳 ⦙  الـسـبـب ~> اسـتـمـر بـالـتـكـرار .♻️**"
    sqllist.rm_from_list("pmchat", chat.id)
    try:
        return await event.client.send_message(BOTLOG_CHATID, the_message)
    except BaseException:
        return
async def do_pm_spam_action(event, chat):
    try:
        PMMESSAGE_CACHE = sql.get_collection("pmmessagecache").json
    except AttributeError:
        PMMESSAGE_CACHE = {}
    try:
        if str(chat.id) in PMMESSAGE_CACHE:
            await event.client.delete_messages(chat.id, PMMESSAGE_CACHE[str(chat.id)])
            del PMMESSAGE_CACHE[str(chat.id)]
    except Exception as e:
        LOGS.info(str(e))
    USER_BOT_WARN_ZERO = f"**🝳 ⦙  تـم تـحـذيـرڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل .** \n**🝳 ⦙   تـم حـظـرڪ مـن الـحـسـاب 🚫.** \n**🝳 ⦙  لـن اسـتـلـم رسـائـلـڪ الـى ان يـاتـي مـالـڪ الـحـسـاب .🧸**"
    await event.reply(USER_BOT_WARN_ZERO)
    await event.client(functions.contacts.BlockRequest(chat.id))
    the_message = f"**🝳 ⦙  حـمـايـة الـخـاص  (الـبـرايـفـت)  : 📩**\n[{get_display_name(chat)}](tg://user?id={chat.id}) **تـم حـظـر الـمـسـتـخـدم .🗣🚫**\n**🝳 ⦙  الـسـبـب ~> اسـتـمـر بـالـتـكـرار .♻️**"
    sqllist.rm_from_list("pmspam", chat.id)
    sql.add_collection("pmmessagecache", PMMESSAGE_CACHE, {})
    try:
        return await event.client.send_message(BOTLOG_CHATID,the_message)
    except BaseException:
        return







