#  Ftmgram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present <https://github.com/TelegramPlayGround>
#
#  This file is part of Ftmgram.
#
#  Ftmgram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Ftmgram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Ftmgram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import List

import ftmgram


class DeleteBusinessStory:
    async def delete_business_story(
        self: "ftmgram.Client",
        business_connection_id: str,
        story_id: int,
    ) -> List[int]:
        """Deletes a story previously posted by the bot on behalf of a managed business account.

        Requires the can_manage_stories business bot right.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

            story_id (``int``):
                Unique identifier of the story to delete.

        Returns:
            List of ``int``: List of deleted story IDs.

        Example:
            .. code-block:: python

                await app.delete_business_story(business_connection_id, story_id)
        """
        if not business_connection_id:
            raise ValueError("business_connection_id is required")

        business_connection = self.business_user_connection_cache[business_connection_id]
        if business_connection is None:
            business_connection = await self.get_business_connection(business_connection_id)

        return await self.delete_stories(
            chat_id=business_connection.user_chat_id,
            story_ids=story_id
        )
