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

from typing import BinaryIO, Optional, Union

from ..object import Object


class InputRichMessageMedia(Object):
    """Explicitly specifies media used in markdown or html formatting when sending a rich message (Bot API 10.2).

    Parameters:
        media (``str`` | ``BinaryIO``):
            File to send or file_id / URL.

        type (``str``, *optional*):
            Type of the media (e.g. "photo", "video", "document", "audio", "voice", "animation").

        file_name (``str``, *optional*):
            File name for documents.
    """

    def __init__(
        self,
        media: Union[str, BinaryIO],
        type: str = "auto",
        file_name: Optional[str] = None,
    ):
        super().__init__()

        self.media = media
        self.type = type
        self.file_name = file_name
