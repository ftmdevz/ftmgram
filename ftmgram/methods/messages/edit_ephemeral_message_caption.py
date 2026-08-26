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


class EditEphemeralMessageCaption:
    async def edit_ephemeral_message_caption(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        message_id: int,
        caption: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
    ) -> Union["types.Message", bool]:
        """Edit the caption of an ephemeral message (Bot API 10.2 / 10.3).

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Ephemeral message identifier.

            caption (``str``):
                New caption of the message.

            parse_mode (:obj:`~ftmgram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.

            caption_entities (List of :obj:`~ftmgram.types.MessageEntity`, *optional*):
                List of special entities that appear in caption.

            show_caption_above_media (``bool``, *optional*):
                True, if caption should be shown above the message media (Bot API 10.3).

            reply_markup (:obj:`~ftmgram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~ftmgram.types.Message` | ``bool``: On success, the edited Message is returned.
        """
        return await self.edit_message_caption(
            chat_id=chat_id,
            message_id=message_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )
