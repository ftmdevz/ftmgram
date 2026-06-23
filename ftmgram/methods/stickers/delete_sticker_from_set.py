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
from ftmgram.file_id import FileId


class DeleteStickerFromSet:
    async def delete_sticker_from_set(
        self: "ftmgram.Client",
        sticker: str,
    ) -> bool:
        """Delete a sticker from a set created by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            sticker (``str``):
                File identifier of the sticker.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_sticker_from_set("file_id")
        """
        file_id = FileId.decode(sticker)

        await self.invoke(
            raw.functions.stickers.RemoveStickerFromSet(
                sticker=raw.types.InputDocument(
                    id=file_id.media_id,
                    access_hash=file_id.access_hash,
                    file_reference=file_id.file_reference
                )
            )
        )

        return True
