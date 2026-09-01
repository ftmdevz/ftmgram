Invoking Raw MTProto
====================

FTMGram exposes the entire Telegram Type-Language (TL) schema via ``ftmgram.raw``.
You can invoke any MTProto function directly using ``app.invoke()``.

Example
-------

.. code-block:: python

   from ftmgram import Client, raw

   app = Client("my_account")

   async def main():
       async with app:
           config = await app.invoke(
               raw.functions.help.GetConfig()
           )
           print("Current Data Center:", config.this_dc)

   app.run(main())
