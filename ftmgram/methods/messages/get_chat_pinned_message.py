#  Ftmgram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present <https://github.com/TelegramPlayGround>
#
#  This file is part of Ftmgram.
#
#  Ftmgram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Ftmgram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Ftmgram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Union, Optional

import ftmgram
from ftmgram import raw, types, utils


class GetChatPinnedMessage:
    async def get_chat_pinned_message(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        replies: int = 1
    ) -> Optional["types.Message"]:
        """Returns the newest pinned message in a supergroup or channel.

        Use :meth:`~ftmgram.Client.search_messages` to return all pinned messages.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target supergroup or channel.

            replies (``int``, *optional*):
                The number of subsequent replies to fetch. Pass 0 for none, -1 for unlimited.
                Defaults to 1.

        Returns:
            :obj:`~ftmgram.types.Message`: On success, the pinned message is returned.

        Raises:
            ValueError: If chat_id does not belong to a supergroup or channel.

        Example:
            .. code-block:: python

                pinned = await app.get_chat_pinned_message(chat_id)
        """
        peer = await self.resolve_peer(chat_id)

        if not isinstance(peer, raw.types.InputPeerChannel):
            raise ValueError("chat_id must belong to a supergroup or channel.")

        rpc = raw.functions.channels.GetMessages(
            channel=peer,
            id=[raw.types.InputMessagePinned()]
        )
        r = await self.invoke(rpc, sleep_threshold=-1)

        if replies < 0:
            replies = (1 << 31) - 1

        messages = await utils.parse_messages(
            self, r, is_scheduled=False, replies=replies
        )
        return messages[0] if messages else None
