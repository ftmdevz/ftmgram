Rich Messages
=============

Rich messages (also called article messages) are structured content messages
introduced in **Bot API 10.1**. They support styled text, photos, videos, tables,
slideshows, and more — similar to Telegram's Instant View format.

Sending a Rich Message
----------------------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import (
       InputRichMessage,
       InputRichMessageContent,
       RichText,
   )

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           await app.send_rich_message(
               chat_id=123456789,
               rich_message=InputRichMessage(
                   title=RichText.plain("My Article Title"),
                   content=[
                       InputRichMessageContent.paragraph(
                           text=RichText.concat([
                               RichText.bold("FTMGram"),
                               RichText.plain(" is the most up-to-date MTProto library."),
                           ])
                       ),
                   ]
               )
           )

   app.run(main())

RichText Types
--------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Type
     - Description
   * - ``RichText.plain(text)``
     - Plain text
   * - ``RichText.bold(text)``
     - **Bold** text
   * - ``RichText.italic(text)``
     - *Italic* text
   * - ``RichText.underline(text)``
     - Underlined text
   * - ``RichText.strikethrough(text)``
     - ~~Strikethrough~~ text
   * - ``RichText.code(text)``
     - Inline ``code``
   * - ``RichText.url(text, url)``
     - Hyperlink
   * - ``RichText.marked(text)``
     - Highlighted/marked text
   * - ``RichText.concat(items)``
     - Combine multiple RichText objects
   * - ``RichTextEmailAddress``
     - Clickable email address
   * - ``RichTextPhoneNumber``
     - Clickable phone number
   * - ``RichTextSubscript``
     - Subscript text
   * - ``RichTextSuperscript``
     - Superscript text

RichBlock Types
---------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Block
     - Description
   * - ``RichBlockParagraph``
     - A paragraph of styled text
   * - ``RichBlockPhoto``
     - An inline photo
   * - ``RichBlockVideo``
     - An inline video
   * - ``RichBlockAudio``
     - An audio player block
   * - ``RichBlockVoiceNote``
     - A voice note block
   * - ``RichBlockAnimation``
     - A GIF/animation block
   * - ``RichBlockTable``
     - A data table
   * - ``RichBlockList``
     - Ordered or unordered list
   * - ``RichBlockSlideshow``
     - Multi-image slideshow
   * - ``RichBlockCollage``
     - Photo collage
   * - ``RichBlockBlockQuotation``
     - Block quote
   * - ``RichBlockPreformatted``
     - Code/preformatted block
   * - ``RichBlockSectionHeading``
     - Section heading
   * - ``RichBlockDivider``
     - Horizontal divider
   * - ``RichBlockFooter``
     - Footer text
   * - ``RichBlockMap``
     - Embedded map
   * - ``RichBlockDetails``
     - Collapsible details section
   * - ``RichBlockMathematicalExpression``
     - LaTeX math expression
   * - ``RichBlockThinking``
     - AI thinking block

Editing a Rich Message
-----------------------

.. code-block:: python

   await app.edit_message_text(
       chat_id=123456789,
       message_id=42,
       rich_message=InputRichMessage(
           title=RichText.plain("Updated Title"),
       )
   )

Saving as Draft
---------------

.. code-block:: python

   await app.send_rich_message_draft(
       chat_id=123456789,
       rich_message=InputRichMessage(
           title=RichText.plain("Draft Article"),
       )
   )
