Quick Start
===========

This guide gets you up and running with FTMGram in minutes.

Installation
------------

.. code-block:: bash

   pip install ftmgram

Your First Bot
--------------

.. code-block:: python

   from ftmgram import Client, filters

   app = Client("my_bot", bot_token="YOUR_BOT_TOKEN")

   @app.on_message(filters.private & filters.text)
   async def echo(client, message):
       await message.reply(message.text)

   app.run()

Your First User Client
----------------------

.. code-block:: python

   from ftmgram import Client

   app = Client("my_account")

   async def main():
       async with app:
           me = await app.get_me()
           print(f"Logged in as: {me.first_name}")

   app.run(main())

Sending a Rich Message (Bot API 10.1)
--------------------------------------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import InputRichMessage, RichText

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           await app.send_rich_message(
               chat_id=123456789,
               rich_message=InputRichMessage(
                   title=RichText.plain("My Article"),
               )
           )

   app.run(main())

Sending a Checklist
-------------------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import InputChecklistTask

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           await app.send_message(
               chat_id=123456789,
               text="Shopping list",
               checklist=[
                   InputChecklistTask(text="Milk"),
                   InputChecklistTask(text="Eggs"),
                   InputChecklistTask(text="Bread"),
               ]
           )

   app.run(main())

Answering a Chat Join Request Query
------------------------------------

.. code-block:: python

   from ftmgram import Client

   app = Client("my_bot", bot_token="TOKEN")

   @app.on_chat_join_request()
   async def handle_join(client, request):
       if request.query_id:
           await client.answer_chat_join_request_query(
               query_id=request.query_id,
               ok=True,
               title="Welcome!"
           )

   app.run()

Next Steps
----------

- Read the :doc:`installing` guide for advanced install options.
- See :doc:`topics/rich-messages` for full rich message API.
- See :doc:`changelog` for what's new in v3.0.0.
