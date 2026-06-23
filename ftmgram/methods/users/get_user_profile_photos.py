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

from typing import List, Optional, Union

import ftmgram
from ftmgram import raw, types


class GetUserProfilePhotos:
    async def get_user_profile_photos(
        self: "ftmgram.Client",
        user_id: Union[int, str],
        offset: int = 0,
        limit: int = 0,
    ) -> Optional[List["types.Photo"]]:
        """Get a list of profile pictures for a user.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier of the target user.

            offset (``int``, *optional*):
                Sequential number of the first photo to be returned.
                By default, all photos are returned.

            limit (``int``, *optional*):
                Limits the number of photos to be retrieved.
                Values between 1-100 are accepted. Defaults to 100.

        Returns:
            List of :obj:`~ftmgram.types.Photo`: On success, a list of photos is returned.

        Example:
            .. code-block:: python

                photos = await app.get_user_profile_photos(user_id)
                print(f"Total photos: {len(photos)}")
        """
        peer = await self.resolve_peer(user_id)

        if not isinstance(peer, (raw.types.InputPeerUser, raw.types.InputPeerSelf)):
            peer = raw.types.InputUser(user_id=peer.user_id, access_hash=getattr(peer, 'access_hash', 0)) if hasattr(peer, 'user_id') else raw.types.InputUserSelf()

        r = await self.invoke(
            raw.functions.photos.GetUserPhotos(
                user_id=peer if isinstance(peer, (raw.types.InputPeerSelf,)) else raw.types.InputUser(
                    user_id=peer.user_id if hasattr(peer, 'user_id') else 0,
                    access_hash=peer.access_hash if hasattr(peer, 'access_hash') else 0
                ),
                offset=offset,
                max_id=0,
                limit=limit or 100
            )
        )

        return types.List([types.Photo._parse(self, photo, {}) for photo in r.photos if photo])
