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

from typing import Union

import ftmgram
from ftmgram import raw, types


class ProcessChatProtectedContentDisableRequest:
    async def process_chat_protected_content_disable_request(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        request_message_id: int,
        enabled: bool
    ) -> Union["types.Message", bool]:
        """Processes a request to disable ``has_protected_content`` in a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            request_message_id (``int``):
                Identifier of the service message with the request.
                Must be of type :obj:`~ftmgram.types.ChatHasProtectedContentToggled`.

            enabled (``bool``):
                Pass True to approve the request; pass False to reject it.

        Returns:
            :obj:`~ftmgram.types.Message` | ``bool``: The service message on success,
            or True if no message object could be returned.

        Example:
            .. code-block:: python

                await app.process_chat_protected_content_disable_request(chat_id, msg_id, True)
        """
        r = await self.invoke(
            raw.functions.messages.ToggleNoForwards(
                peer=await self.resolve_peer(chat_id),
                enabled=enabled,
                request_msg_id=request_message_id
            )
        )
        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage, raw.types.UpdateNewChannelMessage)):
                return await types.Message._parse(
                    self,
                    i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    replies=self.fetch_replies
                )
        return True
