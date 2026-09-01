UNRELEASED VERSION
==================


New Features
-------------

- Allow to set emoji status for channel.
- Added ``members_only`` and ``country_codes`` to :meth:`~ftmgram.Client.send_poll`, :meth:`~ftmgram.types.Message.reply_poll` and :obj:`~ftmgram.types.Poll`.
- Added the :obj:`~ftmgram.filters.guest_message_query_id`.
- Added the classes :obj:`~ftmgram.types.SentGuestMessage` and :obj:`~ftmgram.types.BotAccessSettings`.
- Added the methods :meth:`~ftmgram.Client.answer_guest_query`, :meth:`~ftmgram.types.Message.answer`, :meth:`~ftmgram.Client.delete_message_reaction`, :meth:`~ftmgram.Client.delete_all_message_reactions`, :meth:`~ftmgram.Client.get_user_personal_chat_messages` and :meth:`~ftmgram.Client.get_user_personal_chat_messages_count`.
- Added the fields ``guest_bot_caller_user``, ``guest_bot_caller_chat``, ``guest_query_id``, ``summary_language_code``, ``is_paid_star_suggested_post``, ``is_paid_ton_suggested_post``, ``schedule_repeat_period``, ``restriction_reason`` to the :obj:`~ftmgram.types.Message`.
- Added the parameter ``return_bots`` to the method :meth:`~ftmgram.Client.get_chat_administrators`.
- Added the field ``supports_guest_queries`` to the :obj:`~ftmgram.types.User`.
- Added ``description_media`` and ``explanation_media`` in :meth:`~ftmgram.Client.send_poll` and :meth:`~ftmgram.types.Message.reply_poll`.
- Added the field ``can_react_to_messages`` to the :obj:`~ftmgram.types.ChatPermissions`.

Bug Fixes
----------

- Resolves NameError with the InputMedia types (contributed by @zydou in `#242 <https://github.com/TelegramPlayground/FTMGram/issues/242>`__)
- Resolves four NameError bugs that cause runtime crashes in the library. (contributed by @Gaoc3 in `#244 <https://github.com/TelegramPlayground/FTMGram/pull/244>`__)

Layer Changes
--------------

- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=225&to=228>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=225&to=228>`__.
