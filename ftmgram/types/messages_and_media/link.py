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

from ftmgram import raw
from ..object import Object


class Link(Object):
    """Represents a link used as poll option media.

    Parameters:
        url (``str``):
            HTTP URL of the link.

        name (``str``, *optional*):
            Title of the link.

        photo_url (``str``, *optional*):
            URL of the thumbnail for the link.

        photo_width (``int``, *optional*):
            Width of the thumbnail.

        photo_height (``int``, *optional*):
            Height of the thumbnail.
    """

    def __init__(
        self,
        *,
        url: str,
        name: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
    ):
        super().__init__()

        self.url = url
        self.name = name
        self.photo_url = photo_url
        self.photo_width = photo_width
        self.photo_height = photo_height

    @staticmethod
    def _parse(media: "raw.types.MessageMediaWebPage") -> Optional["Link"]:
        if not isinstance(media, raw.types.MessageMediaWebPage):
            return None

        web_page = media.webpage
        if not isinstance(web_page, raw.types.WebPage):
            url = getattr(media, "url", None)
            if url:
                return Link(url=url)
            return None

        return Link(
            url=web_page.url,
            name=getattr(web_page, "title", None) or None,
            photo_url=getattr(web_page, "url", None),
        )
