from datetime import datetime, timedelta
from decimal import Decimal
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.storage import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from admin_panel.database.models import CarModel

from tgbot.keyboards.inline import bought_cars_markup, bought_cars_callback, close_markup
from tgbot.misc.scheduler_jobs import add_rent_day_job
from tgbot.misc.states import AddNewrent
from tgbot.services.db import get_bought_cars, get_car_model

async def add_new_rent(message: Message):
    bought_cars = await get_bought_cars()
    if len(bought_cars) == 0:
        return await message.answer('You have no bought cars')
    await message.answer(
        'Select car',
        reply_markup=await bought_cars_markup(bought_cars)
    )
    
async def enter_rent_days(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    car_model_id: int = int(callback_data.get('id'))
    car_model: CarModel = await get_car_model(car_model_id)
    await call.message.edit_text(
        'Enter rent days for {}'.format(car_model.name),
        reply_markup=await close_markup()
    )
    await state.set_state(AddNewrent.get_rent_days)
    await state.update_data(car_model_id=int(callback_data['id']))

async def check_digit_number(message: Message):
    if not message.text.isdigit():
        return await message.answer(
            'Enter only digits',
            reply_markup=await close_markup()
            )
    
async def get_rent_days(message: Message, state: FSMContext):
    await check_digit_number(message)
    rent_days = int(message.text)
    await state.set_state(AddNewrent.get_earnings)
    await state.update_data(rent_days=rent_days)
    car_model_id: int = int((await state.get_data()).get('car_model_id'))
    car_model: CarModel = await get_car_model(car_model_id)
    await message.answer(
        'Enter earnings for {}'.format(car_model.name),
        reply_markup=await close_markup()
    )


async def get_earnings(
    message: Message, state: FSMContext, scheduler: AsyncIOScheduler):
    await check_digit_number(message)    
    earnings = int(message.text)
    rent_days: int = (await state.get_data()).get('rent_days')
    car_model_id = (await state.get_data()).get('car_model_id')
    car_model: CarModel = await get_car_model(car_model_id)
    await state.finish()
    next_day_time = (datetime.now() + timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    scheduler.add_job(
        add_rent_day_job,
        'interval',
        days=1,
        kwargs={
            'earnings': Decimal(earnings/rent_days),    
            'car_model_id': car_model_id,
        },
        misfire_grace_time=None,
        start_date=next_day_time,
        end_date=next_day_time + timedelta(days=rent_days)
    )
    await message.answer(
        'Rent for {} added'.format(car_model.name),
    )
    
    

def register_newrent_handlers(dp: Dispatcher):
    dp.register_message_handler(
        add_new_rent,
        commands=['newrent'],
    )
    dp.register_callback_query_handler(
        enter_rent_days,
        bought_cars_callback.filter()
    )
    dp.register_message_handler(
        get_rent_days,
        state=AddNewrent.get_rent_days
    )
    dp.register_message_handler(
        get_earnings,
        state=AddNewrent.get_earnings
    )
    