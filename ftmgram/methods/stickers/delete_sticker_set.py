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


class DeleteStickerSet:
    async def delete_sticker_set(
        self: "ftmgram.Client",
        name: str,
    ) -> bool:
        """Delete a sticker set that was created by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            name (``str``):
                Sticker set name.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_sticker_set("my_set_by_bot")
        """
        await self.invoke(
            raw.functions.stickers.DeleteStickerSet(
                stickerset=raw.types.InputStickerSetShortName(short_name=name)
            )
        )

        return True
