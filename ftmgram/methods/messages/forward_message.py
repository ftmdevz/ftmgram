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
from typing import Optional, Union

import ftmgram
from ftmgram import types


class ForwardMessage:
    async def forward_message(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        disable_notification: bool = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        send_as: Union[int, str] = None,
        reply_parameters: Optional["types.ReplyParameters"] = None,
    ) -> "types.Message":
        """Forward a single message.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the source chat.

            message_id (``int``):
                Message identifier in the chat specified in *from_chat_id*.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.

            disable_notification (``bool``, *optional*):
                Sends the message silently.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the forwarded message from forwarding and saving.

            send_as (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the chat to send the message as.

            reply_parameters (:obj:`~ftmgram.types.ReplyParameters`, *optional*):
                Describes reply parameters for the message that is being sent.

        Returns:
            :obj:`~ftmgram.types.Message`: On success, the forwarded message is returned.

        Example:
            .. code-block:: python

                await app.forward_message(to_chat, from_chat, 123)
        """
        result = await self.forward_messages(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            schedule_date=schedule_date,
            protect_content=protect_content,
            send_as=send_as,
            reply_parameters=reply_parameters,
        )
        if isinstance(result, list):
            return result[0] if result else None
        return result
