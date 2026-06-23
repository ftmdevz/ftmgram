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


class AddStickerToSet:
    async def add_sticker_to_set(
        self: "ftmgram.Client",
        name: str,
        sticker: "types.InputSticker",
    ) -> "types.StickerSet":
        """Add a new sticker to a set created by the bot.

        The format of the added sticker must match the format of the other stickers in the set.
        Emoji sticker sets can have up to 200 stickers. Animated and video sticker sets can have up to 50 stickers.
        Static sticker sets can have up to 120 stickers.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            name (``str``):
                Sticker set name.

            sticker (:obj:`~ftmgram.types.InputSticker`):
                An InputSticker object with information about the added sticker.

        Returns:
            :obj:`~ftmgram.types.StickerSet`: On success, the sticker set is returned.

        Example:
            .. code-block:: python

                await app.add_sticker_to_set("my_set_by_bot", sticker)
        """
        if hasattr(sticker, 'write'):
            raw_sticker = sticker
        else:
            raw_sticker = raw.types.InputStickerSetItem(
                document=raw.types.InputDocument(
                    id=sticker.file_id,
                    access_hash=0,
                    file_reference=b""
                ),
                emoji=getattr(sticker, 'emoji_list', ['🎯'])[0] if hasattr(sticker, 'emoji_list') else '🎯',
            )

        r = await self.invoke(
            raw.functions.stickers.AddStickerToSet(
                stickerset=raw.types.InputStickerSetShortName(short_name=name),
                sticker=raw_sticker
            )
        )

        return types.StickerSet._parse(self, r)
