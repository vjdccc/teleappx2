# -*- coding: utf-8 -*-
"""
arabcompat - طبقة توافق تشغّل أوامر "Telethon Zahid" (المبنية على Telethon)
فوق Pyrogram. تقدم نفس الواجهة التي تستعملها الأوامر: event.edit / client.send_file / conversation ...
كل شيء هنا يعمل بـ Pyrogram + مكتبات بايثون العادية، والحزم الإضافية اختيارية (تُحمّل تلقائياً إن وُجدت).
"""
import asyncio, base64, glob, html as _html, inspect, io, itertools, json, logging, math
import mimetypes, os, random, re, shlex, shutil, string, subprocess, sys, textwrap, time, traceback
from collections import deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Tuple

from pyrogram import Client, filters, enums
from pyrogram import errors as _perr
from pyrogram.handlers import MessageHandler

from config import app, bot, r, sudo_id, sudo_command
from arabstyle import dget, dset

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = logging.getLogger("arab")
logging = logging  # noqa  (بعض الأوامر تستعمل logging.getLogger)

# ───────────────────────── اعدادات (بديل Config) ─────────────────────────
class _Cfg:
    ALIVE_NAME = "المستخدم"
    AUTONAME = None
    DEFAULT_BIO = None
    COMMAND_HAND_LER = "."
    OWNER_ID = sudo_id
    SUDO_USERS = set()
    TMP_DOWNLOAD_DIRECTORY = "./temp/"
    PM_LOGGER_GROUP_ID = -100
    PRIVATE_GROUP_BOT_API_ID = None
    PRIVATE_CHANNEL_BOT_API_ID = None
    HEROKU_APP_NAME = None
    HEROKU_API_KEY = None
    THUMB_IMAGE = None
    NO_LOAD = []

    def __getattr__(self, name):  # أي اعداد غير معرّف يرجع None بدل خطأ
        if name.startswith("__"):
            raise AttributeError(name)
        return None


