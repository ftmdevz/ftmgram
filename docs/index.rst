FTMGram
=======

.. image:: _static/logo.png
   :align: center
   :width: 160px
   :alt: FTMGram

|

.. rst-class:: lead

   **Elegant, modern and asynchronous Telegram MTProto API framework in Python — for users and bots.**

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 🚀 Quick Start
      :link: quickstart
      :link-type: doc

      Get your first bot running in minutes.

   .. grid-item-card:: 📦 Installing
      :link: installing
      :link-type: doc

      Install FTMGram via pip or from GitHub.

   .. grid-item-card:: 📋 Changelog
      :link: changelog
      :link-type: doc

      See what's new in every release.

----

What is FTMGram?
----------------

**FTMGram** is an actively maintained fork of Pyrogram with complete
**Bot API 10.1** (June 2026) support. It is a drop-in replacement for Pyrogram
and KuriGram — migrate with zero code changes.

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_account")

   @app.on_message(filters.private)
   async def hello(client, message):
       await message.reply("Hello from FTMGram!")

   app.run()

----

Bot API 10.1 Coverage
---------------------

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Feature
     - Status
   * - Rich Messages — ``sendRichMessage``, ``sendRichMessageDraft``, ``editMessageText``
     - ✅
   * - RichText — 14 inline types (Bold, Italic, Url, Code, Marked, …)
     - ✅
   * - RichBlock — 19 block types (Paragraph, Photo, Video, Table, Slideshow, …)
     - ✅
   * - Checklist media — ``MessageMediaType.CHECKLIST``
     - ✅
   * - Link poll media — ``MessageMediaType.LINK``, ``Link`` type
     - ✅
   * - Chat join request queries — ``answerChatJoinRequestQuery``, ``sendChatJoinRequestWebApp``
     - ✅
   * - ``User.supports_join_request_queries``, ``Chat.guard_bot``, ``ChatJoinRequest.query_id``
     - ✅
   * - Owned star balance — ``get_owned_star_count``
     - ✅

----

Key Features
------------

* **Ready** — ``pip install ftmgram`` and start building immediately.
* **Easy** — Clean Pythonic API that hides MTProto complexity.
* **Elegant** — Low-level details abstracted into intuitive high-level types.
* **Fast** — Powered by `TgCrypto <https://github.com/pyrogram/tgcrypto>`_, a C-level crypto library.
* **Type-hinted** — Full annotations for excellent IDE support.
* **Async** — Fully asynchronous; synchronous usage also supported.
* **Bot API 10.1 complete** — Latest Telegram features covered on day one.

----

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started

   installing
   quickstart

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Reference

   topics/rich-messages
   topics/checklists
   topics/poll-media
   changelog
