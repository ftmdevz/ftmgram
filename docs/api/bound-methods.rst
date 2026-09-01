Bound Methods
=============

Bound methods are helper functions attached directly to data model instances for fluid, chainable programming.

Message Bound Methods
---------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``Message.reply(text, ...)``
     - Reply to this message with a text message.
   * - ``Message.reply_text(text, ...)``
     - Alias for ``reply()``.
   * - ``Message.reply_photo(photo, ...)``
     - Reply with a photo.
   * - ``Message.edit_text(text, ...)``
     - Edit the message's text.
   * - ``Message.edit_caption(caption, ...)``
     - Edit the message's media caption.
   * - ``Message.delete()``
     - Delete this message.
   * - ``Message.forward(chat_id)``
     - Forward this message to another chat.
   * - ``Message.copy(chat_id)``
     - Copy this message without forward header.
   * - ``Message.click(index)``
     - Click an inline button attached to this message.
   * - ``Message.download()``
     - Download the media attached to this message.

CallbackQuery Bound Methods
---------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``CallbackQuery.answer(text, ...)``
     - Answer this callback query with a notification or alert.
   * - ``CallbackQuery.edit_message_text(text, ...)``
     - Edit the originating message's text.

Chat Bound Methods
------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``Chat.ban_member(user_id)``
     - Ban a member from this chat.
   * - ``Chat.unban_member(user_id)``
     - Unban a member from this chat.
   * - ``Chat.get_member(user_id)``
     - Get details about a specific chat member.
   * - ``Chat.leave()``
     - Leave this group, supergroup, or channel.
