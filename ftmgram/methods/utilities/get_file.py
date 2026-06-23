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
from ftmgram import types
from ftmgram.file_id import FileId


class GetFile:
    async def get_file(
        self: "ftmgram.Client",
        file_id: str,
    ) -> "types.File":
        """Get basic information about a file and prepare it for downloading.

        Bots can download files of up to 20 MB in size. The file can then be downloaded via
        :meth:`~ftmgram.Client.download_media`.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            file_id (``str``):
                File identifier to get information about.

        Returns:
            :obj:`~ftmgram.types.File`: On success, a File object is returned.

        Example:
            .. code-block:: python

                file = await app.get_file("BQACAgIAAxkBAAIBZmQ...")
                print(file.file_path)
        """
        decoded = FileId.decode(file_id)

        return types.File(
            file_id=file_id,
            file_unique_id=file_id,
            file_size=decoded.file_size if hasattr(decoded, 'file_size') else None,
        )
