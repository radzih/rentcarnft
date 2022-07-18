import logging
from typing import Any, Type
from aiogram import types
from aiogram.types.base import TelegramObject
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from tgbot.services.db import Language, get_user_language


class ACKMidlleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: tuple) -> Type[Language]:
        user = types.User.get_current()
        lsn = await get_user_language(user.id)
        logging.info(lsn)
        return lsn
    
class LanguageMidlleware(LifetimeControllerMiddleware):
    def __init__(self, i18n: ACKMidlleware):
        self._i18n = i18n
        super().__init__()
        
    async def pre_process(
        self, obj: TelegramObject, data: dict[str: Any], *args: Any):
        data['locale'] = self._i18n.gettext
