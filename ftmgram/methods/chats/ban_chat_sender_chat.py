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

from typing import Union

import ftmgram
from ftmgram import raw


class BanChatSenderChat:
    async def ban_chat_sender_chat(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        sender_chat_id: Union[int, str],
    ) -> bool:
        """Ban a channel chat in a supergroup or a channel.

        Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of
        their channels. The bot must be an administrator in the supergroup or channel for this to work and must have
        the appropriate administrator rights.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            sender_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target sender chat to ban.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.ban_chat_sender_chat(chat_id, sender_chat_id)
        """
        peer = await self.resolve_peer(chat_id)
        sender_peer = await self.resolve_peer(sender_chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            await self.invoke(
                raw.functions.channels.EditBanned(
                    channel=raw.types.InputChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash
                    ),
                    participant=sender_peer,
                    banned_rights=raw.types.ChatBannedRights(
                        until_date=0,
                        view_messages=True,
                        send_messages=True,
                        send_media=True,
                        send_stickers=True,
                        send_gifs=True,
                        send_games=True,
                        send_inline=True,
                        embed_links=True,
                    )
                )
            )
        else:
            raise ValueError("ban_chat_sender_chat is only supported for channels and supergroups")

        return True
