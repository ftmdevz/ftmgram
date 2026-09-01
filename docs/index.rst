Welcome to FTMGram
==================

.. raw:: html

   <div class="ftm-hero-wrapper">
     <img src="_static/img/ftmgram_icon.svg" class="ftm-hero-logo" alt="FTMGram Logo" />
     <span class="ftm-hero-title">FTMGram</span>
   </div>

   <p align="center">
       <b>Telegram MTProto API Framework for Python</b>
       <br>
       <a href="https://ftmgram.ftmbotzx.dev">Homepage</a> •
       <a href="https://github.com/ftmdevz/ftmgram">Development</a> •
       <a href="releases/v3.5.1.html">v3.5.1 Release</a> •
       <a href="releases/index.html">All Releases</a> •
       <a href="https://t.me/ftmdeveloperz">News</a>
   </p>

.. note::

   **🎉 FTMGram v3.5.1 Released!**
   Featuring **Bot Chat History Scanning** (``get_bot_chat_history``), **Turbo Multi-Worker Media Engine** (``fast_download``), **In-Message Buttons** (``<tg-button-row>``), **AI Token Streaming** (``stream_text``), **Fluent RichMessageBuilder DSL**, **Batch Purge Admin Tools**, and **Checklists**.
   Read the :doc:`releases/v3.5.1` release notes for full details!

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_account")

   @app.on_message(filters.private)
   async def hello(client, message):
       await message.reply("Hello from FTMGram v3.5.1!")

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

  * :doc:`start/setup` — Setup guide.
  * :doc:`start/auth` — How to obtain your Telegram API ID and Hash.
  * :doc:`start/invoking` — Calling Telegram methods with your Client.
  * :doc:`start/updates` — Registering handlers and listening to updates.
  * :doc:`start/errors` — Error handling guide.
  * :doc:`start/examples/index` — Working code examples for common bot workflows.

* **API Reference**

  * :doc:`api/client` — Complete reference of all Client methods.
  * :doc:`api/methods/index` — Detailed index of all Client methods.
  * :doc:`api/types/index` — Detailed list of all Telegram types and models.
  * :doc:`api/bound-methods/index` — Convenience methods bound to types.
  * :doc:`api/enums/index` — Enumerations used across the API.
  * :doc:`api/handlers` — Update handlers.
  * :doc:`api/decorators` — Decorators for registering callbacks.
  * :doc:`api/filters` — Built-in and custom update filters.
  * :doc:`api/errors/index` — Telegram RPC and network errors.

* **Topics & Guides**

  * :doc:`topics/intext-buttons` — In-Message Buttons (``<tg-button-row>``).
  * :doc:`topics/streaming-drafts` — Live AI Response Token Streaming & Drafts.
  * :doc:`topics/ephemeral` — Ephemeral Messages & Overlays.
  * :doc:`topics/checklists` — Interactive Checklists & Task Lists.
  * :doc:`topics/text-formatting` — Markdown, HTML, and Entities.
  * :doc:`topics/smart-plugins` — Modular project layout for large bots.
  * :doc:`topics/storage-engines` — File SQLite, In-Memory, and Session Strings.
  * :doc:`topics/create-filters` — Creating custom update filters.
  * :doc:`topics/use-filters` — Using filters effectively.
  * :doc:`topics/more-on-updates` — Advanced update mechanisms.
  * :doc:`topics/client-settings` — Client configuration options.
  * :doc:`topics/speedups` — Maximizing network and CPU throughput.
  * :doc:`topics/proxy` — Using SOCKS5 and HTTP proxies.
  * :doc:`topics/scheduling` — Scheduling messages and tasks.
  * :doc:`topics/advanced-usage` — Advanced MTProto techniques.
  * :doc:`topics/mtproto-vs-botapi` — MTProto architecture vs HTTP Bot API.
  * :doc:`topics/debugging` — Debugging and logging.
  * :doc:`topics/test-servers` — Testing on Telegram test DCs.
  * :doc:`topics/voice-calls` — Voice call architecture.
  * :doc:`topics/serializing` — Object serialization.
  * :doc:`topics/synchronous` — Running synchronously.
  * :doc:`topics/message-identifiers` — Message ID schemas.
  * :doc:`topics/comparison-with-other-forks` — Comparison with other libraries.

* **Releases & Changelog**

  * :doc:`releases/v3.5.1` — Highlights and new methods in v3.5.1.
  * :doc:`releases/index` — Full historical release notes and changelog.

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

   start/setup
   start/auth
   start/invoking
   start/updates
   start/errors
   start/examples/index

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API Reference

   api/client
   api/methods/index
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

   topics/intext-buttons
   topics/streaming-drafts
   topics/ephemeral
   topics/checklists
   topics/text-formatting
   topics/smart-plugins
   topics/storage-engines
   topics/create-filters
   topics/use-filters
   topics/more-on-updates
   topics/client-settings
   topics/speedups
   topics/proxy
   topics/scheduling
   topics/advanced-usage
   topics/mtproto-vs-botapi
   topics/debugging
   topics/test-servers
   topics/voice-calls
   topics/serializing
   topics/synchronous
   topics/message-identifiers
   topics/comparison-with-other-forks

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Releases & Changelog

   releases/v3.5.1
   releases/index

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Meta

   faq/index
   support
