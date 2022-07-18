import logging
import typing
from uuid import UUID

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from tgbot.config import Config
from tgbot.services.db import get_secret_codes


class AddNFTFilter(BoundFilter):
    key = 'add_nft'

    def __init__(self, add_nft: typing.Optional[bool] = None):
        self.add_nft = add_nft

    async def check(self, obj: Message | CallbackQuery) -> bool:
        if self.add_nft is None or obj.get_args() is None:
            return False
        try:
            secret_code: UUID = UUID(obj.get_args())
        except ValueError:
            return False
        avaible_secret_codes = await get_secret_codes()
        return secret_code in avaible_secret_codes

