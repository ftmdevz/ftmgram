Welcome to FTMGram
==================

.. image:: static/img/ftmgram_hero.svg
   :align: center
   :width: 270px
   :alt: FTMGramFTMGram

.. raw:: html

   <p align="center">
       <b>Telegram MTProto API Framework for Python</b>
       <br>
       <a href="https://ftmgram.ftmbotzx.dev">Homepage</a> •
       <a href="https://github.com/ftmdevz/ftmgram">Development</a> •
       <a href="releases/index.html">Releases</a> •
       <a href="https://t.me/ftmdeveloperz">News</a>
   </p>

.. note::

   **FTMGram v3.3.0** is an elegant, modern and asynchronous MTProto API framework with full **Bot API 10.3** support (In-Message Buttons, AI Response Streaming, Ephemeral Overlays, Checklists, Stars).

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_account")

   @app.on_message(filters.private)
   async def hello(client, message):
       await message.reply("Hello from FTMGram!")

   app.run()

**FTMGram** is a modern, elegant and asynchronous MTProto API framework. It enables you to easily
interact with the main Telegram API through a user account (custom client) or a bot identity (bot
API alternative) using Python.

How the Documentation is Organized
-----------------------------------

* **Quick Start**

  * :doc:`intro/quickstart` — An overview showing the first steps to take.
  * :doc:`intro/install` — Detailed instructions on how to install FTMGram.

* **Getting Started**

  * :doc:`start/auth` — How to obtain your Telegram API ID and Hash.
  * :doc:`start/invoking` — Calling Telegram methods with your Client.
  * :doc:`start/updates` — Registering handlers and listening to updates.
  * :doc:`start/filters` — Using and combining filters with ``&``, ``|``, ``~``.
  * :doc:`start/examples` — Working code examples for common bot workflows.

* **API Reference**

  * :doc:`api/client` — Complete reference of all Client methods.
  * :doc:`api/types/index` — Detailed list of all Telegram types and models.
  * :doc:`api/bound-methods/index` — Convenience methods bound to types.
  * :doc:`api/enums/index` — Enumerations used across the API.
  * :doc:`api/handlers` — Update handlers.
  * :doc:`api/decorators` — Decorators for registering callbacks.
  * :doc:`api/filters` — Built-in and custom update filters.
  * :doc:`api/errors/index` — Telegram RPC and network errors.

* **Topics & Guides**

  * :doc:`topics/rich-messages` — Structured Rich Messages (Bot API 10.3).
  * :doc:`topics/intext-buttons` — In-Message Buttons (``<tg-button-row>``).
  * :doc:`topics/streaming-drafts` — Live AI Response Token Streaming & Drafts.
  * :doc:`topics/ephemeral` — Ephemeral Messages & Overlays.
  * :doc:`topics/checklists` — Interactive Checklists & Task Lists.
  * :doc:`topics/text-formatting` — Markdown, HTML, and Entities.
  * :doc:`topics/smart-plugins` — Modular project layout for large bots.
  * :doc:`topics/storage-engines` — File SQLite, In-Memory, and Session Strings.

* **Meta**

  * :doc:`faq/index` — Frequently asked questions.
  * :doc:`support` — Support and Telegram community.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Introduction

   intro/quickstart
   intro/install

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Getting Started

   start/auth
   start/invoking
   start/updates
   start/filters
   start/examples

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API Reference

   api/client
   api/types/index
   api/bound-methods/index
   api/enums/index
   api/handlers
   api/decorators
   api/filters
   api/errors/index

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Topic Guides

   topics/rich-messages
   topics/intext-buttons
   topics/streaming-drafts
   topics/ephemeral
   topics/checklists
   topics/text-formatting
   topics/smart-plugins
   topics/storage-engines

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Meta

   faq/index
   support
