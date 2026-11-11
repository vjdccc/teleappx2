# -*- coding: utf-8 -*-
"""حلقة asyncio واحدة دائمة لكل التطبيق (البوت + ادوات الاستخراج).

pyrogram يربط نفسه بأول حلقة يُستورد فيها، لذلك كل شيء يجب ان يعمل على حلقة واحدة.
"""
import asyncio
import threading

_loop = None
_lock = threading.Lock()


def get_loop():
    global _loop
    with _lock:
        if _loop is None:
            ready = threading.Event()

            def run():
                global _loop
                lp = asyncio.new_event_loop()
                asyncio.set_event_loop(lp)
                _loop = lp
                ready.set()
                lp.run_forever()

            threading.Thread(target=run, name="zahid-loop", daemon=True).start()
            ready.wait()
    return _loop


def run_coro(coro, timeout=None):
    """يشغّل coroutine على الحلقة المشتركة وينتظر نتيجتها (يُستدعى من اي خيط عادي)."""
    return asyncio.run_coroutine_threadsafe(coro, get_loop()).result(timeout)
