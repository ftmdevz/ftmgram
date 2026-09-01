Ephemeral Messages
==================

Ephemeral messages allow bots to send temporary interactive overlays or replace messages
exclusively for the user who interacted with a button.

Example
-------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import EphemeralMessageParameters

   app = Client("my_bot", bot_token="TOKEN")

   @app.on_callback_query()
   async def handle_click(client, query):
       # Private in-place overlay visible only to clicking user
       await client.send_message(
           chat_id=query.message.chat.id,
           text="🤫 Secret VIP Code: **FTM-VIP-999**\nVisible only to you!",
           ephemeral_message_parameters=EphemeralMessageParameters(
               receiver_user_id=query.from_user.id,
               callback_query_id=query.id,
               replace_callback_query_message=True
           )
       )

   app.run()
