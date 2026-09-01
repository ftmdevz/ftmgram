Handlers & Decorators
=====================

Handlers process incoming Telegram updates. You can register handlers using client decorators or through ``app.add_handler()``.

Available Handlers
------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Decorator / Handler
     - Description
   * - ``@app.on_message(filters)``
     - Handles new incoming or outgoing messages.
   * - ``@app.on_callback_query(filters)``
     - Handles inline button clicks.
   * - ``@app.on_inline_query(filters)``
     - Handles inline search queries.
   * - ``@app.on_chosen_inline_result(filters)``
     - Handles chosen inline results.
   * - ``@app.on_edited_message(filters)``
     - Handles message edits.
   * - ``@app.on_deleted_messages()``
     - Handles message deletion events.
   * - ``@app.on_chat_member_updated()``
     - Handles member join, leave, promotion, and demotion events.
   * - ``@app.on_chat_join_request()``
     - Handles join requests in private channels/groups.
   * - ``@app.on_message_generation_stopped()``
     - Handles when a user taps Stop during live AI text streaming.
   * - ``@app.on_raw_update()``
     - Low-level handler receiving unprocessed MTProto updates.

Example
-------

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_bot")

   @app.on_message(filters.command("start"))
   async def start_handler(client, message):
       await message.reply("Welcome to FTMGram!")

   @app.on_callback_query()
   async def callback_handler(client, query):
       await query.answer("Received click!")