Config = _Cfg()
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
os.makedirs(TMP_DOWNLOAD_DIRECTORY, exist_ok=True)
BOTLOG = False
BOTLOG_CHATID = 0
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = None
DEFAULT_BIO = None
USERID = sudo_id
mention = f"[{ALIVE_NAME}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{ALIVE_NAME}</a>"
PM_START, PMMESSAGE_CACHE, SUDO_LIST = [], {}, []
PMMENU = False
HEROKU_APP = None
StartTime = time.time()
catversion = version = "1.0"
plugin_category = "Telethon Zahid"
thumb_image_path = os.path.join(TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

# ───────────────────────── تخزين دائم (JSON) ─────────────────────────
def gvarstatus(key):
    try:
        return dget("gv:" + str(key))
    except Exception:
        return None


def addgvar(key, value):
    dset("gv:" + str(key), str(value))


def delgvar(key):
    dset("gv:" + str(key), None)


def _lst(name):
    v = dget("gl:" + name, None)
    return v if isinstance(v, list) else []


def add_to_list(keyword, value):
    items = _lst(keyword)
    if value not in items:
        items.append(value)
        dset("gl:" + keyword, items)
    return True


def rm_from_list(keyword, value):
    items = _lst(keyword)
    if value in items:
        items.remove(value)
        dset("gl:" + keyword, items)
        return True
    return False


def is_in_list(keyword, value):
    return value in _lst(keyword)


def get_collection_list(keyword):
    return list(_lst(keyword))


def del_keyword_list(keyword):
    dset("gl:" + keyword, [])


add_to_collectionlist = add_to_list
del_keyword_collectionlist = del_keyword_list
get_collectionlist_items = get_collection_list


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value not in dictionary[key]:
            dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


# ───────────────────────── مكتبات اختيارية ─────────────────────────
import contextvars
IN_HANDLER = contextvars.ContextVar('arab_in_handler', default=False)


class _Missing:
    """بديل لمكتبة غير مثبتة: لا يكسر تحميل الاضافة، ويعطي رسالة واضحة عند الاستعمال."""

    def __init__(self, name):
        object.__setattr__(self, "_n", name)

    def _fail(self, *a, **k):
        if not IN_HANDLER.get():  # وقت تحميل الاضافة: لا نكسر الاستيراد
            return _Missing(f"{self._n}()")
        raise ImportError(f"المكتبة '{self._n}' غير مثبتة؛ ثبّتها بالأمر: pip install {self._n.split('.')[0]}")

    def __getattr__(self, item):
        if item.startswith("__"):
            raise AttributeError(item)
        return _Missing(f"{self._n}.{item}")

    __call__ = _fail

    def __bool__(self):
        return False


def optional(modname):
    try:
        return __import__(modname, fromlist=["_"])
    except Exception:
        return _Missing(modname)


# ───────────────────────── اخطاء تيليثون → بايروجرام ─────────────────────────
def _err(name, fallback_base=Exception):
    return getattr(_perr, name, None) or type(name, (fallback_base,), {})


FloodWaitError = _err("FloodWait")
if not hasattr(FloodWaitError, "seconds"):
    try:
        FloodWaitError.seconds = property(lambda self: getattr(self, "value", 0))
    except Exception:
        pass
MessageNotModifiedError = _err("MessageNotModified")
YouBlockedUserError = _err("UserIsBlocked")
ChatAdminRequiredError = _err("ChatAdminRequired")
UserAdminInvalidError = _err("UserAdminInvalid")
BadRequestError = _err("BadRequest")
UserAlreadyParticipantError = _err("UserAlreadyParticipant")
MessageTooLongError = _err("MessageTooLong")
MediaEmptyError = _err("MediaEmpty")
PhotoCropSizeSmallError = _err("PhotoCropSizeSmall")
PhotoInvalidDimensionsError = _err("PhotoInvalidDimensions")
ImageProcessFailedError = _err("ImageProcessFailed")
ChannelInvalidError = _err("ChannelInvalid")
ChannelPrivateError = _err("ChannelPrivate")
ChannelPublicGroupNaError = _err("ChannelPublicGroupNa")
QueryIdInvalidError = _err("QueryIdInvalid")
UsernameOccupiedError = _err("UsernameOccupied")
UserIdInvalidError = _err("UserIdInvalid")
BotInlineDisabledError = _err("BotInlineDisabled")
ChatSendInlineForbiddenError = _err("ChatSendInlineForbidden")
ChatSendStickersForbiddenError = _err("ChatSendStickersForbidden")
rpcbaseerrors = (_err("RPCError"),)
AsyncTimeout = asyncio.TimeoutError


async def _flood(coro_fn, *a, **k):
    """ينفّذ استدعاء بايروجرام ويعيد المحاولة مرة عند FloodWait قصير."""
    try:
        return await coro_fn(*a, **k)
    except _perr.FloodWait as e:
        wait = int(getattr(e, "value", 5) or 5)
        if wait > 90:
            raise
        await asyncio.sleep(wait + 1)
        return await coro_fn(*a, **k)


# ───────────────────────── تحويل parse_mode ─────────────────────────
def _pm(parse_mode):
    if parse_mode is None:
        return enums.ParseMode.MARKDOWN
    if isinstance(parse_mode, enums.ParseMode):
        return parse_mode
    p = str(parse_mode).lower()
    if p in ("html", "htm"):
        return enums.ParseMode.HTML
    if p in ("md", "markdown"):
        return enums.ParseMode.MARKDOWN
    if p in ("none", "disabled"):
        return enums.ParseMode.DISABLED
    return enums.ParseMode.MARKDOWN


# ═════════════════════════ كيانات (مستخدم / محادثة) ═════════════════════════
def _mk_filter(attrname, names):
    class _F:
        pass
    _F.f = None
    for n in names:
        v = getattr(enums.MessagesFilter, n, None)
        if v is not None:
            _F.f = v
            break
    return _F


class _EntMeta(type):
    def __instancecheck__(cls, obj):
        o = getattr(obj, "_o", obj)
        return cls._chk(o)


def _ctype(o):
    if o.__class__.__name__ == "User":
        return "user"
    t = getattr(o, "type", None)
    if t in (enums.ChatType.PRIVATE, getattr(enums.ChatType, "BOT", None)):
        return "user"
    if t == enums.ChatType.GROUP:
        return "group"
    if t in (enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL):
        return "channel"
    return "?"


class User(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: _ctype(o) == "user")


class Chat(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: _ctype(o) == "group")


class Channel(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: _ctype(o) == "channel")


class AdminRights:
    """يشبه ChatAdminRights في تيليثون (للقراءة)."""

    def __init__(self, p=None):
        g = lambda n: bool(getattr(p, n, False)) if p is not None else False
        self.change_info = g("can_change_info")
        self.post_messages = g("can_post_messages")
        self.edit_messages = g("can_edit_messages")
        self.delete_messages = g("can_delete_messages")
        self.ban_users = g("can_restrict_members")
        self.invite_users = g("can_invite_users")
        self.pin_messages = g("can_pin_messages")
        self.add_admins = g("can_promote_members")
        self.manage_call = g("can_manage_video_chats")
        self.anonymous = g("is_anonymous")
        self.other = g("can_manage_chat")


class _Ent:
    """غلاف حول User/Chat في Pyrogram ليبدو كأنه كيان Telethon."""

    creator = False
    admin_rights = None
    default_banned_rights = None
    access_hash = 0

    def __init__(self, o):
        object.__setattr__(self, "_o", o)

    # الاسماء المختلفة بين المكتبتين
    _ALIAS = {
        "bot": "is_bot", "deleted": "is_deleted", "verified": "is_verified",
        "restricted": "is_restricted", "scam": "is_scam", "fake": "is_fake",
        "premium": "is_premium", "phone": "phone_number", "contact": "is_contact",
        "mutual_contact": "is_mutual_contact", "support": "is_support",
        "participants_count": "members_count",
    }

    def __getattr__(self, n):
        if n.startswith("__"):
            raise AttributeError(n)
        o = object.__getattribute__(self, "_o")
        if n == "id":
            i = o.id
            if isinstance(i, int) and i < -1000000000000:
                return -(i + 1000000000000)
            if isinstance(i, int) and i < 0:
                return -i
            return i
        if n == "megagroup":
            return getattr(o, "type", None) == enums.ChatType.SUPERGROUP
        if n == "broadcast":
            return getattr(o, "type", None) == enums.ChatType.CHANNEL
        if n == "gigagroup":
            return False
        if n == "self":
            return bool(getattr(o, "is_self", False))
        if n == "about":
            return getattr(o, "description", None) or getattr(o, "bio", None)
        if n == "title":
            t = getattr(o, "title", None)
            return t
        if n in self._ALIAS:
            return getattr(o, self._ALIAS[n], None if n != "bot" else False)
        return getattr(o, n)

    def __eq__(self, other):
        a = getattr(self, "_o", None)
        b = getattr(other, "_o", other)
        return a is b or (getattr(a, "id", 1) == getattr(b, "id", 2))

    def __hash__(self):
        return hash(getattr(self._o, "id", id(self._o)))

    def __repr__(self):
        return f"<Ent {self._o!r}>"[:200]


def _ent(o):
    if o is None or isinstance(o, _Ent):
        return o
    return _Ent(o)


def get_display_name(entity):
    if entity is None:
        return ""
    o = getattr(entity, "_o", entity)
    t = getattr(o, "title", None)
    if t:
        return t
    return " ".join(x for x in (getattr(o, "first_name", None), getattr(o, "last_name", None)) if x) or ""


def _mid(chat_id):
    """ايدي قناة/مجموعة بدون -100 (مثل Telethon)."""
    try:
        i = int(chat_id)
    except Exception:
        return chat_id
    if i < -1000000000000:
        return -(i + 1000000000000)
    return abs(i)


# ═════════════════════════ فلاتر الرسائل / الاعضاء ═════════════════════════
class InputMessagesFilterPhotos(_mk_filter("", ["PHOTO"])): pass
class InputMessagesFilterVideo(_mk_filter("", ["VIDEO"])): pass
class InputMessagesFilterDocument(_mk_filter("", ["DOCUMENT"])): pass
class InputMessagesFilterUrl(_mk_filter("", ["URL"])): pass
class InputMessagesFilterGif(_mk_filter("", ["ANIMATION"])): pass
class InputMessagesFilterVoice(_mk_filter("", ["VOICE_NOTE"])): pass
class InputMessagesFilterMusic(_mk_filter("", ["AUDIO"])): pass
class InputMessagesFilterRoundVideo(_mk_filter("", ["VIDEO_NOTE"])): pass
class InputMessagesFilterGeo(_mk_filter("", ["LOCATION"])): pass
class InputMessagesFilterPinned(_mk_filter("", ["PINNED"])): pass
class InputMessagesFilterMyMentions(_mk_filter("", ["MENTION"])): pass
class InputMessagesFilterEmpty(_mk_filter("", ["EMPTY"])): pass


def _cmf(name):
    class _C:
        pass
    _C.f = getattr(enums.ChatMembersFilter, name, None)
    return _C


class ChannelParticipantsAdmins(_cmf("ADMINISTRATORS")): pass
class ChannelParticipantsBots(_cmf("BOTS")): pass
class ChannelParticipantsKicked(_cmf("BANNED")): pass
class ChannelParticipantsBanned(_cmf("RESTRICTED")): pass
class ChannelParticipantsRecent(_cmf("RECENT")): pass
class ChannelParticipantsSearch(_cmf("SEARCH")): pass


class ChannelParticipantAdmin(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: getattr(o, "status", None) == enums.ChatMemberStatus.ADMINISTRATOR)


class ChannelParticipantCreator(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: getattr(o, "status", None) == enums.ChatMemberStatus.OWNER)


# ═════════════════════════ الرسالة (Msg) ═════════════════════════
class _PeerId:
    def __init__(self, i, kind="user"):
        self.user_id = i if kind == "user" else None
        self.channel_id = i if kind == "channel" else None
        self.chat_id = i if kind == "chat" else None


class _ReplyTo:
    def __init__(self, rid, top=None):
        self.reply_to_msg_id = rid
        self.reply_to_top_id = top


class _FileInfo:
    def __init__(self, m):
        o = None
        for n in ("photo", "audio", "voice", "video", "video_note", "animation", "sticker", "document"):
            o = getattr(m, n, None)
            if o:
                self.kind = n
                break
        self._o = o
        self.name = getattr(o, "file_name", None)
        self.mime_type = getattr(o, "mime_type", None) or ("image/jpeg" if getattr(m, "photo", None) else None)
        self.size = getattr(o, "file_size", None)
        self.duration = getattr(o, "duration", None)
        self.width = getattr(o, "width", None)
        self.height = getattr(o, "height", None)
        self.id = getattr(o, "file_id", None)
        self.title = getattr(o, "title", None)
        self.performer = getattr(o, "performer", None)
        ext = os.path.splitext(self.name or "")[1]
        if not ext and self.mime_type:
            ext = mimetypes.guess_extension(self.mime_type) or ""
        if not ext and getattr(m, "photo", None):
            ext = ".jpg"
        self.ext = ext


class MediaRef:
    """يمثّل media الرسالة (للارسال/النسخ لاحقاً)."""

    def __init__(self, m):
        self._m = m

    def __bool__(self):
        return bool(getattr(self._m, "media", None))

    @property
    def photo(self):
        return getattr(self._m, "photo", None)

    @property
    def document(self):
        for n in ("document", "audio", "voice", "video", "video_note", "animation", "sticker"):
            o = getattr(self._m, n, None)
            if o:
                return o
        return None

    @property
    def webpage(self):
        return getattr(self._m, "web_page", None)


class MessageMediaPhoto(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: isinstance(o, MediaRef) and bool(o.photo))


class MessageMediaWebPage(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: isinstance(o, MediaRef) and bool(o.webpage))


class _Ent2:  # كيان "mention" داخل النص
    def __init__(self, e):
        self._e = e
        self.offset = e.offset
        self.length = e.length
        self.url = getattr(e, "url", None)
        u = getattr(e, "user", None)
        self.user_id = u.id if u else None

    def __getattr__(self, n):
        return getattr(self._e, n)


class MessageEntityMentionName(metaclass=_EntMeta):
    _chk = staticmethod(lambda o: isinstance(o, _Ent2) and o.user_id is not None)


def _txt(s):
    return "" if s is None else str(s)


def _rid(reply_to):
    if reply_to is None or reply_to is False:
        return None
    if isinstance(reply_to, Msg):
        return reply_to.id
    if hasattr(reply_to, "id") and not isinstance(reply_to, int):
        return reply_to.id
    return int(reply_to)


class Msg:
    """رسالة بواجهة Telethon."""

    def __init__(self, client, m):
        self._m = m
        self.client = client
        self._reply = None

    # ---- هوية
    @property
    def id(self):
        return self._m.id

    @property
    def chat_id(self):
        return self._m.chat.id if self._m.chat else None

    @property
    def sender_id(self):
        m = self._m
        if m.from_user:
            return m.from_user.id
        if m.sender_chat:
            return m.sender_chat.id
        return None

    @property
    def from_id(self):
        m = self._m
        if m.from_user:
            return _PeerId(m.from_user.id, "user")
        if m.sender_chat:
            return _PeerId(m.sender_chat.id, "channel")
        return None

    @property
    def out(self):
        return bool(getattr(self._m, "outgoing", False))

    @property
    def date(self):
        return self._m.date

    @property
    def mentioned(self):
        return bool(getattr(self._m, "mentioned", False))

    @property
    def via_bot_id(self):
        v = getattr(self._m, "via_bot", None)
        return v.id if v else None

    @property
    def fwd_from(self):
        m = self._m
        if getattr(m, "forward_date", None) or getattr(m, "forward_origin", None) or \
                getattr(m, "forward_from", None) or getattr(m, "forward_from_chat", None):
            return m
        return None

    # ---- نص
    def _plain(self):
        return _txt(self._m.text or self._m.caption)

    @property
    def message(self):
        return self._plain()

    @property
    def raw_text(self):
        return self._plain()

    @property
    def text(self):
        s = self._m.text or self._m.caption
        if s is None:
            return ""
        return getattr(s, "markdown", None) or str(s)

    @property
    def entities(self):
        es = self._m.entities or self._m.caption_entities or []
        return [_Ent2(e) for e in es]

    # ---- ردود
    @property
    def reply_to_msg_id(self):
        m = self._m
        rid = getattr(m, "reply_to_message_id", None)
        if rid is None and getattr(m, "reply_to_message", None) is not None:
            rid = m.reply_to_message.id
        return rid

    @property
    def is_reply(self):
        return bool(self.reply_to_msg_id)

    @property
    def reply_to(self):
        rid = self.reply_to_msg_id
        return _ReplyTo(rid, getattr(self._m, "message_thread_id", None)) if rid else None

    async def get_reply_message(self):
        if self._reply is not None:
            return self._reply
        rid = self.reply_to_msg_id
        if not rid:
            return None
        rm = getattr(self._m, "reply_to_message", None)
        if rm is None or getattr(rm, "empty", False):
            try:
                rm = await self.client._c.get_messages(self._m.chat.id, rid)
            except Exception:
                return None
        if rm is None or getattr(rm, "empty", False):
            return None
        self._reply = Msg(self.client, rm)
        return self._reply

    # ---- نوع المحادثة
    @property
    def is_private(self):
        return self._m.chat.type in (enums.ChatType.PRIVATE, getattr(enums.ChatType, "BOT", enums.ChatType.PRIVATE))

    @property
    def is_group(self):
        return self._m.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP)

    @property
    def is_channel(self):
        return self._m.chat.type in (enums.ChatType.CHANNEL, enums.ChatType.SUPERGROUP)

    # ---- وسائط
    @property
    def media(self):
        return MediaRef(self._m) if getattr(self._m, "media", None) else None

    @property
    def photo(self):
        return getattr(self._m, "photo", None)

    @property
    def sticker(self):
        return getattr(self._m, "sticker", None)

    @property
    def voice(self):
        return getattr(self._m, "voice", None)

    @property
    def audio(self):
        return getattr(self._m, "audio", None)

    @property
    def video(self):
        return getattr(self._m, "video", None)

    @property
    def video_note(self):
        return getattr(self._m, "video_note", None)

    @property
    def gif(self):
        return getattr(self._m, "animation", None)

    @property
    def document(self):
        m = self._m
        for n in ("document", "audio", "voice", "video", "video_note", "animation", "sticker"):
            o = getattr(m, n, None)
            if o:
                return o
        return None

    @property
    def web_preview(self):
        return getattr(self._m, "web_page", None)

    @property
    def geo(self):
        return getattr(self._m, "location", None)

    @property
    def contact(self):
        return getattr(self._m, "contact", None)

    @property
    def file(self):
        if not getattr(self._m, "media", None):
            return None
        return _FileInfo(self._m)

    @property
    def buttons(self):
        return None

    @property
    def reply_markup(self):
        return getattr(self._m, "reply_markup", None)

    # ---- افعال
    async def edit(self, text=None, *, parse_mode=None, link_preview=None, file=None, buttons=None, **kw):
        if file is not None:
            new = await self.client.send_file(self.chat_id, file, caption=text, parse_mode=parse_mode)
            try:
                await self.delete()
            except Exception:
                pass
            self._m = new._m
            return self
        text = _txt(text)
        kwargs = {"parse_mode": _pm(parse_mode)}
        if link_preview is not None:
            kwargs["disable_web_page_preview"] = not link_preview
        try:
            if getattr(self._m, "media", None) and not getattr(self._m, "web_page", None):
                kwargs.pop("disable_web_page_preview", None)
                await _flood(self._m.edit_caption, text, **kwargs)
            else:
                await _flood(self._m.edit_text, text, **kwargs)
        except _perr.MessageNotModified:
            pass
        return self

    async def reply(self, message="", *, file=None, parse_mode=None, link_preview=None, buttons=None, silent=None, **kw):
        if file is not None:
            return await self.client.send_file(self.chat_id, file, caption=message, reply_to=self.id,
                                               parse_mode=parse_mode, silent=silent)
        return await self.client.send_message(self.chat_id, message, reply_to=self.id, parse_mode=parse_mode,
                                              link_preview=link_preview, silent=silent)

    async def respond(self, message="", *, file=None, parse_mode=None, link_preview=None, buttons=None, silent=None, **kw):
        if file is not None:
            return await self.client.send_file(self.chat_id, file, caption=message, parse_mode=parse_mode, silent=silent)
        return await self.client.send_message(self.chat_id, message, parse_mode=parse_mode,
                                              link_preview=link_preview, silent=silent)

    async def delete(self, *, revoke=True):
        try:
            await self._m.delete(revoke=revoke)
        except TypeError:
            await self._m.delete()
        return True

    async def forward_to(self, entity):
        return await self.client.forward_messages(entity, self)

    async def pin(self, *, notify=False):
        await self.client.pin_message(self.chat_id, self, notify=notify)

    async def mark_read(self):
        await self.client.send_read_acknowledge(self.chat_id)

    async def download_media(self, file=None, *, thumb=None, progress_callback=None):
        return await self.client.download_media(self, file)

    async def get_sender(self):
        m = self._m
        if m.from_user:
            return _ent(m.from_user)
        if m.sender_chat:
            return _ent(m.sender_chat)
        return None

    async def get_input_sender(self):
        return await self.get_sender()

    async def get_chat(self):
        return await self.client._chat_full(self._m.chat)

    async def get_input_chat(self):
        return _ent(self._m.chat)

    async def get_user(self):
        return await self.get_sender()

    @property
    def chat(self):
        return _ent(self._m.chat)

    @property
    def input_chat(self):
        return _ent(self._m.chat)

    @property
    def sender(self):
        return _ent(self._m.from_user or self._m.sender_chat)

    # أحداث الانضمام (ChatAction)
    @property
    def user_joined(self):
        return bool(getattr(self._m, "new_chat_members", None))

    @property
    def user_added(self):
        nm = getattr(self._m, "new_chat_members", None)
        return bool(nm and self._m.from_user and nm[0].id != self._m.from_user.id)

    @property
    def user_left(self):
        return bool(getattr(self._m, "left_chat_member", None))

    @property
    def action_message(self):
        return self._m


