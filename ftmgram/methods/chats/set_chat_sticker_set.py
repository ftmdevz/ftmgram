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


class SetChatStickerSet:
    async def set_chat_sticker_set(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        sticker_set_name: str,
    ) -> bool:
        """Set a new group sticker set for a supergroup.

        The bot must be an administrator in the chat for this to work and must have the appropriate administrator
        rights. Use the field *can_set_sticker_set* optionally returned in :meth:`~ftmgram.Client.get_chat` requests
        to check if the bot can use this method.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            sticker_set_name (``str``):
                Name of the sticker set to be set as the group sticker set.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_chat_sticker_set(chat_id, "my_sticker_set")
        """
        peer = await self.resolve_peer(chat_id)

        if not isinstance(peer, raw.types.InputPeerChannel):
            raise ValueError("set_chat_sticker_set is only supported for supergroups and channels")

        await self.invoke(
            raw.functions.channels.SetStickers(
                channel=raw.types.InputChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash
                ),
                stickerset=raw.types.InputStickerSetShortName(
                    short_name=sticker_set_name
                )
            )
        )

        return True
