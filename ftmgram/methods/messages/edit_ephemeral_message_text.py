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
from ftmgram import enums, types


class EditEphemeralMessageText:
    async def edit_ephemeral_message_text(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        message_id: int,
        text: Optional[str] = None,
        rich_message: Optional["types.InputRichMessage"] = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
    ) -> Union["types.Message", bool]:
        """Edit the text of an ephemeral message (Bot API 10.2 / 10.3).

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Ephemeral message identifier.

            text (``str``, *optional*):
                New text of the message.

            rich_message (:obj:`~ftmgram.types.InputRichMessage`, *optional*):
                New rich message content (Bot API 10.3).

            parse_mode (:obj:`~ftmgram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.

            entities (List of :obj:`~ftmgram.types.MessageEntity`, *optional*):
                List of special entities that appear in message text.

            reply_markup (:obj:`~ftmgram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~ftmgram.types.Message` | ``bool``: On success, the edited Message is returned, otherwise True.
        """
        if rich_message:
            return await self.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                rich_message=rich_message,
                reply_markup=reply_markup,
            )
        return await self.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            reply_markup=reply_markup,
        )