class Ev(Msg):
    """حدث NewMessage بواجهة Telethon."""

    def __init__(self, client, m, match=None):
        super().__init__(client, m)
        self.pattern_match = match
        self._msgobj = None

    @property
    def message(self):  # event.message يرجع رسالة (وليس نصاً)
        if self._msgobj is None:
            self._msgobj = Msg(self.client, self._m)
            self._msgobj._reply = self._reply
        return self._msgobj

    async def get_user(self):
        m = self._m
        if getattr(m, "new_chat_members", None):
            return _ent(m.new_chat_members[0])
        if getattr(m, "left_chat_member", None):
            return _ent(m.left_chat_member)
        return await self.get_sender()


# ═════════════════════════ العميل (CClient) ═════════════════════════
_IMG = {".jpg", ".jpeg", ".png", ".bmp"}
_AUD = {".mp3", ".m4a", ".flac", ".wav", ".aac", ".wma", ".opus_audio"}
_VOI = {".ogg", ".oga", ".opus"}
_VID = {".mp4", ".mkv", ".mov", ".avi", ".webm", ".3gp", ".m4v", ".ts"}


def _peer(e):
    if e is None:
        return "me"
    if isinstance(e, bool):
        raise ValueError("bad peer")
    if isinstance(e, int):
        return e
    if isinstance(e, str):
        s = e.strip()
        if re.fullmatch(r"-?\d+", s):
            return int(s)
        if "t.me/" in s:
            s = s.rsplit("/", 1)[-1]
        return s.lstrip("@") if s.lower() != "me" else "me"
    if isinstance(e, _Ent):
        return e._o.id
    if isinstance(e, Msg):
        return e.chat_id
    i = getattr(e, "id", None)
    if i is not None:
        return i
    raise ValueError(f"Cannot use {e!r} as input entity")


def _kind_of(name, force_document=False):
    ext = os.path.splitext(str(name).split("?")[0])[1].lower()
    if force_document:
        return "document"
    if ext in _IMG:
        return "photo"
    if ext in _VOI:
        return "voice"
    if ext in _AUD:
        return "audio"
    if ext in _VID:
        return "video"
    if ext == ".gif":
        return "animation"
    if ext in (".webp", ".tgs"):
        return "sticker"
    return "document"


def _thumb(t):
    return t if isinstance(t, str) and os.path.exists(t) else None


class _Dialog:
    def __init__(self, d):
        self._d = d
        c = d.chat
        self.entity = _Ent(c)
        self.id = c.id
        self.name = c.title or " ".join(x for x in (getattr(c, "first_name", None), getattr(c, "last_name", None)) if x)
        t = _ctype(c)
        self.is_user = t == "user"
        self.is_group = t == "group" or getattr(c, "type", None) == enums.ChatType.SUPERGROUP
        self.is_channel = t == "channel"
        self.message = d.top_message
        self.date = getattr(d.top_message, "date", None)
        self.unread_count = getattr(d, "unread_messages_count", 0)
        self.archived = False
        self.pinned = bool(getattr(d, "is_pinned", False))

    def __getattr__(self, n):
        return getattr(self._d, n)


class _PhotoList(list):
    total = 0


class _TotalList(list):
    @property
    def total(self):
        return len(self)


class _Action:
    _MAP = {
        "typing": "TYPING", "contact": "CHOOSE_CONTACT", "game": "PLAYING", "location": "FIND_LOCATION",
        "sticker": "CHOOSE_STICKER", "record-audio": "RECORD_AUDIO", "record-voice": "RECORD_AUDIO",
        "record-round": "RECORD_VIDEO_NOTE", "record-video": "RECORD_VIDEO", "audio": "UPLOAD_AUDIO",
        "voice": "UPLOAD_AUDIO", "round": "UPLOAD_VIDEO_NOTE", "video": "UPLOAD_VIDEO",
        "photo": "UPLOAD_PHOTO", "document": "UPLOAD_DOCUMENT", "file": "UPLOAD_DOCUMENT",
    }

    def __init__(self, cli, peer, action):
        self.cli, self.peer = cli, peer
        n = self._MAP.get(str(action).lower(), "TYPING")
        self.act = getattr(enums.ChatAction, n, enums.ChatAction.TYPING)
        self._t = None

    async def _loop(self):
        while True:
            try:
                await self.cli._c.send_chat_action(self.peer, self.act)
            except Exception:
                pass
            await asyncio.sleep(4)

    async def __aenter__(self):
        self._t = asyncio.ensure_future(self._loop())
        return self

    async def __aexit__(self, *a):
        if self._t:
            self._t.cancel()
        try:
            await self.cli._c.send_chat_action(self.peer, enums.ChatAction.CANCEL)
        except Exception:
            pass


class _Conv:
    """محادثة مع بوت: send_message / get_response بالاستطلاع."""

    def __init__(self, cli, entity, timeout=60, **kw):
        self.cli = cli
        self.peer = _peer(entity)
        self.timeout = timeout
        self._seen = 0

    async def __aenter__(self):
        try:
            async for m in self.cli._c.get_chat_history(self.peer, limit=1):
                self._seen = m.id
        except Exception:
            self._seen = 0
        return self

    async def __aexit__(self, *a):
        return False

    async def send_message(self, text="", **kw):
        m = await self.cli.send_message(self.peer, text, **kw)
        self._seen = max(self._seen, m.id)
        return m

    async def send_file(self, file, **kw):
        m = await self.cli.send_file(self.peer, file, **kw)
        self._seen = max(self._seen, m.id)
        return m

    async def get_response(self, message=None, *, timeout=None):
        end = time.time() + (timeout or self.timeout or 60)
        while time.time() < end:
            try:
                msgs = [m async for m in self.cli._c.get_chat_history(self.peer, limit=10)]
            except Exception:
                msgs = []
            new = sorted((m for m in msgs if m.id > self._seen and not m.outgoing), key=lambda x: x.id)
            if new:
                self._seen = new[0].id
                return Msg(self.cli, new[0])
            await asyncio.sleep(1)
        raise asyncio.TimeoutError()

    get_reply = get_response

    async def get_edit(self, message=None, *, timeout=None):
        await asyncio.sleep(2)
        async for m in self.cli._c.get_chat_history(self.peer, limit=1):
            return Msg(self.cli, m)

    async def wait_event(self, event=None, *, timeout=None):
        return await self.get_response(timeout=timeout)

    async def mark_read(self, message=None):
        try:
            await self.cli._c.read_chat_history(self.peer)
        except Exception:
            pass

    async def cancel_all(self):
        return None


class _InlineItem:
    def __init__(self, cli, qid, res):
        self.cli, self.qid, self.res = cli, qid, res
        self.id = res.id
        self.title = getattr(res, "title", None)
        self.description = getattr(res, "description", None)

    async def click(self, entity=None, *, reply_to=None, silent=False, **kw):
        m = await self.cli._c.send_inline_bot_result(_peer(entity), self.qid, self.id,
                                                     disable_notification=bool(silent),
                                                     reply_to_message_id=_rid(reply_to))
        return Msg(self.cli, m) if hasattr(m, "id") else m


