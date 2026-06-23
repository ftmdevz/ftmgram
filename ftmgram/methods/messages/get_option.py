#  Ftmgram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present <https://github.com/TelegramPlayGround>
#
#  This file is part of Ftmgram.
#
#  Ftmgram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Ftmgram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Ftmgram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from typing import Union, Optional

import ftmgram
from ftmgram import raw


class GetOption:
    async def get_option(
        self: "ftmgram.Client",
        name: str,
    ) -> Optional[Union[bool, int, str, list, dict]]:
        """Returns the value of a Telegram server option by its name.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            name (``str``):
                The name of the option (e.g. ``"chat_read_mark_expire_period"``).

        Returns:
            ``bool`` | ``int`` | ``str`` | ``list`` | ``dict``: The value of the option, or None if not found.

        Example:
            .. code-block:: python

                value = await app.get_option("chat_read_mark_expire_period")
                print(value)
        """
        app_config = await self.invoke(
            raw.functions.help.GetAppConfig(hash=0)
        )
        option = next(
            (x for x in app_config.config.value if x.key == name),
            None
        )
        if not option:
            return None
        return self._parse_tggob_json(option.value)
