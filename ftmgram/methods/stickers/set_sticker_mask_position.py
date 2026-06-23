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

from typing import Optional

import ftmgram
from ftmgram import raw, types
from ftmgram.file_id import FileId


class SetStickerMaskPosition:
    async def set_sticker_mask_position(
        self: "ftmgram.Client",
        sticker: str,
        mask_position: Optional["types.MaskPosition"] = None,
    ) -> bool:
        """Change the mask position of a mask sticker.

        The sticker must belong to a sticker set that was created by the bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            sticker (``str``):
                File identifier of the sticker.

            mask_position (:obj:`~ftmgram.types.MaskPosition`, *optional*):
                A MaskPosition object with the position where the mask should be placed on faces.
                Omit the parameter to remove the mask position.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                from ftmgram.types import MaskPosition
                pos = MaskPosition("forehead", 0.0, 0.0, 1.0)
                await app.set_sticker_mask_position("file_id", pos)
        """
        file_id = FileId.decode(sticker)

        mask_coords = None
        if mask_position is not None:
            mask_coords = mask_position.write() if hasattr(mask_position, 'write') else None

        await self.invoke(
            raw.functions.stickers.ChangeSticker(
                sticker=raw.types.InputDocument(
                    id=file_id.media_id,
                    access_hash=file_id.access_hash,
                    file_reference=file_id.file_reference
                ),
                mask_coords=mask_coords,
            )
        )

        return True
