from typing import Awaitable
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.middlewares.language import ACKMidlleware
from tgbot.keyboards.inline import choose_language_markup, choose_language_callback
from tgbot.services.db import change_user_language 

async def select_language(message: Message, locale: ACKMidlleware):
    await message.answer(
        locale('Select your language'),
        reply_markup=choose_language_markup 
        )

async def change_language(call: CallbackQuery, locale: ACKMidlleware,
                          callback_data: dict):
    await call.answer()
    choosen_lang = callback_data['lang']
    await change_user_language(call.from_user.id, choosen_lang)
    await call.message.edit_text(
        locale('Language changed to {}'.format(choosen_lang)),
    )

def register_lang_handlers(dp: Dispatcher):
    dp.register_message_handler(
        select_language,
        commands=['lang'])
    dp.register_callback_query_handler(
        change_language,
        choose_language_callback.filter()
    )