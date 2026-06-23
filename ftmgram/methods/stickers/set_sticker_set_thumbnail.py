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

from typing import BinaryIO, Optional, Set, Union

import ftmgram
from ftmgram import raw
from ftmgram.file_id import FileId


class SetStickerSetThumbnail:
    async def set_sticker_set_thumbnail(
        self: "ftmgram.Client",
        name: str,
        user_id: Union[int, str],
        thumbnail: Optional[Union[str, BinaryIO]] = None,
        format: str = "static",
    ) -> bool:
        """Set the thumbnail of a regular or mask sticker set.

        The format of the thumbnail file must match the format of the stickers in the set.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            name (``str``):
                Sticker set name.

            user_id (``int`` | ``str``):
                User identifier of the sticker set owner.

            thumbnail (``str`` | ``BinaryIO``, *optional*):
                A .WEBP or .PNG image with the thumbnail. Pass file_id as string to use existing file,
                or pass a file path/binary object to upload. Pass None to drop the thumbnail.

            format (``str``, *optional*):
                Format of the thumbnail: "static", "animated", or "video". Defaults to "static".

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_sticker_set_thumbnail("my_set_by_bot", user_id, "thumbnail.webp")
        """
        thumb_doc = None

        if thumbnail is not None:
            if isinstance(thumbnail, str):
                try:
                    file_id = FileId.decode(thumbnail)
                    thumb_doc = raw.types.InputDocument(
                        id=file_id.media_id,
                        access_hash=file_id.access_hash,
                        file_reference=file_id.file_reference
                    )
                except Exception:
                    file = await self.save_file(thumbnail)
                    r = await self.invoke(
                        raw.functions.messages.UploadMedia(
                            peer=await self.resolve_peer(user_id),
                            media=raw.types.InputMediaUploadedDocument(
                                file=file,
                                mime_type="image/webp",
                                attributes=[raw.types.DocumentAttributeFilename(file_name="thumbnail.webp")]
                            )
                        )
                    )
                    thumb_doc = raw.types.InputDocument(
                        id=r.document.id,
                        access_hash=r.document.access_hash,
                        file_reference=r.document.file_reference
                    )
            else:
                file = await self.save_file(thumbnail)
                r = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(user_id),
                        media=raw.types.InputMediaUploadedDocument(
                            file=file,
                            mime_type="image/webp",
                            attributes=[raw.types.DocumentAttributeFilename(file_name="thumbnail.webp")]
                        )
                    )
                )
                thumb_doc = raw.types.InputDocument(
                    id=r.document.id,
                    access_hash=r.document.access_hash,
                    file_reference=r.document.file_reference
                )

        await self.invoke(
            raw.functions.stickers.SetStickerSetThumb(
                stickerset=raw.types.InputStickerSetShortName(short_name=name),
                thumb=thumb_doc,
            )
        )

        return True
