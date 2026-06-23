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
from typing import Iterable, List, Optional, Union

import ftmgram
from ftmgram import types


class CopyMessages:
    async def copy_messages(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: Union[int, Iterable[int]],
        message_thread_id: int = None,
        disable_notification: bool = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        remove_caption: bool = None,
        send_as: Optional[Union[int, str]] = None,
        reply_parameters: Optional["types.ReplyParameters"] = None,
    ) -> List["types.Message"]:
        """Copy multiple messages without a forward tag.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the source chat.

            message_ids (``int`` | Iterable of ``int``):
                An iterable of message identifiers in the source chat or a single message id.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.

            disable_notification (``bool``, *optional*):
                Sends the message silently.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the messages will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent messages from forwarding and saving.

            remove_caption (``bool``, *optional*):
                Pass True to copy messages without their captions.

            send_as (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the chat to send the messages as.

            reply_parameters (:obj:`~ftmgram.types.ReplyParameters`, *optional*):
                Describes reply parameters for the first message in the copied group.

        Returns:
            List of :obj:`~ftmgram.types.Message`: On success, a list of copied messages is returned.

        Example:
            .. code-block:: python

                await app.copy_messages(to_chat, from_chat, [1, 2, 3])
        """
        is_iterable = not isinstance(message_ids, int)
        message_ids = list(message_ids) if is_iterable else [message_ids]

        results = []
        for mid in message_ids:
            msg = await self.copy_message(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_id=mid,
                disable_notification=disable_notification,
                message_thread_id=message_thread_id,
                schedule_date=schedule_date,
                protect_content=protect_content,
                send_as=send_as,
                reply_parameters=reply_parameters,
            )
            if msg:
                results.append(msg)

        return results