class CClient:
    _inst = {}

    def __init__(self, c):
        self._c = c

    @classmethod
    def of(cls, c):
        if isinstance(c, CClient):
            return c
        k = id(c)
        if k not in cls._inst:
            cls._inst[k] = CClient(c)
        return cls._inst[k]

    @property
    def uid(self):
        me = getattr(self._c, "me", None)
        return me.id if me else sudo_id

    def __getattr__(self, n):
        if n.startswith("__"):
            raise AttributeError(n)
        return getattr(self._c, n)

    async def __call__(self, request):
        run = getattr(request, "_run", None)
        if run is None:
            raise NotImplementedError(f"طلب Telethon غير مدعوم: {request!r}")
        return await run(self)

    # ---------- معلومات
    async def get_me(self):
        return _ent(await self._c.get_me())

    async def get_entity(self, e):
        if isinstance(e, (list, tuple)):
            return [await self.get_entity(x) for x in e]
        if isinstance(e, _Ent):
            return e
        key = _peer(e)
        try:
            if isinstance(key, int) and key < 0:
                return _Ent(await self._c.get_chat(key))
            return _Ent(await self._c.get_users(key))
        except _perr.FloodWait:
            raise
        except Exception:
            try:
                return _Ent(await self._c.get_chat(key))
            except Exception as e2:
                raise ValueError(f"Could not find the input entity for {e!r}") from e2

    get_input_entity = get_entity

    async def _chat_full(self, chat):
        e = _Ent(chat)
        if _ctype(chat) in ("group", "channel"):
            try:
                me = await self._c.get_chat_member(chat.id, "me")
                if me.status == enums.ChatMemberStatus.OWNER:
                    e.creator = True
                    e.admin_rights = AdminRights(type("P", (), {k: True for k in (
                        "can_change_info", "can_post_messages", "can_edit_messages", "can_delete_messages",
                        "can_restrict_members", "can_invite_users", "can_pin_messages", "can_promote_members",
                        "can_manage_video_chats", "can_manage_chat")})())
                elif me.status == enums.ChatMemberStatus.ADMINISTRATOR:
                    e.admin_rights = AdminRights(getattr(me, "privileges", None))
            except Exception:
                pass
        return e

    async def get_permissions(self, entity, user=None):
        peer = _peer(entity)
        mem = await self._c.get_chat_member(peer, _peer(user) if user is not None else "me")

        class P:
            is_admin = mem.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER)
            is_creator = mem.status == enums.ChatMemberStatus.OWNER
            is_banned = mem.status == enums.ChatMemberStatus.BANNED
            has_default_permissions = True
            participant = mem
        return P

    # ---------- ارسال
    async def send_message(self, entity, message="", *, reply_to=None, parse_mode=None, link_preview=None,
                           file=None, buttons=None, silent=None, schedule=None, **kw):
        if isinstance(message, Msg):
            if message.media:
                return await self.send_file(entity, message.media, caption=message.text, reply_to=reply_to)
            message = message.text
        if file is not None:
            return await self.send_file(entity, file, caption=message, reply_to=reply_to,
                                        parse_mode=parse_mode, silent=silent)
        kwargs = {"parse_mode": _pm(parse_mode)}
        if link_preview is not None:
            kwargs["disable_web_page_preview"] = not link_preview
        if silent:
            kwargs["disable_notification"] = True
        rid = _rid(reply_to)
        if rid:
            kwargs["reply_to_message_id"] = rid
        m = await _flood(self._c.send_message, _peer(entity), _txt(message), **kwargs)
        return Msg(self, m)

    async def send_file(self, entity, file, *, caption=None, reply_to=None, parse_mode=None, force_document=False,
                        voice_note=False, video_note=False, supports_streaming=False, silent=None, thumb=None,
                        attributes=None, link_preview=None, progress_callback=None, allow_cache=True,
                        buttons=None, **kw):
        peer = _peer(entity)
        rid = _rid(reply_to)
        common = {}
        if silent:
            common["disable_notification"] = True
        if rid:
            common["reply_to_message_id"] = rid
        cap = {"caption": _txt(caption), "parse_mode": _pm(parse_mode)}
        if isinstance(file, (list, tuple)):
            from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaDocument
            media = []
            for i, f in enumerate(file):
                k = _kind_of(f if isinstance(f, str) else getattr(f, "name", "x.bin"), force_document)
                c0 = _txt(caption) if i == 0 else ""
                media.append({"photo": InputMediaPhoto, "video": InputMediaVideo}.get(k, InputMediaDocument)(f, caption=c0))
            res = await _flood(self._c.send_media_group, peer, media, **common)
            return [Msg(self, m) for m in res]
        if isinstance(file, Msg):
            file = file.media
        if isinstance(file, MediaRef):
            m = await _flood(self._c.copy_message, peer, file._m.chat.id, file._m.id, caption=_txt(caption),
                             parse_mode=cap["parse_mode"], **common)
            return Msg(self, m)
        if isinstance(file, (bytes, bytearray)):
            bio = io.BytesIO(bytes(file))
            bio.name = "file.bin"
            file = bio
        name = file if isinstance(file, str) else getattr(file, "name", "file.bin")
        if isinstance(file, str) and not file.startswith(("http://", "https://")) and not os.path.exists(file):
            # ربما file_id
            m = await _flood(self._c.send_cached_media, peer, file, caption=cap["caption"],
                             parse_mode=cap["parse_mode"], **common)
            return Msg(self, m)
        if isinstance(file, str) and file.startswith(("http://", "https://")) and \
                not os.path.splitext(file.split("?")[0])[1]:
            name = await self._guess_url_name(file)
        kind = "voice" if voice_note else "video_note" if video_note else _kind_of(name, force_document)
        if kind == "voice" and not voice_note and os.path.splitext(str(name))[1].lower() not in _VOI:
            kind = "audio"
        th = _thumb(thumb)
        if kind == "photo":
            m = await _flood(self._c.send_photo, peer, file, **cap, **common)
        elif kind == "voice":
            m = await _flood(self._c.send_voice, peer, file, **cap, **common)
        elif kind == "audio":
            extra = {"thumb": th} if th else {}
            m = await _flood(self._c.send_audio, peer, file, **cap, **extra, **common)
        elif kind == "video":
            extra = {"thumb": th} if th else {}
            m = await _flood(self._c.send_video, peer, file, supports_streaming=True, **cap, **extra, **common)
        elif kind == "video_note":
            extra = {"thumb": th} if th else {}
            m = await _flood(self._c.send_video_note, peer, file, **extra, **common)
        elif kind == "animation":
            m = await _flood(self._c.send_animation, peer, file, **cap, **common)
        elif kind == "sticker":
            m = await _flood(self._c.send_sticker, peer, file, **common)
        else:
            extra = {"thumb": th} if th else {}
            m = await _flood(self._c.send_document, peer, file, **cap, **extra, **common)
        return Msg(self, m)

    async def _guess_url_name(self, url):
        def head():
            import requests
            try:
                ct = requests.head(url, timeout=8, allow_redirects=True).headers.get("content-type", "")
            except Exception:
                return "x.bin"
            return "x" + (mimetypes.guess_extension(ct.split(";")[0].strip()) or ".bin")
        return await asyncio.get_event_loop().run_in_executor(None, head)

    async def upload_file(self, file, *a, **k):
        return file

    # ---------- حذف / توجيه / قراءة
    async def delete_messages(self, entity, message_ids, *, revoke=True):
        ids = message_ids if isinstance(message_ids, (list, tuple, set)) else [message_ids]
        ids = [_rid(i) for i in ids if i is not None]
        peer = _peer(entity)
        n = 0
        for i in range(0, len(ids), 100):
            try:
                n += await _flood(self._c.delete_messages, peer, ids[i:i + 100], revoke=revoke) or 0
            except TypeError:
                n += await _flood(self._c.delete_messages, peer, ids[i:i + 100]) or 0
        return n

    async def forward_messages(self, entity, messages, from_peer=None, *, silent=None, **kw):
        single = not isinstance(messages, (list, tuple))
        ms = [messages] if single else list(messages)
        if from_peer is None and ms and isinstance(ms[0], Msg):
            from_peer = ms[0].chat_id
        ids = [_rid(x) for x in ms]
        res = await _flood(self._c.forward_messages, _peer(entity), _peer(from_peer), ids,
                           disable_notification=bool(silent))
        res = res if isinstance(res, list) else [res]
        out = [Msg(self, m) for m in res]
        return out[0] if single else out

    async def send_read_acknowledge(self, entity, message=None, **kw):
        try:
            await self._c.read_chat_history(_peer(entity))
        except Exception:
            pass
        return True

    async def pin_message(self, entity, message=None, *, notify=False):
        await self._c.pin_chat_message(_peer(entity), _rid(message), disable_notification=not notify)

    async def unpin_message(self, entity, message=None, **kw):
        if message is None:
            await self._c.unpin_all_chat_messages(_peer(entity))
        else:
            await self._c.unpin_chat_message(_peer(entity), _rid(message))

    async def kick_participant(self, entity, user):
        peer, uid = _peer(entity), _peer(user)
        await self._c.ban_chat_member(peer, uid)
        await self._c.unban_chat_member(peer, uid)

    # ---------- قراءة الرسائل
    async def iter_messages(self, entity, limit=None, *, search=None, from_user=None, filter=None, min_id=0,
                            max_id=0, offset_id=0, reverse=False, ids=None, wait_time=None, **kw):
        peer = _peer(entity)
        items = []
        if ids is not None:
            lst = ids if isinstance(ids, (list, tuple)) else [ids]
            res = await self._c.get_messages(peer, [_rid(i) for i in lst])
            for m in (res if isinstance(res, list) else [res]):
                if m is not None and not getattr(m, "empty", False):
                    yield Msg(self, m)
            return
        if search or from_user or filter:
            flt = getattr(filter, "f", filter) if filter is not None else enums.MessagesFilter.EMPTY
            args = dict(query=search or "", filter=flt or enums.MessagesFilter.EMPTY, limit=limit or 0)
            if from_user:
                args["from_user"] = _peer(from_user)
            agen = self._c.search_messages(peer, **args)
        else:
            agen = self._c.get_chat_history(peer, limit=limit or 0, offset_id=offset_id or 0)
        count = 0
        async for m in agen:
            if min_id and m.id <= min_id:
                if reverse:
                    continue
                break
            if max_id and m.id >= max_id:
                continue
            if reverse:
                items.append(m)
            else:
                yield Msg(self, m)
                count += 1
                if limit and count >= limit:
                    return
        for m in reversed(items):
            yield Msg(self, m)

    async def get_messages(self, entity, limit=None, *, ids=None, search=None, from_user=None, filter=None, **kw):
        if ids is not None:
            res = await self._c.get_messages(_peer(entity), [_rid(i) for i in ids] if isinstance(ids, (list, tuple)) else _rid(ids))
            if isinstance(res, list):
                return [Msg(self, m) for m in res if m is not None and not getattr(m, "empty", False)]
            return Msg(self, res) if res is not None and not getattr(res, "empty", False) else None
        return _TotalList([m async for m in self.iter_messages(entity, limit, search=search, from_user=from_user, filter=filter)])

    # ---------- الاعضاء
    async def iter_participants(self, entity, limit=None, *, search="", filter=None, aggressive=False, **kw):
        args = {"limit": limit or 0}
        if filter is not None and getattr(filter, "f", None) is not None:
            args["filter"] = filter.f
        if search:
            args["query"] = search
        async for m in self._c.get_chat_members(_peer(entity), **args):
            if m.user is None:
                continue
            e = _Ent(m.user)
            e.participant = m
            yield e

    async def get_participants(self, entity, limit=None, **kw):
        out = []
        async for u in self.iter_participants(entity, limit, **kw):
            out.append(u)
        return out

    async def iter_dialogs(self, limit=None, **kw):
        async for d in self._c.get_dialogs(limit=limit or 0):
            yield _Dialog(d)

    async def get_dialogs(self, limit=None, **kw):
        return [d async for d in self.iter_dialogs(limit)]

    # ---------- تنزيل
    async def download_media(self, message, file=None, *, thumb=None, progress_callback=None, **kw):
        obj = message
        if isinstance(obj, Msg):
            obj = obj._m
        elif isinstance(obj, MediaRef):
            obj = obj._m
        if file is bytes:
            bio = await self._c.download_media(obj, in_memory=True)
            return bio.getvalue() if bio else None
        fn = None
        if isinstance(file, (str, os.PathLike)):
            fn = str(file)
            if os.path.isdir(fn) and not fn.endswith("/"):
                fn += "/"
        else:
            fn = TMP_DOWNLOAD_DIRECTORY
        os.makedirs(os.path.dirname(fn) or ".", exist_ok=True)
        return await self._c.download_media(obj, file_name=fn)

    async def download_file(self, media, file=None, **kw):
        return await self.download_media(media, file)

    async def fast_download_file(self, location, out=None, progress_callback=None, **kw):
        return await self.download_media(location, out)

    async def fast_upload_file(self, file, *a, **k):
        return file

    async def get_profile_photos(self, entity, limit=None, **kw):
        out = _PhotoList()
        try:
            async for p in self._c.get_chat_photos(_peer(entity), limit=limit or 0):
                out.append(p)
        except Exception:
            pass
        out.total = len(out)
        return out

    async def download_profile_photo(self, entity, file=None, *, download_big=True, **kw):
        try:
            ch = await self._c.get_chat(_peer(entity))
        except Exception:
            return None
        if not getattr(ch, "photo", None):
            return None
        fid = ch.photo.big_file_id if download_big else ch.photo.small_file_id
        fn = str(file) if file else TMP_DOWNLOAD_DIRECTORY
        os.makedirs(os.path.dirname(fn) or ".", exist_ok=True)
        return await self._c.download_media(fid, file_name=fn)

    # ---------- اخرى
    def action(self, entity, action):
        return _Action(self, _peer(entity), action)

    def conversation(self, entity, timeout=60, **kw):
        return _Conv(self, entity, timeout)

    async def inline_query(self, bot_, query="", *, entity=None, offset=None, geo_point=None):
        res = await self._c.get_inline_bot_results(_peer(bot_), query)
        return [_InlineItem(self, res.query_id, x) for x in res.results]

    async def get_admin_log(self, *a, **k):
        raise NotImplementedError

    def _parse_message_text(self, message, parse_mode):
        return message, []


