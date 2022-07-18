import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from tgbot.services.db import get_user_nfts


class OwnerFilter(BoundFilter):
    key = 'is_owner'

    def __init__(self, is_owner: typing.Optional[bool]):
        self._is_owner = is_owner

    async def check(self, obj: Message | CallbackQuery) -> bool:
        if self._is_owner is None:
            return False
        user_nfts = await get_user_nfts(obj.from_user.id)
        return bool(user_nfts)

