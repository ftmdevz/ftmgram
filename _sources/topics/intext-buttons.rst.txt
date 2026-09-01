In-Message Buttons
==================

Telegram **Bot API 10.3** introduced **In-Message Buttons**, allowing buttons to be embedded
directly inside the rich message card body rather than attached only to the bottom of the bubble.

HTML Tags & Attributes
----------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Tag / Attribute
     - Description
   * - ``<tg-button-row align="center">``
     - Container row holding 1 to 8 buttons. Alignment can be ``left``, ``center``, or ``right``.
   * - ``type="callback_data"``
     - Triggers a callback query event to your bot (``data="YOUR_PAYLOAD"``).
   * - ``type="url"``
     - Opens an external web link (``url="https://..."``).
   * - ``type="copy_text"``
     - One-tap clipboard copy button (``text="COPIED_TEXT"``).
   * - ``type="web_app"``
     - Launches a Telegram Mini App (``url="https://..."``).
   * - ``type="disabled"``
     - Unclickable button with optional popup reason.
   * - ``style="..."``
     - Button color: ``primary`` (blue), ``success`` (green), ``danger`` (red), ``link`` (transparent).

Example
-------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import InputRichMessage

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           html = """
           <b>Select your membership plan:</b>
           <tg-button-row align="center">
             <tg-button type="callback_data" style="primary" data="plan_basic">Basic ($5)</tg-button>
             <tg-button type="callback_data" style="success" data="plan_pro">Pro ($10)</tg-button>
             <tg-button type="callback_data" style="danger" data="plan_vip">VIP ($25)</tg-button>
           </tg-button-row>
           <tg-button-row align="center">
             <tg-button type="copy_text" text="FTM2026">📋 Copy Promo Code</tg-button>
             <tg-button type="disabled" style="primary">🔒 Enterprise (Sold Out)</tg-button>
           </tg-button-row>
           """
           await app.send_rich_message(
               chat_id=123456789,
               rich_message=InputRichMessage(html=html.strip())
           )

   app.run(main())