def _cli(c):
    return CClient.of(c)


# ═════════════════════════ مسجّل الأوامر (admin_cmd / zahid) ═════════════════════════
_GROUP = itertools.count(2000)


def _build_rx(pattern):
    if pattern is None:
        return None
    p = pattern
    if p.startswith("\\#") or p.startswith("^"):
        return re.compile(p)
    if p.startswith("\\."):
        p = p[2:]
    elif p.startswith(".") and len(p) > 1 and p[1] not in "*+?":
        p = p[1:]
    return re.compile(r"^\." + p)


class CmdSpec:
    def __init__(self, pattern=None, command=None, **kw):
        self.pattern = pattern
        self.kw = kw
        self.rx = _build_rx(pattern)


def admin_cmd(pattern=None, command=None, **kw):
    return CmdSpec(pattern, command, **kw)


sudo_cmd = admin_cmd


class _EvKind:
    def __init__(self, name):
        self.name = name

    def __call__(self, *a, **k):
        return self


class events:
    NewMessage = _EvKind("NewMessage")
    MessageEdited = _EvKind("MessageEdited")
    ChatAction = _EvKind("ChatAction")
    CallbackQuery = _EvKind("CallbackQuery")
    InlineQuery = _EvKind("InlineQuery")

    class StopPropagation(Exception):
        pass


CallbackQuery = events.CallbackQuery
InlineQuery = events.InlineQuery


def _make_filter(spec):
    kw = spec.kw
    parts = []
    if spec.rx is not None:
        parts.append(filters.regex(spec.rx))
    incoming = bool(kw.get("incoming"))
    if incoming and not kw.get("outgoing"):
        parts.append(filters.incoming & ~filters.me)
    elif kw.get("outgoing", spec.rx is not None) or spec.rx is not None:
        parts.append(filters.me)
    if kw.get("groups_only"):
        parts.append(filters.group)
    if kw.get("private_only"):
        parts.append(filters.private)
    fn = kw.get("func")
    if fn is not None:
        async def _f(_, c, m):
            try:
                ev = Ev(CClient.of(c), m)
                v = fn(ev)
                if inspect.isawaitable(v):
                    v = await v
                return bool(v)
            except Exception:
                return False
        parts.append(filters.create(_f))
    if not parts:
        parts.append(filters.me)
    flt = parts[0]
    for p in parts[1:]:
        flt = flt & p
    return flt


_ONLINE_TS = [0.0]


async def _presence(client, message):
    """يظهر "يكتب ..." في المحادثة ويجعل الحساب متصل عند كتابة أي أمر."""
    try:
        await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    except Exception:
        pass
    now = time.time()
    if now - _ONLINE_TS[0] > 15:
        _ONLINE_TS[0] = now
        try:
            from pyrogram.raw import functions as _rf
            await client.invoke(_rf.account.UpdateStatus(offline=False))
        except Exception:
            pass


def _register(fn, spec, kind="message"):
    flt = _make_filter(spec)
    private_only, groups_only = spec.kw.get("private_only"), spec.kw.get("groups_only")

    async def handler(client, message):
        match = None
        ms = getattr(message, "matches", None)
        if ms:
            match = ms[0]
        ev = Ev(CClient.of(client), message, match)
        if spec.rx is not None and getattr(message, "outgoing", False):
            asyncio.ensure_future(_presence(client, message))
        IN_HANDLER.set(True)
        try:
            await fn(ev)
        except (_perr.MessageNotModified,):
            pass
        except Exception as e:
            if e.__class__.__name__ in ("StopPropagation", "ContinuePropagation"):
                raise
            traceback.print_exc()
            if spec.rx is not None:
                try:
                    await ev.edit(f"**🝳 ⦙   حدث خطأ في تنفيذ الامر :**\n`{str(e)[:300]}`")
                except Exception:
                    pass

    handler.__name__ = getattr(fn, "__name__", "h")
    g = next(_GROUP)
    handler.handlers = [(MessageHandler(handler, flt), g)]
    mod = sys.modules.get(getattr(fn, "__module__", None))
    if mod is not None:
        setattr(mod, f"_arab_h{g}", handler)
    return fn


class _Zahid:
    @property
    def uid(self):
        me = getattr(app, "me", None)
        return me.id if me else sudo_id

    tgbot = None

    def on(self, spec=None, **kw):
        if not isinstance(spec, CmdSpec):
            spec = CmdSpec(None, **kw)

        def deco(fn):
            return _register(fn, spec)
        return deco

    def iq_cmd(self, pattern=None, command=None, info=None, **kw):
        kw.setdefault("outgoing", True if pattern is not None else kw.get("outgoing", False))
        return self.on(CmdSpec(pattern, command, **kw))

    def bot_cmd(self, *a, **k):
        return lambda fn: fn

    async def __call__(self, req):
        return await CClient.of(app)(req)

    def __getattr__(self, n):
        if n.startswith("__"):
            raise AttributeError(n)
        return getattr(CClient.of(app), n)


zahid = bot_ = _Zahid()
assistant_bot = bot
bot = zahid


# ═════════════════════════ دوال مساعدة (مثل helpers عرب) ═════════════════════════
def md_to_text(md):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", _txt(md))
    return re.sub(r"(\*\*|__|~~|`)", "", t)


async def paste_message(text, pastetype="s", extension=None, markdown=True):
    import requests
    text = md_to_text(text) if markdown else text

    def go():
        try:
            k = requests.post("https://nekobin.com/api/documents", json={"content": text}, timeout=15).json()
            return "https://nekobin.com/" + k["result"]["key"]
        except Exception:
            pass
        try:
            k = requests.post("https://spaceb.in/api/v1/documents/", data={"content": text, "extension": "txt"},
                              timeout=15).json()
            return "https://spaceb.in/" + k["payload"]["id"]
        except Exception:
            return None
    return await asyncio.get_event_loop().run_in_executor(None, go)


async def edit_or_reply(event, text, parse_mode=None, link_preview=None, file_name=None, aslink=False,
                        deflink=False, noformat=False, linktext=None, caption=None):
    text = _txt(text)
    link_preview = link_preview or False
    if len(text) < 4096 and not deflink:
        await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)
        return event
    if not noformat:
        text = md_to_text(text)
    if aslink or deflink:
        url = await paste_message(text, markdown=False)
        if url:
            await event.edit((linktext or "الرسالة طويلة جدا فتم رفعها") + f" [هنا]({url})", link_preview=link_preview)
            return event
    file_name = file_name or "output.txt"
    with open(file_name, "w+", encoding="utf-8") as f:
        f.write(text)
    await event.client.send_file(event.chat_id, file_name, caption=caption)
    await event.delete()
    os.remove(file_name)


async def edit_delete(event, text, time=None, parse_mode=None, link_preview=None):
    time = time or 5
    e = await event.edit(text, parse_mode=parse_mode, link_preview=link_preview or False)
    await asyncio.sleep(time)
    try:
        await (e or event).delete()
    except Exception:
        pass
    return e


edit_delere = ed = edit_delete


async def eor(event, text, parse_mode=None, link_preview=None, file_name=None, aslink=False, linktext=None, caption=None, time=None, **kw):
    r_ = await edit_or_reply(event, text, parse_mode, link_preview, file_name, aslink, False, False, linktext, caption)
    if time:
        await asyncio.sleep(time)
        try:
            await event.delete()
        except Exception:
            pass
    return r_


eod = edit_delete


async def reply_id(event):
    return event.reply_to_msg_id


