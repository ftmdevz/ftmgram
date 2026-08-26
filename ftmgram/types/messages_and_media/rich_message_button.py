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

from typing import Optional, Union

import ftmgram
from ftmgram import enums, types
from ..object import Object


class RichMessageButton(Object):
    """Represents a button in a RichMessage or RichBlockButtons (Bot API 10.3).

    Parameters:
        text (``str``):
            Label text on the button.

        url (``str``, *optional*):
            HTTP or tg:// URL to be opened when the button is pressed.

        callback_data (``str`` | ``bytes``, *optional*):
            Data to be sent in a callback query to the bot when the button is pressed.

        web_app (:obj:`~ftmgram.types.WebAppInfo`, *optional*):
            Description of the Web App that will be launched.

        login_url (:obj:`~ftmgram.types.LoginUrl`, *optional*):
            An HTTP URL used to automatically authorize the user.

        switch_inline_query (``str``, *optional*):
            Inline query prompt in user's chats.

        switch_inline_query_current_chat (``str``, *optional*):
            Inline query prompt in the current chat.

        copy_text (``str``, *optional*):
            Text to copy to clipboard.

        style (:obj:`~ftmgram.enums.ButtonStyle`, *optional*):
            Style of the button.
    """

    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[Union[str, bytes]] = None,
        web_app: Optional["types.WebAppInfo"] = None,
        login_url: Optional["types.LoginUrl"] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        copy_text: Optional[str] = None,
        style: "enums.ButtonStyle" = enums.ButtonStyle.DEFAULT,
    ):
        super().__init__()

        self.text = str(text)
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.copy_text = copy_text
        self.style = style
