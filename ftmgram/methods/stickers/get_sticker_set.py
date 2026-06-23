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
from ftmgram import raw, types


class GetStickerSet:
    async def get_sticker_set(
        self: "ftmgram.Client",
        set_name: str,
    ) -> "types.StickerSet":
        """Get a sticker set by its short name.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            set_name (``str``):
                Short name of the sticker set that is used in t.me/addstickers/ URLs (e.g., *animals*).

        Returns:
            :obj:`~ftmgram.types.StickerSet`: On success, a StickerSet object is returned.

        Example:
            .. code-block:: python

                await app.get_sticker_set("animals")
        """
        r = await self.invoke(
            raw.functions.messages.GetStickerSet(
                stickerset=raw.types.InputStickerSetShortName(short_name=set_name),
                hash=0
            )
        )

        return types.StickerSet._parse(self, r)
