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

from typing import BinaryIO, Callable, Union

import ftmgram
from ftmgram import raw, types


class UploadStickerFile:
    async def upload_sticker_file(
        self: "ftmgram.Client",
        user_id: Union[int, str],
        sticker: Union[str, BinaryIO],
        sticker_format: str = "static",
        progress: Callable = None,
        progress_args: tuple = (),
    ) -> "types.Document":
        """Upload a .WEBP, .PNG, .TGS, or .WEBM file with a sticker for later use in
        :meth:`~ftmgram.Client.create_new_sticker_set` and :meth:`~ftmgram.Client.add_sticker_to_set`.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                User identifier of the sticker file owner.

            sticker (``str`` | ``BinaryIO``):
                A file with the sticker in .WEBP, .PNG, .TGS, or .WEBM format.
                Pass a file path as string or a binary file-like object.

            sticker_format (``str``, *optional*):
                Format of the sticker: "static", "animated", or "video". Defaults to "static".

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.

        Returns:
            :obj:`~ftmgram.types.Document`: On success, the uploaded document is returned.

        Example:
            .. code-block:: python

                doc = await app.upload_sticker_file(user_id, "sticker.webp")
        """
        file = await self.save_file(sticker, progress=progress, progress_args=progress_args)

        media = raw.types.InputMediaUploadedDocument(
            file=file,
            mime_type="image/webp" if sticker_format == "static" else (
                "application/x-tgsticker" if sticker_format == "animated" else "video/webm"
            ),
            attributes=[
                raw.types.DocumentAttributeFilename(
                    file_name="sticker.webp" if sticker_format == "static" else (
                        "sticker.tgs" if sticker_format == "animated" else "sticker.webm"
                    )
                )
            ]
        )

        r = await self.invoke(
            raw.functions.messages.UploadMedia(
                peer=await self.resolve_peer(user_id),
                media=media
            )
        )

        return types.Document._parse(self, r.document, {}, {}) if hasattr(r, 'document') else None
