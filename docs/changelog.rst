Changelog
=========

v3.5.0 — September 2026
-----------------------

* **Bot Chat History Retrieval (`get_bot_chat_history`)**:
  Allows bots to retrieve message history across private chats and groups through safe, high-speed 100-ID batch scanning.

* **Turbo Multi-Worker Media Transfers (`fast_download`)**:
  Download large files, videos, and documents at maximum network speed using multi-worker parallel chunk streaming.

* **Fluent `RichMessageBuilder` DSL**:
  Construct styled rich messages with `<tg-button-row>`, expandable quotes, tables, and paragraphs effortlessly in Python.

* **AI Response Streaming (`stream_text` & `thinking`)**:
  Stream LLM tokens in real-time directly to Telegram drafts with animated thinking placeholders and stop controls.

* **Batch Purge Admin Tool (`purge_messages`)**:
  High-speed batch message deletion with automatic RPC chunking and rate-limit handling.

* **In-Memory Media Buffering (`download_media_to_memory`)**:
  Download media straight into an in-memory `io.BytesIO` buffer without disk I/O bottlenecks.

* **Multi-Client Orchestration (`MultiClient`)**:
  Manage and run multiple bots and user accounts concurrently in a single event loop.

v3.3.0 — June 2026
-------------------


**Bot API 10.1 (June 11, 2026) — Full Coverage**

New Types
~~~~~~~~~

- :class:`~ftmgram.types.RichMessage` — Received rich/article message
- :class:`~ftmgram.types.InputRichMessage` — Send rich messages
- :class:`~ftmgram.types.InputRichMessageContent` — Content block builder
- **RichText variants** (14 types):
  ``RichText``, ``RichTextBold``, ``RichTextItalic``, ``RichTextUnderline``,
  ``RichTextStrikethrough``, ``RichTextCode``, ``RichTextUrl``,
  ``RichTextEmailAddress``, ``RichTextPhoneNumber``, ``RichTextMarked``,
  ``RichTextSubscript``, ``RichTextSuperscript``, ``RichTextAnchor``,
  ``RichTextAnchorLink``
- **RichBlock variants** (19 types):
  ``RichBlock``, ``RichBlockParagraph``, ``RichBlockPhoto``, ``RichBlockVideo``,
  ``RichBlockAudio``, ``RichBlockVoiceNote``, ``RichBlockAnimation``,
  ``RichBlockTable``, ``RichBlockTableCell``, ``RichBlockList``,
  ``RichBlockListItem``, ``RichBlockSlideshow``, ``RichBlockCollage``,
  ``RichBlockBlockQuotation``, ``RichBlockPullQuotation``, ``RichBlockPreformatted``,
  ``RichBlockSectionHeading``, ``RichBlockCaption``, ``RichBlockDetails``,
  ``RichBlockDivider``, ``RichBlockFooter``, ``RichBlockMap``,
  ``RichBlockMathematicalExpression``, ``RichBlockThinking``, ``RichBlockUnsupported``
- :class:`~ftmgram.types.Link` — Link type for poll option media
- :class:`~ftmgram.types.Checklist` — Checklist message type
- :class:`~ftmgram.types.ChecklistTask` — Individual checklist task
- :class:`~ftmgram.types.InputChecklistTask` — Input for creating tasks

New Methods
~~~~~~~~~~~

- :meth:`~ftmgram.Client.send_rich_message` — Send a rich/article message
- :meth:`~ftmgram.Client.send_rich_message_draft` — Save rich message as draft
- :meth:`~ftmgram.Client.answer_chat_join_request_query` — Answer join request from Mini App
- :meth:`~ftmgram.Client.send_chat_join_request_web_app` — Open Mini App for join requests
- :meth:`~ftmgram.Client.get_owned_star_count` — Get bot's owned star balance
- :meth:`~ftmgram.Client.append_checklist_tasks` — Add tasks to existing checklist
- :meth:`~ftmgram.Client.toggle_checklist_task` — Check/uncheck a task

Updated Methods
~~~~~~~~~~~~~~~

- :meth:`~ftmgram.Client.edit_message_text` — Now accepts ``rich_message`` parameter

New Fields
~~~~~~~~~~

- :attr:`~ftmgram.types.Message.rich_message` — Rich message content on received messages
- :attr:`~ftmgram.types.User.supports_join_request_queries` — Bot supports join request queries
- :attr:`~ftmgram.types.Chat.guard_bot` — Channel's anti-spam guard bot
- :attr:`~ftmgram.types.ChatJoinRequest.query_id` — Join request query ID for Mini App flow

New Enums
~~~~~~~~~

- ``MessageMediaType.LINK`` — Link media type
- ``MessageMediaType.CHECKLIST`` — Checklist media type

Bug Fixes
~~~~~~~~~

- Fixed all generated ``ftmgram/raw/`` files incorrectly importing from ``ftmgram`` instead of ``ftmgram``
- Removed duplicate ``get_business_account_star_balance`` method
- Removed deprecated ``send_reaction`` alias

----

v2.2.23 and earlier
--------------------

See `FTMGram releases <https://github.com/ftmdevz/ftmgram/releases>`_ for prior history.
