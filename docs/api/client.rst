Client
======

The :class:`~ftmgram.Client` is the main entry point for interacting with Telegram.
It manages the connection, session, and exposes all high-level API methods.

.. code-block:: python

   from ftmgram import Client

   app = Client(
       name="my_session",
       api_id=12345,
       api_hash="0123456789abcdef",
   )

Constructor
-----------

.. autoclass:: ftmgram.Client
   :members: __init__
   :undoc-members:

----

.. rubric:: Messages

.. autosummary::
   :nosignatures:

   ftmgram.Client.send_message
   ftmgram.Client.send_photo
   ftmgram.Client.send_video
   ftmgram.Client.send_audio
   ftmgram.Client.send_document
   ftmgram.Client.send_animation
   ftmgram.Client.send_sticker
   ftmgram.Client.send_voice
   ftmgram.Client.send_video_note
   ftmgram.Client.send_location
   ftmgram.Client.send_contact
   ftmgram.Client.send_poll
   ftmgram.Client.send_rich_message
   ftmgram.Client.send_rich_message_draft
   ftmgram.Client.edit_message_text
   ftmgram.Client.edit_message_caption
   ftmgram.Client.delete_messages
   ftmgram.Client.forward_messages
   ftmgram.Client.copy_message
   ftmgram.Client.pin_chat_message
   ftmgram.Client.unpin_chat_message
   ftmgram.Client.get_messages
   ftmgram.Client.get_history

.. rubric:: Checklists

.. autosummary::
   :nosignatures:

   ftmgram.Client.append_checklist_tasks
   ftmgram.Client.toggle_checklist_task

.. rubric:: Chats

.. autosummary::
   :nosignatures:

   ftmgram.Client.get_chat
   ftmgram.Client.get_dialogs
   ftmgram.Client.join_chat
   ftmgram.Client.leave_chat
   ftmgram.Client.archive_chats
   ftmgram.Client.unarchive_chats
   ftmgram.Client.get_chat_members
   ftmgram.Client.get_chat_member
   ftmgram.Client.ban_chat_member
   ftmgram.Client.unban_chat_member
   ftmgram.Client.restrict_chat_member
   ftmgram.Client.promote_chat_member
   ftmgram.Client.answer_chat_join_request_query
   ftmgram.Client.send_chat_join_request_web_app

.. rubric:: Users

.. autosummary::
   :nosignatures:

   ftmgram.Client.get_me
   ftmgram.Client.get_users
   ftmgram.Client.get_common_chats
   ftmgram.Client.block_user
   ftmgram.Client.unblock_user

.. rubric:: Bots

.. autosummary::
   :nosignatures:

   ftmgram.Client.get_bot_info
   ftmgram.Client.set_bot_info
   ftmgram.Client.answer_callback_query
   ftmgram.Client.answer_inline_query
   ftmgram.Client.answer_web_app_query
   ftmgram.Client.send_game
   ftmgram.Client.set_game_score
   ftmgram.Client.get_game_high_scores

.. rubric:: Stars & Payments

.. autosummary::
   :nosignatures:

   ftmgram.Client.get_owned_star_count
   ftmgram.Client.send_invoice
   ftmgram.Client.answer_pre_checkout_query
   ftmgram.Client.answer_shipping_query

.. rubric:: Account

.. autosummary::
   :nosignatures:

   ftmgram.Client.update_profile
   ftmgram.Client.set_profile_photo
   ftmgram.Client.delete_profile_photos
   ftmgram.Client.get_profile_photos
   ftmgram.Client.set_privacy

----

Full Method Reference
---------------------

.. autoclass:: ftmgram.Client
   :members:
   :exclude-members: __init__
