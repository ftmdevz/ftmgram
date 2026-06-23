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

import ftmgram
from ftmgram import raw


class UnpinGift:
    async def unpin_gift(
        self: "ftmgram.Client",
        business_connection_id: str,
        owned_gift_id: str,
    ) -> bool:
        """Unpin a gift for the given business account.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

            owned_gift_id (``str``):
                Unique identifier of the regular or upgraded gift that should be unpinned.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.unpin_gift(business_connection_id, gift_id)
        """
        await self.invoke(
            raw.functions.payments.ToggleStarGiftsPinnedToTop(
                peer=raw.types.InputPeerSelf(),
                stargift=[]
            ),
            business_connection_id=business_connection_id
        )

        return True
