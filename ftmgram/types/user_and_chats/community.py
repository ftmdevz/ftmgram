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

from typing import Optional

import ftmgram
from ..object import Object


class Community(Object):
    """Represents a Telegram Community (Bot API 10.2).

    Parameters:
        id (``int``):
            Unique identifier for this community.

        title (``str``):
            Title of the community.

        chat_count (``int``, *optional*):
            Number of chats linked in this community.
    """

    def __init__(
        self,
        *,
        client: "ftmgram.Client" = None,
        id: int,
        title: str,
        chat_count: Optional[int] = None,
    ):
        super().__init__(client)

        self.id = id
        self.title = title
        self.chat_count = chat_count
