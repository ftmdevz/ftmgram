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

from datetime import datetime
from typing import Optional

import ftmgram
from ftmgram import types
from ..object import Object
from ..update import Update


class BotSubscriptionUpdated(Object, Update):
    """Represents an update about changes to a user payment subscription (Bot API 10.2).

    Parameters:
        user (:obj:`~ftmgram.types.User`):
            User who subscribed or whose subscription changed.

        chat (:obj:`~ftmgram.types.Chat`, *optional*):
            Chat associated with the subscription.

        subscription_until_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the subscription expires.

        is_canceled (``bool``, *optional*):
            True, if the subscription was canceled.
    """

    def __init__(
        self,
        *,
        client: "ftmgram.Client" = None,
        user: "types.User" = None,
        chat: Optional["types.Chat"] = None,
        subscription_until_date: Optional[datetime] = None,
        is_canceled: Optional[bool] = None,
    ):
        super().__init__(client)

        self.user = user
        self.chat = chat
        self.subscription_until_date = subscription_until_date
        self.is_canceled = is_canceled
