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


class GetOwnedGifts:
    async def get_owned_gifts(
        self: "ftmgram.Client",
        business_connection_id: str = None,
        user_id: Optional[Union[int, str]] = None,
        chat_id: Optional[Union[int, str]] = None,
        exclude_unsaved: bool = None,
        exclude_saved: bool = None,
        exclude_unlimited: bool = None,
        exclude_limited: bool = None,
        exclude_unique: bool = None,
        sort_by_value: bool = None,
        offset: str = "",
        limit: int = 100,
    ) -> List["types.SavedGift"]:
        """Returns the gifts saved to the given profile.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            business_connection_id (``str``, *optional*):
                Unique identifier of the business connection.

            user_id (``int`` | ``str``, *optional*):
                Unique identifier of the target user. Defaults to current user.

            chat_id (``int`` | ``str``, *optional*):
                Unique identifier of the chat (channel).

            exclude_unsaved (``bool``, *optional*):
                Pass True to exclude gifts that aren't saved to the profile.

            exclude_saved (``bool``, *optional*):
                Pass True to exclude gifts that are saved to the profile.

            exclude_unlimited (``bool``, *optional*):
                Pass True to exclude gifts without a limited number.

            exclude_limited (``bool``, *optional*):
                Pass True to exclude gifts with a limited number.

            exclude_unique (``bool``, *optional*):
                Pass True to exclude unique gifts.

            sort_by_value (``bool``, *optional*):
                Pass True to sort results by gift value instead of send date.

            offset (``str``, *optional*):
                Offset of the first result to return.

            limit (``int``, *optional*):
                Maximum number of gifts to return; 1-100. Defaults to 100.

        Returns:
            List of :obj:`~ftmgram.types.SavedGift`: On success, a list of saved gifts is returned.

        Example:
            .. code-block:: python

                gifts = await app.get_owned_gifts()
        """
        if chat_id:
            peer = await self.resolve_peer(chat_id)
        elif user_id:
            peer = await self.resolve_peer(user_id)
        else:
            peer = raw.types.InputPeerSelf()

        r = await self.invoke(
            raw.functions.payments.GetSavedStarGifts(
                peer=peer,
                offset=offset,
                limit=limit,
                exclude_unsaved=exclude_unsaved,
                exclude_saved=exclude_saved,
                exclude_unlimited=exclude_unlimited,
                exclude_limited=exclude_limited,
                exclude_unique=exclude_unique,
                sort_by_value=sort_by_value,
            ),
            business_connection_id=business_connection_id
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return types.List([
            await types.SavedGift._parse(self, gift, users=users, chats=chats)
            for gift in r.gifts
        ])
