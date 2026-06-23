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

from typing import Optional, Set

import ftmgram
from ftmgram import raw
from ftmgram.file_id import FileId


class SetCustomEmojiStickerSetThumbnail:
    async def set_custom_emoji_sticker_set_thumbnail(
        self: "ftmgram.Client",
        name: str,
        custom_emoji_id: Optional[str] = None,
    ) -> bool:
        """Set the thumbnail of a custom emoji sticker set.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            name (``str``):
                Sticker set name.

            custom_emoji_id (``str``, *optional*):
                Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail
                and use the first sticker as the thumbnail.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_custom_emoji_sticker_set_thumbnail("my_emoji_set_by_bot", "12345678901234567")
        """
        thumb_doc_id = None
        if custom_emoji_id:
            try:
                thumb_doc_id = int(custom_emoji_id)
            except (ValueError, TypeError):
                pass

        await self.invoke(
            raw.functions.stickers.SetStickerSetThumb(
                stickerset=raw.types.InputStickerSetShortName(short_name=name),
                thumb_document_id=thumb_doc_id,
            )
        )

        return True
