Types
=====

High-level Python objects that represent Telegram entities.
All types are found in the :mod:`ftmgram.types` namespace.

.. code-block:: python

   from ftmgram.types import Message, User, Chat

----

Core Types
----------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - ``Message``
     - A single Telegram message
   * - ``User``
     - A Telegram user or bot
   * - ``Chat``
     - A private chat, group, supergroup or channel
   * - ``ChatMember``
     - A member of a chat
   * - ``ChatPermissions``
     - Permissions available in a chat
   * - ``Dialog``
     - An entry in the dialog list

Media Types
-----------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - ``Photo``
     - A photo
   * - ``Video``
     - A video file
   * - ``Audio``
     - An audio file
   * - ``Document``
     - A generic document / file
   * - ``Animation``
     - A GIF or animation
   * - ``Sticker``
     - A sticker
   * - ``Voice``
     - A voice note
   * - ``VideoNote``
     - A round video message
   * - ``Location``
     - A geographic location
   * - ``Contact``
     - A phone contact
   * - ``Poll``
     - A poll
   * - ``Venue``
     - A venue/place
   * - ``Game``
     - A game
   * - ``Invoice``
     - A payment invoice
   * - ``SuccessfulPayment``
     - A successful payment result

Rich Messages — Bot API 10.1
------------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Type
     - Description
   * - ``RichMessage``
     - A received rich/article message
   * - ``InputRichMessage``
     - Input object for sending rich messages
   * - ``InputRichMessageContent``
     - Builder for rich message content blocks
   * - ``RichText``
     - Base class + factory for inline text types
   * - ``RichTextBold``
     - **Bold** text
   * - ``RichTextItalic``
     - *Italic* text
   * - ``RichTextUnderline``
     - Underlined text
   * - ``RichTextStrikethrough``
     - Strikethrough text
   * - ``RichTextCode``
     - Inline ``code``
   * - ``RichTextUrl``
     - A hyperlink
   * - ``RichTextEmailAddress``
     - Clickable email address
   * - ``RichTextPhoneNumber``
     - Clickable phone number
   * - ``RichTextMarked``
     - Highlighted/marked text
   * - ``RichTextSubscript``
     - Subscript text
   * - ``RichTextSuperscript``
     - Superscript text
   * - ``RichTextAnchor``
     - Named anchor
   * - ``RichTextAnchorLink``
     - Link to a named anchor
   * - ``RichBlockParagraph``
     - A paragraph block
   * - ``RichBlockPhoto``
     - An inline photo block
   * - ``RichBlockVideo``
     - An inline video block
   * - ``RichBlockAudio``
     - An audio player block
   * - ``RichBlockTable``
     - A data table block
   * - ``RichBlockList``
     - Ordered or unordered list block
   * - ``RichBlockSlideshow``
     - Multi-image slideshow block
   * - ``RichBlockCollage``
     - Photo collage block
   * - ``RichBlockBlockQuotation``
     - Block quote
   * - ``RichBlockPreformatted``
     - Code / preformatted block
   * - ``RichBlockSectionHeading``
     - Section heading
   * - ``RichBlockDivider``
     - Horizontal divider
   * - ``RichBlockFooter``
     - Footer text block

Checklists — Bot API 10.1
--------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - ``Checklist``
     - A received checklist message
   * - ``ChecklistTask``
     - An individual checklist task
   * - ``InputChecklistTask``
     - Input for creating a new task

Link Media — Bot API 10.1
--------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - ``Link``
     - A link attached to a poll option or message

Join Requests
-------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - ``ChatJoinRequest``
     - A chat join request with optional ``query_id``

Keyboards & Inline
------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Type
     - Description
   * - ``InlineKeyboardMarkup``
     - An inline keyboard
   * - ``InlineKeyboardButton``
     - A single inline button
   * - ``ReplyKeyboardMarkup``
     - A reply keyboard
   * - ``KeyboardButton``
     - A single reply keyboard button
   * - ``ReplyKeyboardRemove``
     - Remove reply keyboard
   * - ``ForceReply``
     - Force a reply from the user
   * - ``CallbackQuery``
     - An incoming callback query
   * - ``InlineQuery``
     - An incoming inline query
