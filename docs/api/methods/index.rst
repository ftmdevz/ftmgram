Methods
=======

Messages
--------

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.send_message`
   * :meth:`~ftmgram.Client.send_rich_message`
   * :meth:`~ftmgram.Client.send_rich_message_draft`
   * :meth:`~ftmgram.Client.send_message_draft`
   * :meth:`~ftmgram.Client.send_photo`
   * :meth:`~ftmgram.Client.send_audio`
   * :meth:`~ftmgram.Client.send_video`
   * :meth:`~ftmgram.Client.send_document`
   * :meth:`~ftmgram.Client.send_animation`
   * :meth:`~ftmgram.Client.send_sticker`
   * :meth:`~ftmgram.Client.send_voice`
   * :meth:`~ftmgram.Client.send_video_note`
   * :meth:`~ftmgram.Client.send_location`
   * :meth:`~ftmgram.Client.send_contact`
   * :meth:`~ftmgram.Client.send_poll`
   * :meth:`~ftmgram.Client.send_dice`
   * :meth:`~ftmgram.Client.send_media_group`
   * :meth:`~ftmgram.Client.send_checklist`
   * :meth:`~ftmgram.Client.forward_messages`
   * :meth:`~ftmgram.Client.copy_message`
   * :meth:`~ftmgram.Client.copy_media_group`
   * :meth:`~ftmgram.Client.edit_message_text`
   * :meth:`~ftmgram.Client.edit_message_caption`
   * :meth:`~ftmgram.Client.edit_message_media`
   * :meth:`~ftmgram.Client.edit_message_reply_markup`
   * :meth:`~ftmgram.Client.edit_ephemeral_message_text`
   * :meth:`~ftmgram.Client.delete_ephemeral_message`
   * :meth:`~ftmgram.Client.delete_messages`
   * :meth:`~ftmgram.Client.get_messages`
   * :meth:`~ftmgram.Client.get_chat_history`
   * :meth:`~ftmgram.Client.search_messages`
   * :meth:`~ftmgram.Client.download_media`
   * :meth:`~ftmgram.Client.send_chat_action`
   * :meth:`~ftmgram.Client.translate_message_text`

.. toctree::
   :hidden:

   send_message
   send_rich_message
   send_rich_message_draft
   send_message_draft
   send_photo
   send_audio
   send_video
   send_document
   send_animation
   send_sticker
   send_voice
   send_video_note
   send_location
   send_contact
   send_poll
   send_dice
   send_media_group
   send_checklist
   forward_messages
   copy_message
   copy_media_group
   edit_message_text
   edit_message_caption
   edit_message_media
   edit_message_reply_markup
   edit_ephemeral_message_text
   delete_ephemeral_message
   delete_messages
   get_messages
   get_chat_history
   search_messages
   download_media
   send_chat_action
   translate_message_text

Chats
-----

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.get_chat`
   * :meth:`~ftmgram.Client.get_dialogs`
   * :meth:`~ftmgram.Client.join_chat`
   * :meth:`~ftmgram.Client.leave_chat`
   * :meth:`~ftmgram.Client.create_group`
   * :meth:`~ftmgram.Client.create_channel`
   * :meth:`~ftmgram.Client.create_supergroup`
   * :meth:`~ftmgram.Client.get_chat_members`
   * :meth:`~ftmgram.Client.get_chat_member`
   * :meth:`~ftmgram.Client.ban_chat_member`
   * :meth:`~ftmgram.Client.unban_chat_member`
   * :meth:`~ftmgram.Client.restrict_chat_member`
   * :meth:`~ftmgram.Client.promote_chat_member`
   * :meth:`~ftmgram.Client.set_chat_title`
   * :meth:`~ftmgram.Client.set_chat_description`
   * :meth:`~ftmgram.Client.set_chat_photo`
   * :meth:`~ftmgram.Client.delete_chat_photo`
   * :meth:`~ftmgram.Client.pin_chat_message`
   * :meth:`~ftmgram.Client.unpin_chat_message`
   * :meth:`~ftmgram.Client.get_chat_invite_link`
   * :meth:`~ftmgram.Client.create_chat_invite_link`
   * :meth:`~ftmgram.Client.archive_chats`
   * :meth:`~ftmgram.Client.set_slow_mode`
   * :meth:`~ftmgram.Client.set_chat_permissions`
   * :meth:`~ftmgram.Client.get_forum_topics`
   * :meth:`~ftmgram.Client.create_forum_topic`

