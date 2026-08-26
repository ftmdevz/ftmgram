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

from typing import BinaryIO, List, Optional, Union

import ftmgram
from ftmgram import enums, types
from .input_media import InputMedia


class InputMediaVoiceNote(InputMedia):
    """A voice note to be sent inside an album or rich message (Bot API 10.2).

    Parameters:
        media (``str`` | ``BinaryIO``):
            Voice file to send. Pass a file_id to send a file that exists on the Telegram servers (recommended),
            pass an HTTP URL for Telegram to get a file from the Internet, or pass a file path or a binary file
            object as file descriptor.

        caption (``str``, *optional*):
            Caption of the voice note to be sent, 0-1024 characters.

        parse_mode (:obj:`~ftmgram.enums.ParseMode`, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.

        caption_entities (List of :obj:`~ftmgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption.

        duration (``int``, *optional*):
            Duration of the voice note in seconds.

        waveform (``bytes``, *optional*):
            Waveform of the voice note.
    """

    def __init__(
        self,
        media: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        duration: Optional[int] = None,
        waveform: Optional[bytes] = None,
    ):
        super().__init__(
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )

        self.duration = duration
        self.waveform = waveform
