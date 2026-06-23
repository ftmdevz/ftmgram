Filters
=======

Filters are used with update handlers to selectively process messages and other updates.
All built-in filters live in :mod:`ftmgram.filters`.

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_bot", bot_token="TOKEN")

   @app.on_message(filters.private & filters.text)
   async def handler(client, message):
       ...

Combining Filters
-----------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Operator
     - Effect
   * - ``&``
     - Both filters must match (AND)
   * - ``|``
     - Either filter must match (OR)
   * - ``~``
     - Filter must NOT match (NOT)

.. code-block:: python

   # Private text messages that are NOT commands
   filters.private & filters.text & ~filters.command("start")

Message Filters
---------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Filter
     - Matches
   * - ``filters.text``
     - Messages with a text body
   * - ``filters.caption``
     - Media messages with a caption
   * - ``filters.photo``
     - Photo messages
   * - ``filters.video``
     - Video messages
   * - ``filters.audio``
     - Audio messages
   * - ``filters.document``
     - Document messages
   * - ``filters.animation``
     - GIF / animation messages
   * - ``filters.sticker``
     - Sticker messages
   * - ``filters.voice``
     - Voice note messages
   * - ``filters.video_note``
     - Round video messages
   * - ``filters.location``
     - Location messages
   * - ``filters.contact``
     - Contact messages
   * - ``filters.poll``
     - Poll messages
   * - ``filters.checklist``
     - Checklist messages *(Bot API 10.1)*
   * - ``filters.media``
     - Any media message
   * - ``filters.web_page``
     - Messages with a link preview
   * - ``filters.forwarded``
     - Forwarded messages
   * - ``filters.reply``
     - Reply messages
   * - ``filters.pinned``
     - Pinned message service events
   * - ``filters.new_chat_members``
     - New member join events
   * - ``filters.left_chat_member``
     - Member leave events

Chat Filters
------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Filter
     - Matches
   * - ``filters.private``
     - Private (DM) chats only
   * - ``filters.group``
     - Group and supergroup chats
   * - ``filters.channel``
     - Channel posts
   * - ``filters.bot``
     - Messages from bots
   * - ``filters.me``
     - Messages from yourself

Command Filter
--------------

.. code-block:: python

   # Single command
   @app.on_message(filters.command("start"))
   async def start(client, message): ...

   # Multiple commands at once
   @app.on_message(filters.command(["help", "h"]))
   async def help_cmd(client, message): ...

   # Custom prefix (e.g. ! instead of /)
   @app.on_message(filters.command("ban", prefixes="!"))
   async def ban(client, message): ...

Regex Filter
------------

.. code-block:: python

   import re

   @app.on_message(filters.regex(r"hello", re.IGNORECASE))
   async def on_hello(client, message): ...

User / Chat Whitelists
----------------------

.. code-block:: python

   ADMINS = [123456789, 987654321]

   @app.on_message(filters.user(ADMINS))
   async def admin_only(client, message): ...

   @app.on_message(filters.chat([-100123456789]))
   async def specific_group(client, message): ...

Custom Filters
--------------

.. code-block:: python

   from ftmgram.filters import Filter

   async def is_long(_, __, message):
       return message.text and len(message.text) > 200

   long_text = Filter.create(is_long, "LongTextFilter")

   @app.on_message(long_text)
   async def handle_long(client, message): ...
