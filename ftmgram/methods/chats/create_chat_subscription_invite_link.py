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
from ftmgram import raw, types


class CreateChatSubscriptionInviteLink:
    async def create_chat_subscription_invite_link(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        subscription_period: int,
        subscription_price: int,
        name: str = None,
    ) -> "types.ChatInviteLink":
        """Create a subscription invite link for a channel chat.

        The bot must be an administrator in the chat for this to work and must have the
        *can_invite_users* administrator rights.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel chat.

            subscription_period (``int``):
                The number of seconds the subscription will be active for before the next payment.
                Currently, it must always be 2592000 (30 days).

            subscription_price (``int``):
                The amount of Telegram Stars a user must pay initially and after each subsequent subscription period
                to be a member of the chat; 1-2500.

            name (``str``, *optional*):
                Invite link name; 0-32 characters.

        Returns:
            :obj:`~ftmgram.types.ChatInviteLink`: On success, the new invite link is returned.

        Example:
            .. code-block:: python

                link = await app.create_chat_subscription_invite_link(chat_id, 2592000, 100)
        """
        r = await self.invoke(
            raw.functions.messages.ExportChatInvite(
                peer=await self.resolve_peer(chat_id),
                title=name,
                subscription_pricing=raw.types.StarsSubscriptionPricing(
                    period=subscription_period,
                    amount=subscription_price
                )
            )
        )

        return types.ChatInviteLink._parse(self, r, {}, {})
