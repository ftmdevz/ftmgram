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

from ..object import Object


class InputPrivacyRule(Object):
    """Content of a privacy rule.

    It should be one of:

    - :obj:`~ftmgram.types.InputPrivacyRuleAllowAll`
    - :obj:`~ftmgram.types.InputPrivacyRuleAllowContacts`
    - :obj:`~ftmgram.types.InputPrivacyRuleAllowPremium`
    - :obj:`~ftmgram.types.InputPrivacyRuleAllowUsers`
    - :obj:`~ftmgram.types.InputPrivacyRuleAllowChats`
    - :obj:`~ftmgram.types.InputPrivacyRuleDisallowAll`
    - :obj:`~ftmgram.types.InputPrivacyRuleDisallowContacts`
    - :obj:`~ftmgram.types.InputPrivacyRuleDisallowUsers`
    - :obj:`~ftmgram.types.InputPrivacyRuleDisallowChats`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "ftmgram.Client"):
        raise NotImplementedError
