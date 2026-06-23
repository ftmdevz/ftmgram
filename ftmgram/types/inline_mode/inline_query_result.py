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

from uuid import uuid4

import ftmgram
from ftmgram import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~ftmgram.types.InlineQueryResultCachedAudio`
    - :obj:`~ftmgram.types.InlineQueryResultCachedDocument`
    - :obj:`~ftmgram.types.InlineQueryResultCachedAnimation`
    - :obj:`~ftmgram.types.InlineQueryResultCachedPhoto`
    - :obj:`~ftmgram.types.InlineQueryResultCachedSticker`
    - :obj:`~ftmgram.types.InlineQueryResultCachedVideo`
    - :obj:`~ftmgram.types.InlineQueryResultCachedVoice`
    - :obj:`~ftmgram.types.InlineQueryResultArticle`
    - :obj:`~ftmgram.types.InlineQueryResultAudio`
    - :obj:`~ftmgram.types.InlineQueryResultContact`
    - :obj:`~ftmgram.types.InlineQueryResultDocument`
    - :obj:`~ftmgram.types.InlineQueryResultAnimation`
    - :obj:`~ftmgram.types.InlineQueryResultLocation`
    - :obj:`~ftmgram.types.InlineQueryResultPhoto`
    - :obj:`~ftmgram.types.InlineQueryResultVenue`
    - :obj:`~ftmgram.types.InlineQueryResultVideo`
    - :obj:`~ftmgram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "ftmgram.Client"):
        pass
