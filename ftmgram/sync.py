#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import functools
import inspect
import threading

from ftmgram import types, utils
from ftmgram.methods import Methods
from ftmgram.methods.utilities import idle as idle_module, compose as compose_module


# ─────────────────────────────────────────────────────────────────────────────
# Capture the main event loop ONCE at module-load time.
# This is the exact same technique used by original Pyrogram.
#
# Why this works:
#   • bot.start() and all top-level sync calls run on THIS loop
#     (via run_until_complete).
#   • Pyrogram's Session / recv_worker also run on THIS loop
#     (because they are started from within run_until_complete).
#   • Worker-thread handlers submit back to THIS loop via
#     run_coroutine_threadsafe — so every Future is created on the
#     same loop and there is ZERO "attached to a different loop" error.
# ─────────────────────────────────────────────────────────────────────────────
main_loop = utils.get_sync_loop()


def async_to_sync(obj, name):
    function = getattr(obj, name)

    def async_to_sync_gen(agen, loop, is_main_thread):
        async def anext(agen):
            try:
                return await agen.__anext__(), False
            except StopAsyncIteration:
                return None, True

        while True:
            if is_main_thread:
                item, done = loop.run_until_complete(anext(agen))
            else:
                item, done = asyncio.run_coroutine_threadsafe(anext(agen), loop).result()

            if done:
                break

            yield item

    @functools.wraps(function)
    def async_to_sync_wrap(*args, **kwargs):
        coroutine = function(*args, **kwargs)

        # ── Main thread OR main_loop not yet running (top-level sync code) ──
        if threading.current_thread() is threading.main_thread() or not main_loop.is_running():
            if main_loop.is_running():
                # Already inside an async context on the main loop → return
                # the coroutine directly so the caller can await it.
                return coroutine
            else:
                if inspect.iscoroutine(coroutine):
                    return main_loop.run_until_complete(coroutine)

                if inspect.isasyncgen(coroutine):
                    return async_to_sync_gen(coroutine, main_loop, True)

        # ── Worker thread (sync def handler dispatched by Pyrogram) ────────
        # The Client's Session and recv_worker are running on main_loop in the
        # main thread.  Submit to main_loop via run_coroutine_threadsafe so
        # that every Future is created on the SAME loop — no clash possible.
        else:
            if inspect.iscoroutine(coroutine):
                if main_loop.is_running():
                    # main_loop is running in another thread — thread-safe submit
                    return asyncio.run_coroutine_threadsafe(coroutine, main_loop).result()
                else:
                    return main_loop.run_until_complete(coroutine)

            if inspect.isasyncgen(coroutine):
                if main_loop.is_running():
                    return async_to_sync_gen(coroutine, main_loop, False)
                else:
                    return async_to_sync_gen(coroutine, main_loop, True)

    setattr(obj, name, async_to_sync_wrap)


def wrap(source):
    for name in dir(source):
        method = getattr(source, name)

        if not name.startswith("_"):
            if inspect.iscoroutinefunction(method) or inspect.isasyncgenfunction(method):
                async_to_sync(source, name)


# Wrap all Client's relevant methods
wrap(Methods)

# Wrap types' bound methods
for class_name in dir(types):
    cls = getattr(types, class_name)

    if inspect.isclass(cls):
        wrap(cls)

# Special case for idle and compose, because they are not inside Methods
async_to_sync(idle_module, "idle")
idle = getattr(idle_module, "idle")

async_to_sync(compose_module, "compose")
compose = getattr(compose_module, "compose")
