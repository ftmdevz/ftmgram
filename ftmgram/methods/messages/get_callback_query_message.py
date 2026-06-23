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


class GetCallbackQueryMessage:
    async def get_callback_query_message(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        message_id: int,
        callback_query_id: int,
        replies: int = 1
    ) -> Optional["types.Message"]:
        """Returns the message that originated a callback query.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Message identifier in the chat.

            callback_query_id (``int``):
                Identifier of the callback query.

            replies (``int``, *optional*):
                The number of subsequent replies to fetch. Pass 0 for none, -1 for unlimited.
                Defaults to 1.

        Returns:
            :obj:`~ftmgram.types.Message`: On success, the message is returned.

        Example:
            .. code-block:: python

                msg = await app.get_callback_query_message(chat_id, message_id, callback_query_id)
        """
        peer = await self.resolve_peer(chat_id)
        ids = [raw.types.InputMessageCallbackQuery(id=message_id, query_id=callback_query_id)]

        if isinstance(peer, raw.types.InputPeerChannel):
            rpc = raw.functions.channels.GetMessages(channel=peer, id=ids)
        else:
            rpc = raw.functions.messages.GetMessages(id=ids)

        r = await self.invoke(rpc, sleep_threshold=-1)

        if replies < 0:
            replies = (1 << 31) - 1

        messages = await utils.parse_messages(
            self, r, is_scheduled=False, replies=replies
        )
        return messages[0] if messages else None
