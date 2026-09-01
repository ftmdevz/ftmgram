Errors & Exceptions
===================

FTMGram translates MTProto RPC error codes into native Python exceptions inheriting from ``ftmgram.errors.RPCError``.

Exception Hierarchy
-------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Exception
     - Description
   * - ``RPCError``
     - Base class for all Telegram RPC errors.
   * - ``FloodWait (420)``
     - Raised when rate limits are exceeded. Contains ``e.value`` (seconds to wait).
   * - ``BadRequest (400)``
     - Invalid parameters (e.g. ``MessageEmpty``, ``PeerIdInvalid``).
   * - ``Unauthorized (401)``
     - Invalid authorization (e.g. ``AuthKeyUnregistered``, ``SessionRevoked``).
   * - ``Forbidden (403)``
     - Insufficient rights or user has blocked the bot (``UserIsBlocked``).
   * - ``InternalServerError (500)``
     - Telegram server-side temporary outage.

Handling FloodWait
------------------

.. code-block:: python

   import asyncio
   from ftmgram.errors import FloodWait

   try:
       await app.send_message(chat_id, "Hello")
   except FloodWait as e:
       print(f"Rate limited! Sleeping for {e.value}s")
       await asyncio.sleep(e.value)
       await app.send_message(chat_id, "Hello")