rd = reply_id


async def get_user_from_event(event, catevent=None, secondgroup=None, nogroup=False, noedits=False):
    catevent = catevent or event
    args, extra = [], None
    grp = ""
    if nogroup is False:
        try:
            grp = event.pattern_match.group(2 if secondgroup else 1) or ""
        except Exception:
            grp = ""
        args = grp.strip().split(" ", 1) if grp.strip() else []
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-") and user[1:].isnumeric()):
                user = int(user)
            for e in event.entities:
                if isinstance(e, MessageEntityMentionName):
                    return await event.client.get_entity(e.user_id), extra
                break
            if isinstance(user, int) or user.startswith("@"):
                return await event.client.get_entity(user), extra
    except Exception:
        pass
    try:
        if nogroup is False:
            extra = grp
        if event.is_private:
            return await event.client.get_entity(event.chat_id), extra
        if event.reply_to_msg_id:
            prev = await event.get_reply_message()
            if prev is None or prev.sender_id is None:
                if not noedits:
                    await edit_delete(catevent, "حسنًا ، هذا مسؤول مجهول")
                return None, None
            return await event.client.get_entity(prev.sender_id), extra
        elif not args:
            if not noedits:
                await edit_delete(catevent, "قم بوضع اسم المستخدم أو معرف المستخدم أو الرد!", 5)
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(catevent, "قم بوضع اسم المستخدم أو معرف المستخدم أو الرد!")
    return None, None


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None


def humanbytes(size):
    if size is None or isinstance(size, str):
        return ""
    power, n = 2 ** 10, 0
    names = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power and n < 4:
        size /= power
        n += 1
    return f"{round(size, 2)} {names[n]}B"


hb = humanbytes


def time_formatter(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    parts = [f"{days} يوم" if days else "", f"{hours} ساعة" if hours else "",
             f"{minutes} دقيقة" if minutes else "", f"{seconds} ثانية" if seconds else ""]
    return ", ".join(p for p in parts if p) or "0 ثانية"


async def get_readable_time(seconds):
    return time_formatter(seconds)


def readable_time(seconds):
    return time_formatter(seconds)


async def extract_time(cat, time_val):
    if any(time_val.endswith(u) for u in "smhdw"):
        unit, num = time_val[-1], time_val[:-1]
        if not num.isdigit():
            await cat.edit("مقدار الوقت غير صحيح")
            return None
        mult = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}[unit]
        return int(time.time() + int(num) * mult)
    await cat.edit("نوع الوقت غير صحيح، المتوقع s او m او h او d او w")
    return None


def char_is_emoji(character):
    return ord(character) > 0x2000 and not character.isalnum()


def deEmojify(inputString):
    return re.sub("[\U00010000-\U0010ffff\u2600-\u27bf\ufe0f\u200d]", "", _txt(inputString))


def yaml_format(obj, indent=0, **kw):
    try:
        return json.dumps(obj if isinstance(obj, (dict, list)) else getattr(obj, "__dict__", str(obj)),
                          ensure_ascii=False, indent=2, default=str)
    except Exception:
        return str(obj)


def parse_pre(text):
    return text.strip(), []


class _format:
    @staticmethod
    def mentionuser(name, userid):
        return f"[{name}](tg://user?id={userid})"

    @staticmethod
    def htmlmentionuser(name, userid):
        return f"<a href='tg://user?id={userid}'>{name}</a>"

    @staticmethod
    def paste_text(*a, **k):
        return None


class _catutils(_format):
    @staticmethod
    async def runcmd(cmd):
        return await runcmd(cmd)

    @staticmethod
    async def bash(cmd):
        return await bash(cmd)

    @staticmethod
    async def unsavegif(event, sandy):
        return None

    @staticmethod
    async def media_to_pic(*a, **k):
        return None

    @staticmethod
    async def run_async(*a, **k):
        return None


_cattools = _catutils


async def install_pip(pipfile):
    if not (sys.executable and os.path.isfile(sys.executable)):
        return False  # اندرويد: لا يوجد pip وقت التشغيل؛ المكتبات تُضمَّن عند بناء التطبيق
    p = await asyncio.create_subprocess_exec(sys.executable, "-m", "pip", "install", pipfile,
                                             stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    await p.communicate()
    return p.returncode == 0


_YT_LOCK = __import__("threading").Lock()


def _is_ytdlp(args):
    """هل الامر هو 'python -m yt_dlp ...' ولا يوجد مفسّر بايثون حقيقي (اندرويد)؟"""
    return (len(args) >= 3 and args[1:3] == ["-m", "yt_dlp"]
            and not (args[0] and os.path.isfile(args[0])))


def _ytdlp_inproc(argv):
    import contextlib
    import io
    import yt_dlp
    out, err = io.StringIO(), io.StringIO()
    code = 0
    with _YT_LOCK, contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            yt_dlp.main(argv)
        except SystemExit as e:
            if isinstance(e.code, int):
                code = e.code
            elif e.code:
                err.write(str(e.code))
                code = 1
        except Exception as e:
            err.write(f"ERROR: {e}")
            code = 1
    # التحذيرات (مثل غياب ffmpeg) ليست اخطاء؛ الاوامر تعتبر اي stderr خطأ
    errs = "\n".join(l for l in err.getvalue().splitlines() if not l.startswith("WARNING"))
    return out.getvalue().strip(), errs.strip(), code, 0


async def runcmd(cmd):
    args = shlex.split(cmd)
    if _is_ytdlp(args):
        return await asyncio.get_event_loop().run_in_executor(None, _ytdlp_inproc, args[3:])
    p = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, err = await p.communicate()
    return out.decode("utf-8", "replace").strip(), err.decode("utf-8", "replace").strip(), p.returncode, p.pid


async def bash(cmd):
    try:
        args = shlex.split(cmd)
    except ValueError:
        args = []
    if _is_ytdlp(args):
        o, e, _, _ = await asyncio.get_event_loop().run_in_executor(None, _ytdlp_inproc, args[3:])
        return o, e
    p = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, err = await p.communicate()
    return out.decode("utf-8", "replace").strip(), err.decode("utf-8", "replace").strip()


async def take_screen_shot(video_file, duration, path=""):
    out = path or os.path.join(TMP_DOWNLOAD_DIRECTORY, f"{os.path.basename(video_file)}.jpg")
    await runcmd(f"ffmpeg -y -ss {duration} -i {shlex.quote(video_file)} -vframes 1 {shlex.quote(out)}")
    return out if os.path.exists(out) else None


async def progress(*a, **k):
    return None


def is_admin_sync(*a):
    return False


async def is_admin(client, chat_id, userid):
    try:
        m = await CClient.of(app)._c.get_chat_member(chat_id, userid)
        return m.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER)
    except Exception:
        return False


def check_data_base_heal_th():
    return True, "JSON"


def get_tz(country):
    try:
        import pytz
        return pytz.timezone(country)
    except Exception:
        return None


class pool:
    @staticmethod
    async def run_in_thread(f):
        def deco(*a, **k):
            return asyncio.get_event_loop().run_in_executor(None, lambda: f(*a, **k))
        return deco


# ═════════════════════════ الازرار وصلاحيات تيليثون ═════════════════════════
class Button:
    @staticmethod
    def inline(text, data=None, *a, **k):
        return ("inline", text, data)

    @staticmethod
    def url(text, url=None, *a, **k):
        return ("url", text, url)


class ChatBannedRights:
    def __init__(self, until_date=None, view_messages=False, send_messages=False, send_media=False,
                 send_stickers=False, send_gifs=False, send_games=False, send_inline=False, embed_links=False,
                 send_polls=False, change_info=False, invite_users=False, pin_messages=False, **kw):
        self.__dict__.update(locals())
        self.__dict__.pop("self", None)
        self.__dict__.pop("kw", None)


class ChatAdminRights:
    def __init__(self, change_info=None, post_messages=None, edit_messages=None, delete_messages=None,
                 ban_users=None, invite_users=None, pin_messages=None, add_admins=None, anonymous=None,
                 manage_call=None, other=None, **kw):
        self.__dict__.update(locals())
        self.__dict__.pop("self", None)
        self.__dict__.pop("kw", None)


async def restrict_user(cli, chat, user, rights):
    """يطبق ChatBannedRights على مستخدم (حظر/تقييد/فك)."""
    from pyrogram.types import ChatPermissions
    c = cli._c
    chat, user = _peer(chat), _peer(user)
    until = rights.until_date
    if rights.view_messages:
        await c.ban_chat_member(chat, user, **({"until_date": until} if until else {}))
        return
    allow_all = not any([rights.send_messages, rights.send_media, rights.send_stickers, rights.send_gifs,
                         rights.send_games, rights.send_inline, rights.embed_links, rights.send_polls])
    if allow_all:
        try:
            await c.unban_chat_member(chat, user)
        except Exception:
            pass
        try:
            await c.restrict_chat_member(chat, user, ChatPermissions(
                can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True,
                can_send_polls=True, can_add_web_page_previews=True, can_invite_users=True,
                can_pin_messages=True, can_change_info=True))
        except Exception:
            pass
        return
    perms = ChatPermissions(can_send_messages=not rights.send_messages,
                            can_send_media_messages=not rights.send_media,
                            can_send_other_messages=not (rights.send_stickers or rights.send_gifs or rights.send_games),
                            can_send_polls=not rights.send_polls,
                            can_add_web_page_previews=not rights.embed_links)
    await c.restrict_chat_member(chat, user, perms, **({"until_date": until} if until else {}))


class EditBannedRequest:
    def __init__(self, channel, participant, banned_rights):
        self.a = (channel, participant, banned_rights)

    async def _run(self, cli):
        await restrict_user(cli, *self.a)


class EditAdminRequest:
    def __init__(self, channel, user_id, admin_rights, rank=""):
        self.a = (channel, user_id, admin_rights, rank)

    async def _run(self, cli):
        from pyrogram.types import ChatPrivileges
        ch, uid, ar, rank = self.a
        g = lambda n: bool(getattr(ar, n, False))
        any_right = any(g(n) for n in ("change_info", "post_messages", "edit_messages", "delete_messages",
                                       "ban_users", "invite_users", "pin_messages", "add_admins", "manage_call"))
        if not any_right:
            await cli._c.promote_chat_member(_peer(ch), _peer(uid), ChatPrivileges(
                can_manage_chat=False, can_delete_messages=False, can_manage_video_chats=False,
                can_restrict_members=False, can_promote_members=False, can_change_info=False,
                can_invite_users=False, can_post_messages=False, can_edit_messages=False, can_pin_messages=False))
            return
        await cli._c.promote_chat_member(_peer(ch), _peer(uid), ChatPrivileges(
            can_manage_chat=True, can_delete_messages=g("delete_messages"),
            can_manage_video_chats=g("manage_call"), can_restrict_members=g("ban_users"),
            can_promote_members=g("add_admins"), can_change_info=g("change_info"),
            can_invite_users=g("invite_users"), can_post_messages=g("post_messages"),
            can_edit_messages=g("edit_messages"), can_pin_messages=g("pin_messages")))
        if rank:
            try:
                await cli._c.set_administrator_title(_peer(ch), _peer(uid), rank)
            except Exception:
                pass


