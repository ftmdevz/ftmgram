Client
======

The ``Client`` class is the main entry point for interacting with Telegram.
It manages the MTProto connection, session, and exposes all high-level API methods.

.. code-block:: python

   from ftmgram import Client

   app = Client(
       name="my_session",
       api_id=12345,
       api_hash="0123456789abcdef",
   )

Constructor Parameters
----------------------

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``name``
     - ``str``
     - Session name (used as filename for the ``.session`` file)
   * - ``api_id``
     - ``int``
     - Telegram API ID from `my.telegram.org <https://my.telegram.org>`_
   * - ``api_hash``
     - ``str``
     - Telegram API hash from `my.telegram.org <https://my.telegram.org>`_
   * - ``bot_token``
     - ``str``
     - Bot token from ``@BotFather`` — omit for user accounts
   * - ``session_string``
     - ``str``
     - String session for serverless/in-memory usage
   * - ``phone_number``
     - ``str``
     - Phone number for user accounts
   * - ``workdir``
     - ``str``
     - Directory for session files (default: current directory)
   * - ``plugins``
     - ``dict``
     - Plugin configuration for loading handlers from files
   * - ``proxy``
     - ``dict``
     - Proxy settings (SOCKS5, SOCKS4, HTTP)

----

Messages
--------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``send_message(chat_id, text, ...)``
     - Send a text message
   * - ``send_photo(chat_id, photo, ...)``
     - Send a photo
   * - ``send_video(chat_id, video, ...)``
     - Send a video
   * - ``send_audio(chat_id, audio, ...)``
     - Send an audio file
   * - ``send_document(chat_id, document, ...)``
     - Send a document
   * - ``send_animation(chat_id, animation, ...)``
     - Send a GIF / animation
   * - ``send_sticker(chat_id, sticker, ...)``
     - Send a sticker
   * - ``send_voice(chat_id, voice, ...)``
     - Send a voice note
   * - ``send_video_note(chat_id, video_note, ...)``
     - Send a round video
   * - ``send_location(chat_id, latitude, longitude)``
     - Send a location
   * - ``send_contact(chat_id, phone_number, ...)``
     - Send a contact
   * - ``send_poll(chat_id, question, options, ...)``
     - Send a poll
   * - ``send_media_group(chat_id, media)``
     - Send a group of media
   * - ``edit_message_text(chat_id, message_id, text, ...)``
     - Edit a message's text
   * - ``edit_message_caption(chat_id, message_id, caption, ...)``
     - Edit a message's caption
   * - ``delete_messages(chat_id, message_ids)``
     - Delete one or more messages
   * - ``forward_messages(chat_id, from_chat_id, message_ids)``
     - Forward messages
   * - ``copy_message(chat_id, from_chat_id, message_id)``
     - Copy a message without the forwarded tag
   * - ``pin_chat_message(chat_id, message_id)``
     - Pin a message
   * - ``unpin_chat_message(chat_id, message_id)``
     - Unpin a message
   * - ``get_messages(chat_id, message_ids)``
     - Fetch one or more messages by ID
   * - ``get_history(chat_id, ...)``
     - Iterate over chat history

Rich Messages — Bot API 10.1
------------------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``send_rich_message(chat_id, rich_message)``
     - Send a rich/article message
   * - ``send_rich_message_draft(chat_id, rich_message)``
     - Save a rich message as a draft
   * - ``edit_message_text(..., rich_message=...)``
     - Edit an existing message using a rich message

Checklists — Bot API 10.1
--------------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``append_checklist_tasks(chat_id, message_id, tasks)``
     - Add tasks to an existing checklist
   * - ``toggle_checklist_task(chat_id, message_id, task_id, completed)``
     - Check or uncheck a task

Chats
-----

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``get_chat(chat_id)``
     - Fetch a chat by ID or username
   * - ``get_dialogs()``
     - Iterate over all dialogs
   * - ``join_chat(chat_id)``
     - Join a chat or channel
   * - ``leave_chat(chat_id)``
     - Leave a chat
   * - ``archive_chats(chat_ids)``
     - Archive one or more chats
   * - ``unarchive_chats(chat_ids)``
     - Unarchive chats
   * - ``get_chat_members(chat_id, ...)``
     - List members of a chat
   * - ``get_chat_member(chat_id, user_id)``
     - Get a specific member's info
   * - ``ban_chat_member(chat_id, user_id, ...)``
     - Ban a member
   * - ``unban_chat_member(chat_id, user_id)``
     - Unban a member
   * - ``restrict_chat_member(chat_id, user_id, permissions)``
     - Restrict a member
   * - ``promote_chat_member(chat_id, user_id, privileges)``
     - Promote a member to admin
   * - ``answer_chat_join_request_query(query_id, ok, ...)``
     - Answer a join request from a Mini App
   * - ``send_chat_join_request_web_app(chat_id, ...)``
     - Open Mini App for join requests

Users
-----

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``get_me()``
     - Get your own user info
   * - ``get_users(user_ids)``
     - Fetch one or more users
   * - ``get_common_chats(user_id)``
     - Get common chats with a user
   * - ``block_user(user_id)``
     - Block a user
   * - ``unblock_user(user_id)``
     - Unblock a user

Bots
----

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``answer_callback_query(callback_query_id, text, ...)``
     - Answer a callback query
   * - ``answer_inline_query(inline_query_id, results, ...)``
     - Answer an inline query
   * - ``answer_web_app_query(web_app_query_id, result)``
     - Answer a web app query
   * - ``set_bot_commands(commands, ...)``
     - Set the bot's command list
   * - ``get_bot_commands(...)``
     - Get the bot's command list
   * - ``delete_bot_commands(...)``
     - Delete bot commands

Stars & Payments
----------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``get_owned_star_count()``
     - Get the bot's owned Telegram Stars balance
   * - ``send_invoice(chat_id, title, description, ...)``
     - Send a payment invoice
   * - ``answer_pre_checkout_query(pre_checkout_query_id, ok)``
     - Confirm or reject a checkout
   * - ``answer_shipping_query(shipping_query_id, ok, ...)``
     - Answer a shipping query

Account
-------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Method
     - Description
   * - ``update_profile(first_name, ...)``
     - Update your profile info
   * - ``set_profile_photo(photo)``
     - Set your profile photo
   * - ``delete_profile_photos(photo_ids)``
     - Delete profile photos
   * - ``get_profile_photos(user_id)``
     - Get profile photos of a user
   * - ``set_privacy(key, rules)``
     - Set privacy rules
