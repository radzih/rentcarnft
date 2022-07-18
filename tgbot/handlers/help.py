from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.keyboards.inline import close_markup

async def show_help(message: Message, state: FSMContext, locale):
    await message.answer(
        locale('Write your question'),
        reply_markup=await close_markup(locale)
    )
    await state.set_state('help')
    
async def get_message(message: Message, state: FSMContext, locale):
    await message.answer(
        locale('Your message sended to our support')
    )
    await message.bot.send_message(
        chat_id=message.bot['config'].misc.support_chat_id,
        text=f'Question from {message.from_user.id}:\n<code>{message.text}</code>'
    )
    await state.finish()

def register_help_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_help,
        commands=['help'], 
    )
    dp.register_message_handler(
        get_message,
        state='help',
    )