class UnblockRequest:
    def __init__(self, id):
        self.id = id

    async def _run(self, cli):
        return await cli._c.unblock_user(_peer(self.id))


class _Full:
    pass


class GetFullUserRequest:
    def __init__(self, id):
        self.id = id

    async def _run(self, cli):
        ch = await cli._c.get_chat(_peer(self.id))
        f = _Full()
        f.about = getattr(ch, "bio", None)
        try:
            f.common_chats_count = len(await cli._c.get_common_chats(_peer(self.id)))
        except Exception:
            f.common_chats_count = 0
        f.private_forward_name = None
        res = _Full()
        res.full_user = f
        res.user = _Ent(ch)
        res.users = [res.user]
        return res


class JoinChannelRequest:
    """لا ينفّذ شيئاً: اوامر عرب الاصلية تنضم تلقائياً لقناة الدعم عند التنفيذ، وهذا السلوك غير منقول."""

    def __init__(self, channel=None):
        self.channel = channel

    async def _run(self, cli):
        return None


class ImportChatInviteRequest(JoinChannelRequest):
    def __init__(self, hash=None):
        self.hash = hash


Get = ImportChatInviteRequest


class functions:  # نفس مسارات telethon.tl.functions المستخدمة
    class _NS:
        pass
    account = _NS()
    channels = _NS()
    messages = _NS()
    contacts = _NS()
    photos = _NS()
    users = _NS()


types = type("types", (), {})()


borg = zahid


class _LazyTelegraph:
    """نسخة كسولة من Telegraph (تنشئ الحساب عند اول استخدام)."""

    def __init__(self, short_name=None):
        self._sn = short_name or "zahid"
        self._t = None

    def _get(self):
        if self._t is None:
            from telegraph import Telegraph
            self._t = Telegraph()
            self._t.create_account(short_name=self._sn)
        return self._t

    def __getattr__(self, n):
        return getattr(self._get(), n)


# ═════════════════════════ طلبات Telethon الاضافية ═════════════════════════
class _Req:
    """أساس لطلب Telethon: يخزّن المعاملات وينفّذ _run(cli)."""
    _fields = ()

    def __init__(self, *a, **k):
        for n, v in zip(self._fields, a):
            setattr(self, n, v)
        for n, v in k.items():
            setattr(self, n, v)


class UpdateProfileRequest(_Req):
    _fields = ("first_name", "last_name", "about")

    async def _run(self, cli):
        kw = {}
        for n in self._fields:
            v = getattr(self, n, None)
            if v is not None:
                kw[n] = v
        if kw:
            await cli._c.update_profile(**kw)
        return True


class BlockRequest(_Req):
    _fields = ("id",)

    async def _run(self, cli):
        return await cli._c.block_user(_peer(self.id))


class GetBlockedRequest(_Req):
    _fields = ("offset", "limit")

    async def _run(self, cli):
        from pyrogram import raw
        res = await cli._c.invoke(raw.functions.contacts.GetBlocked(offset=getattr(self, "offset", 0) or 0,
                                                                    limit=getattr(self, "limit", 1000) or 1000))
        out = _Full()
        out.blocked = []
        for b in getattr(res, "blocked", []):
            o = _Full()
            o.peer_id = _Full()
            o.peer_id.user_id = getattr(b.peer_id, "user_id", None)
            out.blocked.append(o)
        return out


class DeletePhotosRequest(_Req):
    _fields = ("id",)

    async def _run(self, cli):
        ids = [getattr(p, "file_id", p) for p in (self.id if isinstance(self.id, (list, tuple)) else [self.id])]
        ids = [i for i in ids if isinstance(i, str)]
        if ids:
            await cli._c.delete_profile_photos(ids)
        return True


class UploadProfilePhotoRequest(_Req):
    _fields = ("file",)

    async def _run(self, cli):
        await cli._c.set_profile_photo(photo=self.file)
        return True


class GetPrivacyRequest(_Req):
    _fields = ("key",)

    async def _run(self, cli):
        o = _Full()
        o.rules = []
        return o


class InputPrivacyKeyStatusTimestamp:
    pass


class PrivacyValueAllowAll:
    pass


class EditTitleRequest(_Req):
    _fields = ("channel", "title")

    async def _run(self, cli):
        await cli._c.set_chat_title(_peer(self.channel), self.title)


class InviteToChannelRequest(_Req):
    _fields = ("channel", "users")

    async def _run(self, cli):
        users = [_peer(u) for u in self.users]
        await cli._c.add_chat_members(_peer(self.channel), users)


class GetParticipantRequest(_Req):
    _fields = ("channel", "participant")

    async def _run(self, cli):
        mem = await cli._c.get_chat_member(_peer(self.channel), _peer(self.participant))
        o = _Full()
        o.participant = mem
        return o


class GetAdminedPublicChannelsRequest(_Req):
    async def _run(self, cli):
        from pyrogram import raw
        res = await cli._c.invoke(raw.functions.channels.GetAdminedPublicChannels())
        o = _Full()
        o.chats = res.chats
        return o


class UpdateUsernameRequest(_Req):
    _fields = ("username",)

    async def _run(self, cli):
        ok = await cli._c.set_username(self.username or None)
        return ok


class GetUserPhotosRequest(_Req):
    _fields = ("user_id", "offset", "max_id", "limit")

    async def _run(self, cli):
        photos = await cli.get_profile_photos(self.user_id, limit=getattr(self, "limit", 80))
        o = _Full()
        o.photos = list(photos)
        o.count = len(photos)
        return o


class InputChatPhotoEmpty:
    pass


class EditPhotoRequest(_Req):
    _fields = ("channel", "photo")

    async def _run(self, cli):
        if isinstance(self.photo, InputChatPhotoEmpty):
            await cli._c.delete_chat_photo(_peer(self.channel))
        else:
            await cli._c.set_chat_photo(_peer(self.channel), photo=self.photo)


class EditChatDefaultBannedRightsRequest(_Req):
    _fields = ("peer", "banned_rights")

    async def _run(self, cli):
        from pyrogram.types import ChatPermissions
        r_ = self.banned_rights
        perms = ChatPermissions(can_send_messages=not r_.send_messages,
                                can_send_media_messages=not r_.send_media,
                                can_send_other_messages=not (r_.send_stickers or r_.send_gifs or r_.send_games or r_.send_inline),
                                can_send_polls=not r_.send_polls,
                                can_add_web_page_previews=not r_.embed_links,
                                can_change_info=not r_.change_info,
                                can_invite_users=not r_.invite_users,
                                can_pin_messages=not r_.pin_messages)
        await cli._c.set_chat_permissions(_peer(self.peer), perms)


class ExportChatInviteRequest(_Req):
    _fields = ("peer",)

    async def _run(self, cli):
        link = await cli._c.export_chat_invite_link(_peer(self.peer))
        o = _Full()
        o.link = link
        return o


class SaveDraftRequest(_Req):
    _fields = ("peer", "message")

    async def _run(self, cli):
        return True


class GetFullChatRequest(_Req):
    _fields = ("chat_id",)

    async def _run(self, cli):
        ch = await cli._c.get_chat(self.chat_id if isinstance(self.chat_id, int) and self.chat_id < 0 else -abs(int(self.chat_id)))
        f = _Full()
        f.about = ch.description
        f.participants = _Full()
        f.participants.participants = []
        f.participants_count = ch.members_count
        f.exported_invite = _Full()
        f.exported_invite.link = getattr(ch, "invite_link", None)
        res = _Full()
        res.full_chat = f
        res.chats = [_Ent(ch)]
        res.users = []
        return res


class GetFullChannelRequest(GetFullChatRequest):
    _fields = ("channel",)

    async def _run(self, cli):
        ch = await cli._c.get_chat(_peer(self.channel))
        f = _Full()
        f.about = ch.description
        f.participants_count = ch.members_count
        f.admins_count = None
        f.kicked_count = None
        f.banned_count = None
        f.online_count = None
        f.slowmode_seconds = getattr(ch, "slow_mode_delay", None)
        f.linked_chat_id = getattr(getattr(ch, "linked_chat", None), "id", None)
        f.exported_invite = _Full()
        f.exported_invite.link = getattr(ch, "invite_link", None)
        f.call = None
        res = _Full()
        res.full_chat = f
        res.chats = [_Ent(ch)]
        res.users = []
        return res


class UpdateNotifySettingsRequest(_Req):
    async def _run(self, cli):
        return True


class GetStickerSetRequest(_Req):
    async def _run(self, cli):
        raise NotImplementedError("حزم الملصقات تُدار بمحادثة @Stickers")


class InputStickerSetID(_Req):
    _fields = ("id", "access_hash")


class DocumentAttributeFilename(_Req):
    _fields = ("file_name",)


class DocumentAttributeSticker(_Req):
    _fields = ("alt", "stickerset")


class DocumentAttributeAudio(_Req):
    pass


class InputPhoto(_Req):
    _fields = ("id", "access_hash", "file_reference")


class SendMediaRequest(_Req):
    async def _run(self, cli):
        raise NotImplementedError


class GetParticipantsRequest(_Req):
    async def _run(self, cli):
        raise NotImplementedError


class GetHistoryRequest(_Req):
    async def _run(self, cli):
        raise NotImplementedError


class UserStatusOnline: ...
class UserStatusOffline: ...
class UserStatusRecently: ...
class UserStatusLastWeek: ...
class UserStatusLastMonth: ...
class UserStatusEmpty: ...


def pack_bot_file_id(media):
    m = getattr(media, "_m", None)
    f = _FileInfo(m) if m is not None else None
    return f.id if f else None


def get_input_location(photo):
    raise ValueError("غير مدعوم")


def get_attributes(*a, **k):
    return [], None


async def make_gif(event, reply, quality=None, fps=None):
    """يحوّل فيديو/ملصق متحرك الى gif (ffmpeg)."""
    path = await event.client.download_media(reply, TMP_DOWNLOAD_DIRECTORY)
    if not path:
        return None
    out = os.path.splitext(path)[0] + ".gif"
    await runcmd(f"ffmpeg -y -i {shlex.quote(path)} -vf fps={fps or 15},scale=480:-1 {shlex.quote(out)}")
    return out if os.path.exists(out) else None


