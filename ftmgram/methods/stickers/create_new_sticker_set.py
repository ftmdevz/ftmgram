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

from typing import List, Set, Type, Union

import ftmgram
from ftmgram import raw, types


class CreateNewStickerSet:
    async def create_new_sticker_set(
        self: "ftmgram.Client",
        user_id: Union[int, str],
        name: str,
        title: str,
        stickers: List["types.InputSticker"],
        sticker_format: str = "static",
        sticker_type: str = "regular",
        needs_repainting: bool = None,
    ) -> "types.StickerSet":
        """Create a new sticker set owned by a user.

        The bot must be an administrator in the chat for this to work.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                User identifier of the sticker set owner.

            name (``str``):
                Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., *animals*).
                Can contain only English letters, digits and underscores.
                Must begin with a letter, can't contain consecutive underscores and must end in "_by_<bot_username>".

            title (``str``):
                Sticker set title, 1-64 characters.

            stickers (List of :obj:`~ftmgram.types.InputSticker`):
                A list of 1-50 initial stickers to be added to the sticker set.

            sticker_format (``str``, *optional*):
                Format of stickers in the set: "static", "animated", or "video". Defaults to "static".

            sticker_type (``str``, *optional*):
                Type of stickers: "regular", "mask", or "custom_emoji". Defaults to "regular".

            needs_repainting (``bool``, *optional*):
                Pass True if stickers in the sticker set must be repainted to the color of text when used in messages,
                the accent color if used as emoji status, white on chat photos, or another appropriate color based on
                context; for custom emoji sticker sets only.

        Returns:
            :obj:`~ftmgram.types.StickerSet`: On success, the created StickerSet is returned.

        Example:
            .. code-block:: python

                await app.create_new_sticker_set(user_id, "my_set_by_bot", "My Sticker Set", stickers)
        """
        raw_stickers = []
        for s in stickers:
            if hasattr(s, 'write'):
                raw_stickers.append(s)
            else:
                raw_stickers.append(
                    raw.types.InputStickerSetItem(
                        document=raw.types.InputDocument(
                            id=s.file_id,
                            access_hash=0,
                            file_reference=b""
                        ),
                        emoji=getattr(s, 'emoji_list', ['🎯'])[0] if hasattr(s, 'emoji_list') else '🎯',
                    )
                )

        r = await self.invoke(
            raw.functions.stickers.CreateStickerSet(
                user_id=await self.resolve_peer(user_id),
                title=title,
                short_name=name,
                stickers=raw_stickers,
                masks=sticker_type == "mask" or None,
                emojis=sticker_type == "custom_emoji" or None,
                text_color=needs_repainting or None,
            )
        )

        return types.StickerSet._parse(self, r)
