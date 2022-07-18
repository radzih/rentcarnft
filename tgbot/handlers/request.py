from datetime import datetime, timedelta
from random import choice
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery, base
from tgbot.config import Config

from tgbot.middlewares.language import ACKMidlleware
from tgbot.services.db import add_paid_out_money, get_amount_of_money_to_be_paid, get_owner_wallet, get_user, update_user_last_request
from tgbot.keyboards.inline import request_money, request_money_callback


async def show_earned_money(message: Message, locale: ACKMidlleware):
    money_to_be_paid = await get_amount_of_money_to_be_paid(message.from_user.id)
    user = await get_user(message.from_user.id)
    if datetime.now() - user.last_request < timedelta(days=7): 
        return await message.answer(locale('You can get money once in 7 days'))
    await message.answer(
        locale(
            'You can get: {money_to_be_paid}$\n'
            'Tap button below to pay get money'
        ).format(money_to_be_paid=money_to_be_paid),
        reply_markup=await request_money(money_to_be_paid, locale)
        )

async def send_get_money_request(
    call: CallbackQuery, locale: ACKMidlleware, callback_data: dict):
    await call.answer()
    config: Config = call.bot.get('config')
    amount_of_requested_money = float(callback_data.get('amount'))
    owner_wallet = await get_owner_wallet(call.from_user.id)
    await call.bot.send_message(
        chat_id=call.bot['config'].misc.support_chat_id,
        text=(
            f'User {call.from_user.id} want '
            f'to get money \n'
            f'Amount: {amount_of_requested_money}$\n'
            'his wallet:\n'
            f'<code>{owner_wallet}</code>'
        )   
    )
    await call.answer(locale('Request sent'))
    await add_paid_out_money(call.from_user.id)
    await update_user_last_request(call.from_user.id)

async def send_request(
    telegram_obj: Message | CallbackQuery, amount: float, requester_iq: int):
    pass
    
async def check_telegram_obj(obj: base.TelegramObject):
    if isinstance(obj, CallbackQuery):
        await obj.answer()
        obj.message.delete()
        return obj.message
    return obj
    
def register_request_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_earned_money,
        commands=['request'],
        is_owner=True
        
    )
    dp.register_callback_query_handler(
        send_get_money_request,
        request_money_callback.filter()
    )