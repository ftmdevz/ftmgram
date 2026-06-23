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

from typing import Optional, Union

import ftmgram
from ftmgram import raw


class VerifyChat:
    async def verify_chat(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        custom_description: Optional[str] = None,
    ) -> bool:
        """Verifies a chat on behalf of the organization which is represented by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            custom_description (``str``, *optional*):
                Custom description for the verification; 0-70 characters.
                Must be empty if the organization isn't allowed to provide a custom verification description.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.verify_chat(chat_id=-1001234567890)
                await app.verify_chat(chat_id="@mychat", custom_description="Official group")
        """

        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(chat_id),
                enabled=True,
                custom_description=custom_description,
            )
        )

        return bool(r)
