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
from ftmgram import types
from ..object import Object


class InputRichBlock(Object):
    """Base class for all input rich blocks available to format an outgoing rich message (Bot API 10.2 / 10.3)."""
    def __init__(self):
        super().__init__()


class InputRichBlockParagraph(InputRichBlock):
    def __init__(self, text: "types.RichText"):
        super().__init__()
        self.text = text


class InputRichBlockSectionHeading(InputRichBlock):
    def __init__(self, text: "types.RichText"):
        super().__init__()
        self.text = text


class InputRichBlockPreformatted(InputRichBlock):
    def __init__(self, text: "types.RichText", language: Optional[str] = None):
        super().__init__()
        self.text = text
        self.language = language


class InputRichBlockFooter(InputRichBlock):
    def __init__(self, text: "types.RichText"):
        super().__init__()
        self.text = text


class InputRichBlockDivider(InputRichBlock):
    def __init__(self):
        super().__init__()


class InputRichBlockMathematicalExpression(InputRichBlock):
    def __init__(self, expression: "types.RichText"):
        super().__init__()
        self.expression = expression


class InputRichBlockAnchor(InputRichBlock):
    def __init__(self, name: str):
        super().__init__()
        self.name = name


class InputRichBlockListItem(InputRichBlock):
    def __init__(self, text: "types.RichText", blocks: Optional[List["InputRichBlock"]] = None):
        super().__init__()
        self.text = text
        self.blocks = blocks or []


class InputRichBlockList(InputRichBlock):
    def __init__(self, items: List[InputRichBlockListItem], is_ordered: bool = False):
        super().__init__()
        self.items = items
        self.is_ordered = is_ordered


class InputRichBlockBlockQuotation(InputRichBlock):
    def __init__(self, text: "types.RichText", caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.text = text
        self.caption = caption


class InputRichBlockExpandableBlockQuotation(InputRichBlock):
    def __init__(self, text: "types.RichText", caption: Optional["types.RichBlockCaption"] = None, is_expanded: Optional[bool] = None):
        super().__init__()
        self.text = text
        self.caption = caption
        self.is_expanded = is_expanded


class InputRichBlockPullQuotation(InputRichBlock):
    def __init__(self, text: "types.RichText", caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.text = text
        self.caption = caption


class InputRichBlockCollage(InputRichBlock):
    def __init__(self, blocks: List[InputRichBlock], caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.blocks = blocks
        self.caption = caption


class InputRichBlockSlideshow(InputRichBlock):
    def __init__(self, blocks: List[InputRichBlock], caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.blocks = blocks
        self.caption = caption


class InputRichBlockTable(InputRichBlock):
    def __init__(
        self,
        cells: List[List["types.RichBlockTableCell"]],
        is_bordered: Optional[bool] = None,
        is_striped: Optional[bool] = None,
        is_compact: Optional[bool] = None,
        caption: Optional["types.RichBlockCaption"] = None,
    ):
        super().__init__()
        self.cells = cells
        self.is_bordered = is_bordered
        self.is_striped = is_striped
        self.is_compact = is_compact
        self.caption = caption


class InputRichBlockDetails(InputRichBlock):
    def __init__(self, title: "types.RichText", blocks: List[InputRichBlock], is_open: Optional[bool] = None):
        super().__init__()
        self.title = title
        self.blocks = blocks
        self.is_open = is_open


class InputRichBlockMap(InputRichBlock):
    def __init__(self, location: "types.Location", zoom: int = 16, caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.location = location
        self.zoom = zoom
        self.caption = caption


class InputRichBlockAnimation(InputRichBlock):
    def __init__(self, animation: Union[str, "types.Animation"], caption: Optional["types.RichBlockCaption"] = None, has_spoiler: Optional[bool] = None):
        super().__init__()
        self.animation = animation
        self.caption = caption
        self.has_spoiler = has_spoiler


class InputRichBlockAudio(InputRichBlock):
    def __init__(self, audio: Union[str, "types.Audio"], caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.audio = audio
        self.caption = caption


class InputRichBlockPhoto(InputRichBlock):
    def __init__(self, photo: Union[str, "types.Photo"], caption: Optional["types.RichBlockCaption"] = None, has_spoiler: Optional[bool] = None):
        super().__init__()
        self.photo = photo
        self.caption = caption
        self.has_spoiler = has_spoiler


class InputRichBlockVideo(InputRichBlock):
    def __init__(self, video: Union[str, "types.Video"], caption: Optional["types.RichBlockCaption"] = None, has_spoiler: Optional[bool] = None):
        super().__init__()
        self.video = video
        self.caption = caption
        self.has_spoiler = has_spoiler


class InputRichBlockVoiceNote(InputRichBlock):
    def __init__(self, voice_note: Union[str, "types.Voice"], caption: Optional["types.RichBlockCaption"] = None):
        super().__init__()
        self.voice_note = voice_note
        self.caption = caption


class InputRichBlockDocument(InputRichBlock):
    def __init__(self, document: Union[str, "types.Document"], caption: Optional["types.RichBlockCaption"] = None, has_spoiler: Optional[bool] = None):
        super().__init__()
        self.document = document
        self.caption = caption
        self.has_spoiler = has_spoiler


class InputRichBlockThinking(InputRichBlock):
    def __init__(self, text: "types.RichText"):
        super().__init__()
        self.text = text


class InputRichBlockButtons(InputRichBlock):
    def __init__(
        self,
        buttons: List[List["types.RichMessageButton"]],
        align: Optional[str] = None,
    ):
        super().__init__()
        self.buttons = buttons
        self.align = align
