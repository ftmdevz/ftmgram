Poll Option Media
=================

Bot API 10.1 allows poll options to have attached media — a photo, animation,
or a link. FTMGram exposes this via ``MessageContent`` and the ``Link`` type.

Link Media in Poll Options
--------------------------

.. code-block:: python

   from ftmgram.enums import MessageMediaType

   @app.on_message(filters.poll)
   async def on_poll(client, message):
       poll = message.poll
       for option in poll.options:
           if option.media and option.media.type == MessageMediaType.LINK:
               link = option.media.link
               print(f"Option '{option.text}' has link: {link.url}")

The ``Link`` Type
-----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description
   * - ``url``
     - HTTP URL of the link (always present)
   * - ``name``
     - Optional title of the link
   * - ``photo_url``
     - Optional thumbnail URL

``MessageMediaType`` Values
----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Enum value
     - Media type
   * - ``PHOTO``
     - Photo
   * - ``VIDEO``
     - Video
   * - ``ANIMATION``
     - GIF/animation
   * - ``STICKER``
     - Sticker
   * - ``AUDIO``
     - Audio file
   * - ``VOICE``
     - Voice message
   * - ``DOCUMENT``
     - Document/file
   * - ``WEB_PAGE``
     - Rich web page preview
   * - ``POLL``
     - Poll
   * - ``CHECKLIST``
     - Checklist *(new in Bot API 10.1)*
   * - ``LINK``
     - Link media *(new in Bot API 10.1)*
   * - ``PAID_MEDIA``
     - Paid media
   * - ``GIVEAWAY``
     - Giveaway
   * - ``DICE``
     - Dice
