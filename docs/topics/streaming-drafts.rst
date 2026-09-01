AI Response Streaming & Drafts
==============================

Live response streaming allows chatbots to stream generated text responses to the user in real-time.
FTMGram uses native MTProto ``sendMessageTextDraftAction`` via ``messages.setTyping`` with zero flood wait.

Key Features
------------

* **Zero Flood Wait**: Realtime token updates without triggering message edit rate limits.
* **Stop Button (can_stop=True)**: Displays native Telegram Stop button while generating.
* **Thinking Placeholder**: Use ``<tg-thinking>Thinking...</tg-thinking>`` while querying AI models.

Example
-------

.. code-block:: python

   import asyncio
   from ftmgram import Client
   from ftmgram.types import InputRichMessage

   app = Client("my_bot", bot_token="TOKEN")

   async def stream_demo(chat_id: int):
       async with app:
           draft_id = app.rnd_id()

           # 1. Native thinking placeholder
           await app.send_rich_message_draft(
               chat_id=chat_id,
               draft_id=draft_id,
               rich_message=InputRichMessage(html="<tg-thinking>Searching database...</tg-thinking>"),
               can_stop=True
           )
           await asyncio.sleep(1.2)

           # 2. Progressively stream text tokens
           tokens = ["Connecting to server...\n", "Retrieved 10 records.\n", "Analysis complete! 🚀"]
           streamed = ""
           for token in tokens:
               streamed += token
               await app.send_rich_message_draft(
                   chat_id=chat_id,
                   draft_id=draft_id,
                   rich_message=InputRichMessage(markdown=streamed),
                   can_stop=True
               )
               await asyncio.sleep(0.6)

           # 3. Finalize to permanent message
           await app.send_rich_message(
               chat_id=chat_id,
               rich_message=InputRichMessage(markdown=streamed)
           )

   app.run(stream_demo(123456789))
