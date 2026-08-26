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
from ftmgram import types
from ..object import Object


class CommunityChatRemoved(Object):
    """Service message about a chat removed from a community (Bot API 10.2).

    Parameters:
        community (:obj:`~ftmgram.types.Community`, *optional*):
            The community.

        chat (:obj:`~ftmgram.types.Chat`, *optional*):
            The chat that was removed.

        user (:obj:`~ftmgram.types.User`, *optional*):
            User who removed the chat.
    """

    def __init__(
        self,
        *,
        client: "ftmgram.Client" = None,
        community: Optional["types.Community"] = None,
        chat: Optional["types.Chat"] = None,
        user: Optional["types.User"] = None,
    ):
        super().__init__(client)

        self.community = community
        self.chat = chat
        self.user = user
