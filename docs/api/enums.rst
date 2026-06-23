Enums
=====

Enumeration types used across the FTMGram API.
All enums are in :mod:`ftmgram.enums`.

.. code-block:: python

   from ftmgram.enums import MessageMediaType, ChatType, ParseMode

----

ChatType
--------

.. autoclass:: ftmgram.enums.ChatType
   :members:
   :undoc-members:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Value
     - Description
   * - ``ChatType.PRIVATE``
     - Direct message / private chat
   * - ``ChatType.GROUP``
     - Legacy group
   * - ``ChatType.SUPERGROUP``
     - Supergroup
   * - ``ChatType.CHANNEL``
     - Broadcast channel
   * - ``ChatType.BOT``
     - Bot DM

MessageMediaType
----------------

.. autoclass:: ftmgram.enums.MessageMediaType
   :members:
   :undoc-members:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Value
     - Description
   * - ``AUDIO``
     - Audio file
   * - ``DOCUMENT``
     - Generic document
   * - ``PHOTO``
     - Photo
   * - ``STICKER``
     - Sticker
   * - ``VIDEO``
     - Video
   * - ``ANIMATION``
     - GIF or animation
   * - ``VOICE``
     - Voice note
   * - ``VIDEO_NOTE``
     - Round video
   * - ``CONTACT``
     - Contact card
   * - ``LOCATION``
     - Location pin
   * - ``VENUE``
     - Venue/place
   * - ``POLL``
     - Poll
   * - ``DICE``
     - Dice
   * - ``GAME``
     - Game
   * - ``STORY``
     - Story preview
   * - ``WEB_PAGE``
     - Link preview
   * - ``GIVEAWAY``
     - Giveaway
   * - ``INVOICE``
     - Invoice / Stars purchase
   * - ``CHECKLIST``
     - Checklist *(Bot API 10.1)*
   * - ``LINK``
     - Link poll media *(Bot API 10.1)*

ParseMode
---------

.. autoclass:: ftmgram.enums.ParseMode
   :members:
   :undoc-members:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Value
     - Description
   * - ``ParseMode.MARKDOWN``
     - Pyrogram Markdown syntax
   * - ``ParseMode.HTML``
     - HTML tags
   * - ``ParseMode.DISABLED``
     - No parse mode — plain text only

ChatMemberStatus
----------------

.. autoclass:: ftmgram.enums.ChatMemberStatus
   :members:
   :undoc-members:

SentCodeType
------------

.. autoclass:: ftmgram.enums.SentCodeType
   :members:
   :undoc-members:

StorageType
-----------

.. autoclass:: ftmgram.enums.StorageType
   :members:
   :undoc-members:

----

Full Enums Reference
--------------------

.. automodule:: ftmgram.enums
   :members:
   :undoc-members: False
