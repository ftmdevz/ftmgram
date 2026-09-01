AI Response Streaming & Drafts
==============================

Live response streaming allows chatbots to stream generated text responses token-by-token in real-time.
FTMGram uses native MTProto ``sendMessageTextDraftAction`` via ``messages.setTyping`` with zero flood wait.

.. code-block:: python

   import asyncio
   from ftmgram import Client
   from ftmgram.types import InputRichMessage

   app = Client("my_bot", bot_token="TOKEN")

   async def stream_demo(chat_id: int):
       async with app:
           draft_id = app.rnd_id()

           # Native thinking placeholder
           await app.send_rich_message_draft(
               chat_id=chat_id,
               draft_id=draft_id,
               rich_message=InputRichMessage(html="<tg-thinking>Searching database...</tg-thinking>"),
               can_stop=True
           )
           await asyncio.sleep(1.0)

           # Progressive streaming
           tokens = ["Thinking...\n", "Found 3 results.\n", "Complete! 🚀"]
           streamed = ""
           for token in tokens:
               streamed += token
               await app.send_rich_message_draft(
                   chat_id=chat_id,
                   draft_id=draft_id,
                   rich_message=InputRichMessage(markdown=streamed),
                   can_stop=True
               )
               await asyncio.sleep(0.5)

   app.run(stream_demo(123456789))
