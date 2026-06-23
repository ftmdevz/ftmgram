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

import ftmgram
from ftmgram.parser.markdown import Markdown


# expected: the expected unparsed Markdown
# text: original text without entities
# entities: message entities coming from the server

def test_markdown_unparse_bold():
    expected = "**bold**"
    text = "bold"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.BOLD, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_italic():
    expected = "__italic__"
    text = "italic"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.ITALIC, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_strike():
    expected = "~~strike~~"
    text = "strike"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.STRIKETHROUGH, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_spoiler():
    expected = "||spoiler||"
    text = "spoiler"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.SPOILER, offset=0, length=7)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_url():
    expected = '[URL](https://ftmgram.org/)'
    text = "URL"
    entities = ftmgram.types.List([ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.TEXT_LINK,
                                                                 offset=0, length=3, url='https://ftmgram.org/')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_emoji():
    expected = '![🥲](tg://emoji?id=5195264424893488796) im crying'
    text = "🥲 im crying"
    entities = ftmgram.types.List([ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.CUSTOM_EMOJI,
                                                                 offset=0, length=2, custom_emoji_id=5195264424893488796)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_code():
    expected = '`code`'
    text = "code"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.CODE, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_pre():
    expected = """```python
for i in range(10):
    print(i)
```"""

    text = """for i in range(10):
    print(i)"""

    entities = ftmgram.types.List([ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.PRE, offset=0,
                                                                 length=32, language='python')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_blockquote():
    expected = """> Hello
> from

> pyrogram!"""

    text = """Hello\nfrom\n\npyrogram!"""

    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.BLOCKQUOTE, offset=0, length=10),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.BLOCKQUOTE, offset=12, length=9)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_mixed():
    expected = "**aaaaaaa__aaabbb**__~~dddddddd||ddeee~~||||eeeeeeefff||ffff`fffggggggg`ggghhhhhhhhhh"
    text = "aaaaaaaaaabbbddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.BOLD, offset=0, length=13),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.ITALIC, offset=7, length=6),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.STRIKETHROUGH, offset=13, length=13),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.SPOILER, offset=21, length=5),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.SPOILER, offset=26, length=10),
         ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.CODE, offset=40, length=10)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_no_entities():
    expected = "text"
    text = "text"
    entities = []

    assert Markdown.unparse(text=text, entities=entities) == expected

def test_markdown_unparse_html():
    expected = "__This works, it's ok__ <b>This shouldn't</b>"
    text = "This works, it's ok <b>This shouldn't</b>"
    entities = ftmgram.types.List(
        [ftmgram.types.MessageEntity(type=ftmgram.enums.MessageEntityType.ITALIC, offset=0, length=19)])

    assert Markdown.unparse(text=text, entities=entities) == expected
