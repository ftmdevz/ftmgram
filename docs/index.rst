:hide-toc:

FTMGram
=======

.. image:: _static/logo.png
   :align: center
   :width: 180px
   :alt: FTMGram

.. raw:: html

   <p align="center">
     <a href="https://pypi.python.org/pypi/ftmgram"><img src="https://img.shields.io/pypi/v/ftmgram.svg?logo=pypi&logoColor=white&color=orange" alt="PyPI"></a>
     &nbsp;
     <a href="https://pypi.python.org/pypi/ftmgram"><img src="https://img.shields.io/pypi/pyversions/ftmgram.svg?logo=python&logoColor=white" alt="Python"></a>
     &nbsp;
     <a href="https://pypi.python.org/pypi/ftmgram"><img src="https://img.shields.io/pypi/l/ftmgram.svg?color=orange" alt="License"></a>
     &nbsp;
     <a href="https://github.com/ftmdevz/ftmgram"><img src="https://img.shields.io/github/stars/ftmdevz/ftmgram?style=flat&color=orange" alt="Stars"></a>
   </p>

|

.. rst-class:: lead

   **Elegant, modern and asynchronous Telegram MTProto API framework in Python — for users and bots.**

   Built on top of Pyrogram's solid foundation, FTMGram delivers full **Bot API 10.1** support
   with zero migration friction from Pyrogram or KuriGram.

|

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🚀 Getting Started
      :link: intro/index
      :link-type: doc

      Install FTMGram, run your first bot, and migrate from Pyrogram in minutes.

   .. grid-item-card:: 📖 API Reference
      :link: api/index
      :link-type: doc

      Complete reference for Client methods, Types, Filters, and Enums.

   .. grid-item-card:: 📚 Topics & Guides
      :link: topics/index
      :link-type: doc

      In-depth guides on Rich Messages, Checklists, and other advanced features.

   .. grid-item-card:: 📋 Changelog
      :link: changelog
      :link-type: doc

      Full history of every release with new features and bug fixes.

----

.. rubric:: A 30-Second Example

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_account")

   @app.on_message(filters.private & filters.text)
   async def echo(client, message):
       await message.reply(message.text)

   app.run()

----

.. rubric:: Why FTMGram?

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: ⚡ Ready
      :text-align: center

      ``pip install ftmgram`` — no configuration needed to get started.

   .. grid-item-card:: 🔌 Drop-in
      :text-align: center

      Replace ``pyrogram`` or ``kurigram`` imports with ``ftmgram``. Zero other changes.

   .. grid-item-card:: 🏆 Bot API 10.1
      :text-align: center

      Rich Messages, Checklists, Link media, Join-request queries — all covered.

   .. grid-item-card:: 🔒 Type-hinted
      :text-align: center

      Full type annotations for excellent IDE and editor support.

   .. grid-item-card:: ⚙️ Async-first
      :text-align: center

      Fully asynchronous. Synchronous usage is also supported out of the box.

   .. grid-item-card:: 🧩 Extensible
      :text-align: center

      Custom filters, middleware, and raw API access for advanced use-cases.

----

.. rubric:: Bot API 10.1 Coverage

.. list-table::
   :widths: 75 25
   :header-rows: 1

   * - Feature
     - Status
   * - Rich Messages — ``send_rich_message``, ``send_rich_message_draft``, ``edit_message_text``
     - ✅ Full
   * - RichText — 14 inline types (Bold, Italic, Url, Code, Marked, …)
     - ✅ Full
   * - RichBlock — 19+ block types (Paragraph, Photo, Video, Table, Slideshow, …)
     - ✅ Full
   * - Checklist media — ``MessageMediaType.CHECKLIST``, ``Checklist``, ``ChecklistTask``
     - ✅ Full
   * - Link poll media — ``MessageMediaType.LINK``, ``Link`` type
     - ✅ Full
   * - Chat join request queries — ``answer_chat_join_request_query``, ``send_chat_join_request_web_app``
     - ✅ Full
   * - ``User.supports_join_request_queries``, ``Chat.guard_bot``, ``ChatJoinRequest.query_id``
     - ✅ Full
   * - Owned star balance — ``get_owned_star_count``
     - ✅ Full

----

.. rubric:: Community

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 📢 Telegram Channel
      :link: https://t.me/ftmdeveloperz
      :link-type: url

      News, updates and releases — follow us on Telegram.

   .. grid-item-card:: 💬 Telegram Chat
      :link: https://t.me/ftmdevz
      :link-type: url

      Ask questions and get help from the community.

----

.. toctree::
   :hidden:
   :caption: Getting Started

   intro/index
   intro/install
   intro/quickstart
   intro/migration

.. toctree::
   :hidden:
   :caption: API Reference

   api/index
   api/client
   api/types
   api/filters
   api/enums

.. toctree::
   :hidden:
   :caption: Topics

   topics/index
   topics/rich-messages
   topics/checklists
   topics/poll-media

.. toctree::
   :hidden:
   :caption: Meta

   changelog
