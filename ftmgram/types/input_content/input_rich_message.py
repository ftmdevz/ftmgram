#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Optional, Union

from ftmgram import raw

from ..object import Object


class InputRichMessage(Object):
    """Describes a rich message to send (Bot API 10.1 - 10.3).

    Parameters:
        html (``str``, *optional*):
            Content of the rich message to send described using HTML formatting.
            See `rich message formatting options <https://core.telegram.org/bots/api#rich-message-formatting-options>`__ for more details.

        markdown (``str``, *optional*):
            Content of the rich message to send described using Markdown formatting.
            See `rich message formatting options <https://core.telegram.org/bots/api#rich-message-formatting-options>`__ for more details.

        blocks (List of :obj:`~ftmgram.types.InputRichBlock`, *optional*):
            List of rich blocks to format the message (Bot API 10.2).

        media (List of :obj:`~ftmgram.types.InputRichMessageMedia`, *optional*):
            List of media objects used in the rich message (Bot API 10.2).

        is_rtl (``bool``, *optional*):
            Pass *True* if the rich message must be shown right-to-left.

        skip_entity_detection (``bool``, *optional*):
            Pass *True* to skip automatic detection of entities
            (e.g., URLs, email addresses, username mentions, hashtags, cashtags, bot commands, or phone numbers) in the text.
    """

    def __init__(
        self,
        html: Optional[str] = None,
        markdown: Optional[str] = None,
        blocks: Optional[List["InputRichBlock"]] = None,
        media: Optional[List["InputRichMessageMedia"]] = None,
        is_rtl: Optional[bool] = None,
        skip_entity_detection: Optional[bool] = None,
    ):
        super().__init__()

        self.html = html
        self.markdown = markdown
        self.blocks = blocks
        self.media = media
        self.is_rtl = is_rtl
        self.skip_entity_detection = skip_entity_detection

    def write(self) -> "raw.base.InputRichMessage":
        if self.html:
            input_rich_message = raw.types.InputRichMessageHTML(
                html=self.html,
                rtl=self.is_rtl,
                noautolink=self.skip_entity_detection
            )
        elif self.markdown:
            input_rich_message = raw.types.InputRichMessageMarkdown(
                markdown=self.markdown,
                rtl=self.is_rtl,
                noautolink=self.skip_entity_detection
            )
        else:
            raise ValueError("You must provide markdown, html, or blocks in the rich message")

        return input_rich_message
