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

from typing import Iterable, List, Optional, Union

import ftmgram
from ftmgram import raw, types, utils


class GetRepliedMessage:
    async def get_replied_message(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        message_ids: Union[int, Iterable[int]],
        replies: int = 1
    ) -> Optional["types.Message"]:
        """Returns the message that a given message is replying to.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            message_ids (``int`` | Iterable of ``int``):
                Pass a single message identifier or an iterable of message IDs to get
                the replied-to message for each.

            replies (``int``, *optional*):
                The number of subsequent replies to fetch. Pass 0 for none, -1 for unlimited.
                Defaults to 1.

        Returns:
            :obj:`~ftmgram.types.Message` | List of :obj:`~ftmgram.types.Message`: On success.

        Example:
            .. code-block:: python

                replied = await app.get_replied_message(chat_id, message_id)
        """
        peer = await self.resolve_peer(chat_id)
        is_iterable = utils.is_list_like(message_ids)
        ids = list(message_ids) if is_iterable else [message_ids]
        ids = [raw.types.InputMessageReplyTo(id=i) for i in ids]

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
        return messages if is_iterable else (messages[0] if messages else None)
