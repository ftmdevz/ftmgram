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


class VerifyUser:
    async def verify_user(
        self: "ftmgram.Client",
        user_id: Union[int, str],
        custom_description: Optional[str] = None,
    ) -> bool:
        """Verifies a user on behalf of the organization which is represented by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

            custom_description (``str``, *optional*):
                Custom description for the verification; 0-70 characters.
                Must be empty if the organization isn't allowed to provide a custom verification description.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.verify_user(user_id=123456789)
                await app.verify_user(user_id=123456789, custom_description="Verified developer")
        """

        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(user_id),
                enabled=True,
                custom_description=custom_description,
            )
        )

        return bool(r)
