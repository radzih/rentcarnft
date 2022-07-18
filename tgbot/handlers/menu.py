from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher

from tgbot.middlewares.language import ACKMidlleware

async def show_menu(message: Message, locale: ACKMidlleware):
    await message.answer(
        locale(
            'Menu:\n'
            '1. /start - start bot\n'
            '2. /menu - show this menu\n'
            '3. /cars - show avaible NFTs\n'
            '4. /my - show your NFTs\n'
            '5. /lang - change language\n'
            '6. /request - request money\n'
            '6. /help - support'
        )
    )


def register_menu_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_menu,
        commands=['menu']
    )