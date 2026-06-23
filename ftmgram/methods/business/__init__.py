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

from .delete_business_messages import DeleteBusinessMessages
from .read_business_message import ReadBusinessMessage
from .get_business_account_gifts import GetBusinessAccountGifts
from .get_business_connection import GetBusinessConnection
from .get_collectible_item_info import GetCollectibleItemInfo
from .get_owned_star_count import GetOwnedStarCount
from .get_received_gifts import GetReceivedGifts
from .sell_gift import SellGift
from .toggle_gift_is_saved import ToggleGiftIsSaved
from .transfer_business_account_stars import TransferBusinessAccountStars


class Business(
    DeleteBusinessMessages,
    GetBusinessAccountGifts,
    GetBusinessConnection,
    GetCollectibleItemInfo,
    GetOwnedStarCount,
    GetReceivedGifts,
    SellGift,
    ToggleGiftIsSaved,
    ReadBusinessMessage,
    TransferBusinessAccountStars,
):
    pass
