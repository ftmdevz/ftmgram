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


class RemoveChatVerification:
    async def remove_chat_verification(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Removes verification from a chat that is currently verified on behalf of the organization
        represented by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.remove_chat_verification(chat_id=-1001234567890)
        """

        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(chat_id),
                enabled=None,
            )
        )

        return bool(r)