def spin_frames_dummy():
    pass


# ربط الطلبات داخل مساحة functions.*
for _n in ("UpdateProfileRequest", "GetPrivacyRequest"):
    setattr(functions.account, _n, globals()[_n])
functions.account.GetPasswordRequest = type("GetPasswordRequest", (_Req,), {})
for _n in ("BlockRequest", "UnblockRequest", "GetBlockedRequest"):
    setattr(functions.contacts, _n, globals()[_n])
for _n in ("DeletePhotosRequest", "UploadProfilePhotoRequest", "GetUserPhotosRequest"):
    setattr(functions.photos, _n, globals()[_n])
for _n in ("EditBannedRequest", "EditTitleRequest", "InviteToChannelRequest", "GetParticipantRequest",
           "EditAdminRequest", "GetFullChannelRequest", "EditPhotoRequest", "JoinChannelRequest",
           "GetAdminedPublicChannelsRequest"):
    setattr(functions.channels, _n, globals()[_n])
functions.channels.EditCreatorRequest = type("EditCreatorRequest", (_Req,), {})
for _n in ("GetStickerSetRequest", "ImportChatInviteRequest", "ExportChatInviteRequest", "SaveDraftRequest",
           "GetFullChatRequest"):
    setattr(functions.messages, _n, globals()[_n])
setattr(functions.users, "GetFullUserRequest", GetFullUserRequest)
types.InputPrivacyKeyStatusTimestamp = InputPrivacyKeyStatusTimestamp
types.PrivacyValueAllowAll = PrivacyValueAllowAll


# ═════════════════════════ دوال اضافية ═════════════════════════
def url(link):
    return bool(re.match(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", _txt(link).strip(), re.I))


def get_extension(path):
    return os.path.splitext(path)[1].lower()


logger = logging.getLogger("arab")


def is_fullsudo(user_id=None):
    return False


async def _msg_ban_time(self, text):
    m = re.fullmatch(r"(\d+)\s*([smhdw]?)", _txt(text).strip().lower())
    if not m:
        raise ValueError("bad time")
    return int(m.group(1)) * {"": 1, "s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}[m.group(2)]


Msg.ban_time = _msg_ban_time

try:
    from telegraph import Telegraph, exceptions, upload_file
except Exception:
    Telegraph = _Missing("telegraph")
    exceptions = _Missing("telegraph.exceptions")
    upload_file = _Missing("upload_file")


# ───── مترجم بديل لـ googletrans (المكتبة تتعارض مع httpx الحديثة) ─────
GT_LANGUAGES = {
    "af": "afrikaans", "sq": "albanian", "am": "amharic", "ar": "arabic", "hy": "armenian", "az": "azerbaijani",
    "eu": "basque", "be": "belarusian", "bn": "bengali", "bs": "bosnian", "bg": "bulgarian", "ca": "catalan",
    "zh-cn": "chinese (simplified)", "zh-tw": "chinese (traditional)", "hr": "croatian", "cs": "czech",
    "da": "danish", "nl": "dutch", "en": "english", "et": "estonian", "fi": "finnish", "fr": "french",
    "gl": "galician", "ka": "georgian", "de": "german", "el": "greek", "gu": "gujarati", "ht": "haitian creole",
    "iw": "hebrew", "he": "hebrew", "hi": "hindi", "hu": "hungarian", "is": "icelandic", "id": "indonesian",
    "ga": "irish", "it": "italian", "ja": "japanese", "kn": "kannada", "kk": "kazakh", "km": "khmer",
    "ko": "korean", "ku": "kurdish (kurmanji)", "ky": "kyrgyz", "lo": "lao", "la": "latin", "lv": "latvian",
    "lt": "lithuanian", "mk": "macedonian", "ms": "malay", "ml": "malayalam", "mt": "maltese", "mr": "marathi",
    "mn": "mongolian", "my": "myanmar (burmese)", "ne": "nepali", "no": "norwegian", "ps": "pashto",
    "fa": "persian", "pl": "polish", "pt": "portuguese", "pa": "punjabi", "ro": "romanian", "ru": "russian",
    "sr": "serbian", "sd": "sindhi", "si": "sinhala", "sk": "slovak", "sl": "slovenian", "so": "somali",
    "es": "spanish", "su": "sundanese", "sw": "swahili", "sv": "swedish", "tg": "tajik", "ta": "tamil",
    "te": "telugu", "th": "thai", "tr": "turkish", "uk": "ukrainian", "ur": "urdu", "uz": "uzbek",
    "vi": "vietnamese", "cy": "welsh", "yi": "yiddish", "zu": "zulu",
}


class _GTResult:
    def __init__(self, text, src, dest):
        self.text, self.src, self.dest = text, src, dest


class GTranslator:
    """نفس واجهة googletrans.Translator (translate(text, dest=...)) عبر نقطة Google العامة."""

    def translate(self, text, dest="en", src="auto"):
        import requests as _rq
        r = _rq.get("https://translate.googleapis.com/translate_a/single",
                    params={"client": "gtx", "sl": src, "tl": dest, "dt": "t", "q": text}, timeout=15)
        r.raise_for_status()
        data = r.json()
        out = "".join(part[0] for part in (data[0] or []) if part and part[0])
        detected = (data[2] if len(data) > 2 and isinstance(data[2], str) else (src if src != "auto" else "en")).lower()
        return _GTResult(out, detected, dest)


# ───── يوتيوب (yt-dlp بدل youtube-dl) ─────
_PY = shlex.quote(sys.executable or "")
song_dl = (_PY + " -m yt_dlp --force-ipv4 --embed-thumbnail -f bestaudio -x --audio-format mp3 "
           "--audio-quality {QUALITY} -o './temp/%(title)s.%(ext)s' --extract-audio {video_link}")
video_dl = (_PY + " -m yt_dlp --force-ipv4 -f 'best[height<=720]/best' --merge-output-format mp4 "
            "-o './temp/%(title)s.%(ext)s' {video_link}")
name_dl = _PY + " -m yt_dlp --force-ipv4 --get-filename -o './temp/%(title)s.%(ext)s' {video_link}"
thumb_dl = _PY + " -m yt_dlp --force-ipv4 --write-thumbnail --skip-download -o './temp/%(title)s.%(ext)s' {video_link}"


async def yt_search(query):
    loop = asyncio.get_event_loop()

    def go():
        try:
            from youtubesearchpython import VideosSearch
            res = VideosSearch(query, limit=1).result()["result"]
            if res:
                return res[0]["link"].split("&")[0]
        except Exception:
            pass
        try:
            import yt_dlp
            with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True, "extract_flat": True}) as y:
                info = y.extract_info(f"ytsearch1:{query}", download=False)
            ents = (info or {}).get("entries") or []
            if ents:
                return "https://www.youtube.com/watch?v=" + ents[0]["id"]
        except Exception:
            pass
        try:
            import urllib.request, urllib.parse
            h = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + urllib.parse.quote(query))
            ids = re.findall(r"watch\?v=(\S{11})", h.read().decode())
            if ids:
                return "https://www.youtube.com/watch?v=" + ids[0]
        except Exception:
            pass
        return "Couldnt fetch results"
    return await loop.run_in_executor(None, go)


async def ytsearch(query, limit):
    def go():
        out = ""
        try:
            from youtubesearchpython import VideosSearch
            for v in VideosSearch(query.lower(), limit=limit).result()["result"]:
                out += f"☞ [{v['title']}](https://www.youtube.com/watch?v={v['id']})\n"
                out += f"**المدة : **__{v.get('duration')}__\n\n"
            if out:
                return out
        except Exception:
            pass
        import yt_dlp  # بديل يعمل مع httpx الحديثة
        opts = {"quiet": True, "skip_download": True, "extract_flat": True}
        with yt_dlp.YoutubeDL(opts) as y:
            info = y.extract_info(f"ytsearch{int(limit)}:{query}", download=False)
        for v in (info or {}).get("entries", []) or []:
            d = v.get("duration")
            dur = f"{int(d) // 60}:{int(d) % 60:02d}" if d else "?"
            out += f"☞ [{v.get('title')}](https://www.youtube.com/watch?v={v.get('id')})\n"
            out += f"**المدة : **__{dur}__\n\n"
        return out
    return await asyncio.get_event_loop().run_in_executor(None, go)


async def yt_data(link):
    def go():
        import yt_dlp
        with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True}) as y:
            return y.extract_info(link, download=False)
    return await asyncio.get_event_loop().run_in_executor(None, go)


async def thumb_from_audio(audio_path, output):
    await runcmd(f"ffmpeg -y -i {shlex.quote(audio_path)} -filter:v scale=500:500 -an {shlex.quote(output)}")


async def sanga_seperator(sanga_list):
    sanga_list = [i for i in sanga_list if not i.startswith("🔗")]
    s = 0
    for i in sanga_list:
        if i.startswith("Username History"):
            break
        s += 1
    return sanga_list[:s], sanga_list[s:]


async def hide_inlinebot(borg_, bot_name, text, chat_id, reply_to_id, c_lick=0):
    cli = CClient.of(app)
    res = await cli.inline_query(bot_name, f"{text}.")
    m = await res[c_lick].click("me")
    if m:
        await cli.send_file(int(chat_id), m.media, reply_to=reply_to_id)
        await m.delete()


async def waifutxt(text, chat_id, reply_to_id, bot_):
    animus = [0, 1, 2, 3, 4, 9, 15, 20, 22, 27, 29, 32, 33, 34, 37, 38, 41, 42, 44, 45, 47, 48, 51, 52, 53, 55,
              56, 57, 58, 61, 62, 63]
    cli = CClient.of(app)
    res = await cli.inline_query("stickerizerbot", f"#{random.choice(animus)}{text}")
    m = await res[0].click("me")
    if m:
        await cli.send_file(int(chat_id), m.media, reply_to=reply_to_id)
        await m.delete()


def start_background():
    """يشغّل مهام الخلفية التي سجلتها الاوامر (ساعة الاسم، البايو الوقتي...)."""
    for coro in list(BACKGROUND):
        try:
            asyncio.ensure_future(coro)
        except Exception as e:
            print("background:", e)
    BACKGROUND.clear()


BACKGROUND = []


class _Loop:
    def create_task(self, coro):
        BACKGROUND.append(coro)

    def run_until_complete(self, *a):
        return None


_Zahid.loop = property(lambda self: _Loop())

try:
    from arabhelpers import *  # noqa
    from arabhelpers import emojify  # noqa
except Exception as _e:  # pragma: no cover
    print("arabhelpers:", _e)
