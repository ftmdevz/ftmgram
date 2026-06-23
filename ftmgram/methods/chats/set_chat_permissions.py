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

from typing import Set, Union

import ftmgram
from ftmgram import raw
from ftmgram import types


class SetChatPermissions:
    async def set_chat_permissions(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        permissions: "types.ChatPermissions" = None,
        use_independent_chat_permissions: bool = None,
    ) -> "types.Chat":
        """Set default chat permissions for all members.

        You must be an administrator in the group or a supergroup for this to work and must have the
        *can_restrict_members* admin rights.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            permissions (:obj:`~ftmgram.types.ChatPermissions`):
                New default chat permissions.

        Returns:
            :obj:`~ftmgram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                from ftmgram.types import ChatPermissions

                # Completely restrict chat
                await app.set_chat_permissions(chat_id)

                # Chat members can only send text messages and photos
                await app.set_chat_permissions(
                    chat_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_photos=True
                    )
                )
        """
        if permissions is None:
            permissions = types.ChatPermissions()

        r = await self.invoke(
            raw.functions.messages.EditChatDefaultBannedRights(
                peer=await self.resolve_peer(chat_id),
                banned_rights=permissions.write()
            )
        )

        return types.Chat._parse_chat(self, r.chats[0])
