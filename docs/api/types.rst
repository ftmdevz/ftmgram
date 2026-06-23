Types
=====

High-level Python objects that represent Telegram entities.
All types are found in the :mod:`ftmgram.types` namespace.

.. code-block:: python

   from ftmgram.types import Message, User, Chat

----

.. rubric:: Core Types

.. autosummary::
   :nosignatures:

   ftmgram.types.Message
   ftmgram.types.User
   ftmgram.types.Chat
   ftmgram.types.ChatMember
   ftmgram.types.ChatPermissions
   ftmgram.types.ChatPrivileges
   ftmgram.types.Dialog

.. rubric:: Media Types

.. autosummary::
   :nosignatures:

   ftmgram.types.Photo
   ftmgram.types.Video
   ftmgram.types.Audio
   ftmgram.types.Document
   ftmgram.types.Animation
   ftmgram.types.Sticker
   ftmgram.types.Voice
   ftmgram.types.VideoNote
   ftmgram.types.Location
   ftmgram.types.Contact
   ftmgram.types.Poll
   ftmgram.types.PollOption
   ftmgram.types.Venue
   ftmgram.types.Game
   ftmgram.types.Invoice
   ftmgram.types.SuccessfulPayment

.. rubric:: Rich Messages (Bot API 10.1)

.. autosummary::
   :nosignatures:

   ftmgram.types.RichMessage
   ftmgram.types.InputRichMessage
   ftmgram.types.InputRichMessageContent
   ftmgram.types.RichText
   ftmgram.types.RichTextBold
   ftmgram.types.RichTextItalic
   ftmgram.types.RichTextUnderline
   ftmgram.types.RichTextStrikethrough
   ftmgram.types.RichTextCode
   ftmgram.types.RichTextUrl
   ftmgram.types.RichTextEmailAddress
   ftmgram.types.RichTextPhoneNumber
   ftmgram.types.RichTextMarked
   ftmgram.types.RichTextSubscript
   ftmgram.types.RichTextSuperscript
   ftmgram.types.RichTextAnchor
   ftmgram.types.RichTextAnchorLink
   ftmgram.types.RichBlockParagraph
   ftmgram.types.RichBlockPhoto
   ftmgram.types.RichBlockVideo
   ftmgram.types.RichBlockAudio
   ftmgram.types.RichBlockTable
   ftmgram.types.RichBlockList
   ftmgram.types.RichBlockSlideshow
   ftmgram.types.RichBlockCollage
   ftmgram.types.RichBlockBlockQuotation
   ftmgram.types.RichBlockPreformatted
   ftmgram.types.RichBlockSectionHeading
   ftmgram.types.RichBlockDivider
   ftmgram.types.RichBlockFooter

.. rubric:: Checklists (Bot API 10.1)

.. autosummary::
   :nosignatures:

   ftmgram.types.Checklist
   ftmgram.types.ChecklistTask
   ftmgram.types.InputChecklistTask

.. rubric:: Link Media (Bot API 10.1)

.. autosummary::
   :nosignatures:

   ftmgram.types.Link

.. rubric:: Join Requests

.. autosummary::
   :nosignatures:

   ftmgram.types.ChatJoinRequest

.. rubric:: Inline & Keyboards

.. autosummary::
   :nosignatures:

   ftmgram.types.InlineKeyboardMarkup
   ftmgram.types.InlineKeyboardButton
   ftmgram.types.ReplyKeyboardMarkup
   ftmgram.types.KeyboardButton
   ftmgram.types.ReplyKeyboardRemove
   ftmgram.types.ForceReply
   ftmgram.types.CallbackQuery
   ftmgram.types.InlineQuery
   ftmgram.types.InlineQueryResult

.. rubric:: Input Media

.. autosummary::
   :nosignatures:

   ftmgram.types.InputMediaPhoto
   ftmgram.types.InputMediaVideo
   ftmgram.types.InputMediaAudio
   ftmgram.types.InputMediaDocument
   ftmgram.types.InputMediaAnimation

----

Full Types Reference
--------------------

.. automodule:: ftmgram.types
   :members:
   :undoc-members: False
