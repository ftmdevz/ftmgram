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

from typing import Optional

from ..object import Object


class EphemeralMessageParameters(Object):
    """Describes parameters for sending an ephemeral message (Bot API 10.2 / 10.3).

    Parameters:
        receiver_user_id (``int``, *optional*):
            Identifier of the target user who can view the ephemeral message.

        callback_query_id (``str``, *optional*):
            Identifier of the callback query related to the ephemeral message.

        replace_callback_query_message (``bool``, *optional*):
            True, if the ephemeral message should replace the message with the callback query button.
    """

    def __init__(
        self,
        *,
        receiver_user_id: Optional[int] = None,
        callback_query_id: Optional[str] = None,
        replace_callback_query_message: Optional[bool] = None,
    ):
        super().__init__()

        self.receiver_user_id = receiver_user_id
        self.callback_query_id = callback_query_id
        self.replace_callback_query_message = replace_callback_query_message
