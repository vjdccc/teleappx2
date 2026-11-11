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
    from datetime import datetime
except Exception:
    datetime = _Missing('datetime')

LOGS = logging.getLogger(__name__)
class AFK:
    def __init__(self):
        self.USERAFK_ON = {}
        self.afk_time = None
        self.last_afk_message = {}
        self.afk_star = {}
        self.afk_end = {}
        self.reason = None
        self.msg_link = False
        self.afk_type = None
        self.media_afk = None
        self.afk_on = False
sleeping = gvarstatus("OR_SLEEP") or "وضع النائم"


AFK_ = AFK()

