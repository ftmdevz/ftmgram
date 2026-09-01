In-Message Buttons
==================

Telegram **Bot API 10.3** introduced **In-Message Buttons**, allowing styled buttons to be embedded
directly inside the rich message card body using ``<tg-button-row>`` and ``<tg-button>`` tags.

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import InputRichMessage

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           html = """
           <b>Select your plan:</b>
           <tg-button-row align="center">
             <tg-button type="callback_data" style="primary" data="plan_basic">Basic ($5)</tg-button>
             <tg-button type="callback_data" style="success" data="plan_pro">Pro ($10)</tg-button>
             <tg-button type="callback_data" style="danger" data="plan_vip">VIP ($25)</tg-button>
           </tg-button-row>
           """
           await app.send_rich_message(123456789, InputRichMessage(html=html.strip()))

   app.run(main())
