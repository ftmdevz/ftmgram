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


def async_to_sync(obj, name):
    function = getattr(obj, name)

    def async_to_sync_gen(agen, loop):
        """Iterate an async generator synchronously by submitting each step to the loop."""
        async def anext(agen):
            try:
                return await agen.__anext__(), False
            except StopAsyncIteration:
                return None, True

        while True:
            item, done = asyncio.run_coroutine_threadsafe(anext(agen), loop).result()
            if done:
                break
            yield item

    @functools.wraps(function)
    def async_to_sync_wrap(*args, **kwargs):
        coroutine = function(*args, **kwargs)

        # ------------------------------------------------------------------ #
        # If we're already inside a running event loop (i.e. an async context
        # like an async def handler), just return the coroutine/asyncgen so
        # the caller can `await` it directly.  This is the fast-path used by
        # async bots — no thread switching, no loop conflicts.
        # ------------------------------------------------------------------ #
        try:
            running_loop = asyncio.get_running_loop()
            # We are inside an async context — just return as-is.
            return coroutine
        except RuntimeError:
            pass  # No running loop — we are in a sync context.

        # ------------------------------------------------------------------ #
        # Sync context: obtain (or create) a dedicated background event loop
        # that lives in the main thread but is NOT yet running.  We drive it
        # with run_until_complete / run_coroutine_threadsafe so it never
        # conflicts with the Client's internal network loop.
        # ------------------------------------------------------------------ #
        loop = utils.get_sync_loop()

        if inspect.iscoroutine(coroutine):
            return loop.run_until_complete(coroutine)

        if inspect.isasyncgen(coroutine):
            return async_to_sync_gen(coroutine, loop)

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
