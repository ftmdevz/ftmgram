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

from typing import Union

import ftmgram
from ftmgram import raw


class ReadBusinessMessage:
    async def read_business_message(
        self: "ftmgram.Client",
        business_connection_id: str,
        chat_id: Union[int, str],
        message_id: int,
    ) -> bool:
        """Marks incoming message as read on behalf of a business account.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection on behalf of which to read the message.

            chat_id (``int`` | ``str``):
                Unique identifier for the target chat.

            message_id (``int``):
                Identifier of the last message to be marked as read in the chat.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.read_business_message(business_connection_id, chat_id, message_id)
        """
        peer = await self.resolve_peer(chat_id)

        await self.invoke(
            raw.functions.messages.ReadHistory(
                peer=peer,
                max_id=message_id
            ),
            business_connection_id=business_connection_id
        )

        return True
