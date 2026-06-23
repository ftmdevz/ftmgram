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
from ftmgram import raw, types


class GetStarTransactions:
    async def get_star_transactions(
        self: "ftmgram.Client",
        offset: str = "",
        limit: int = 100,
        inbound: Optional[bool] = None,
        outbound: Optional[bool] = None,
        ascending: Optional[bool] = None,
    ) -> List["types.StarTransaction"]:
        """Returns the bot's Telegram Star transactions in chronological order.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            offset (``str``, *optional*):
                Offset of the first transaction to be returned as received from the previous request;
                use empty string for the first request.

            limit (``int``, *optional*):
                The maximum number of transactions to be retrieved. Values between 1-100 are accepted.
                Defaults to 100.

            inbound (``bool``, *optional*):
                Pass True to get only incoming transactions.

            outbound (``bool``, *optional*):
                Pass True to get only outgoing transactions.

            ascending (``bool``, *optional*):
                Pass True to get transactions in ascending chronological order.

        Returns:
            List of :obj:`~ftmgram.types.StarTransaction`: On success, a list of transactions is returned.

        Example:
            .. code-block:: python

                transactions = await app.get_star_transactions()
                for t in transactions:
                    print(t.id, t.nanostar_amount)
        """
        peer = await self.resolve_peer("me")

        r = await self.invoke(
            raw.functions.payments.GetStarsTransactions(
                peer=peer,
                offset=offset,
                limit=limit,
                inbound=inbound,
                outbound=outbound,
                ascending=ascending,
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return types.List([
            types.StarTransaction._parse(self, t, users, chats)
            for t in r.history
        ]) if hasattr(r, 'history') else types.List()