.. toctree::
   :hidden:

   get_chat
   get_dialogs
   join_chat
   leave_chat
   create_group
   create_channel
   create_supergroup
   get_chat_members
   get_chat_member
   ban_chat_member
   unban_chat_member
   restrict_chat_member
   promote_chat_member
   set_chat_title
   set_chat_description
   set_chat_photo
   delete_chat_photo
   pin_chat_message
   unpin_chat_message
   get_chat_invite_link
   create_chat_invite_link
   archive_chats
   set_slow_mode
   set_chat_permissions
   get_forum_topics
   create_forum_topic

Users
-----

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.get_me`
   * :meth:`~ftmgram.Client.get_users`
   * :meth:`~ftmgram.Client.get_user_profile_photos`
   * :meth:`~ftmgram.Client.block_user`
   * :meth:`~ftmgram.Client.unblock_user`
   * :meth:`~ftmgram.Client.update_profile`
   * :meth:`~ftmgram.Client.set_profile_photo`
   * :meth:`~ftmgram.Client.get_common_chats`

.. toctree::
   :hidden:

   get_me
   get_users
   get_user_profile_photos
   block_user
   unblock_user
   update_profile
   set_profile_photo
   get_common_chats

Bots & Inline
-------------

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.answer_callback_query`
   * :meth:`~ftmgram.Client.answer_inline_query`
   * :meth:`~ftmgram.Client.answer_web_app_query`
   * :meth:`~ftmgram.Client.set_bot_commands`
   * :meth:`~ftmgram.Client.get_bot_commands`
   * :meth:`~ftmgram.Client.delete_bot_commands`
   * :meth:`~ftmgram.Client.set_chat_menu_button`
   * :meth:`~ftmgram.Client.get_chat_menu_button`
   * :meth:`~ftmgram.Client.answer_chat_join_request_query`
   * :meth:`~ftmgram.Client.send_chat_join_request_web_app`
   * :meth:`~ftmgram.Client.get_business_connection`
   * :meth:`~ftmgram.Client.verify_user`
   * :meth:`~ftmgram.Client.create_bot`

.. toctree::
   :hidden:

   answer_callback_query
   answer_inline_query
   answer_web_app_query
   set_bot_commands
   get_bot_commands
   delete_bot_commands
   set_chat_menu_button
   get_chat_menu_button
   answer_chat_join_request_query
   send_chat_join_request_web_app
   get_business_connection
   verify_user
   create_bot

Stars & Payments
----------------

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.get_owned_star_count`
   * :meth:`~ftmgram.Client.send_invoice`
   * :meth:`~ftmgram.Client.create_invoice_link`
   * :meth:`~ftmgram.Client.answer_shipping_query`
   * :meth:`~ftmgram.Client.answer_pre_checkout_query`
   * :meth:`~ftmgram.Client.refund_star_payment`

.. toctree::
   :hidden:

   get_owned_star_count
   send_invoice
   create_invoice_link
   answer_shipping_query
   answer_pre_checkout_query
   refund_star_payment

Stickers & Reactions
--------------------

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.send_reaction`
   * :meth:`~ftmgram.Client.get_custom_emoji_stickers`
   * :meth:`~ftmgram.Client.get_sticker_set`
   * :meth:`~ftmgram.Client.create_new_sticker_set`
   * :meth:`~ftmgram.Client.add_sticker_to_set`
   * :meth:`~ftmgram.Client.set_sticker_position_in_set`
   * :meth:`~ftmgram.Client.delete_sticker_from_set`

.. toctree::
   :hidden:

   send_reaction
   get_custom_emoji_stickers
   get_sticker_set
   create_new_sticker_set
   add_sticker_to_set
   set_sticker_position_in_set
   delete_sticker_from_set

Utilities
---------

.. hlist::
   :columns: 3

   * :meth:`~ftmgram.Client.start`
   * :meth:`~ftmgram.Client.stop`
   * :meth:`~ftmgram.Client.run`
   * :meth:`~ftmgram.Client.idle`
   * :meth:`~ftmgram.Client.add_handler`
   * :meth:`~ftmgram.Client.remove_handler`
   * :meth:`~ftmgram.Client.export_session_string`
   * :meth:`~ftmgram.Client.invoke`

.. toctree::
   :hidden:

   start
   stop
   run
   idle
   add_handler
   remove_handler
   export_session_string
   invoke

