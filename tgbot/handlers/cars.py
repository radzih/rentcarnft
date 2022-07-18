from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import Dispatcher
from aiogram.types.input_file import InputFile
from aiogram.types.input_media import InputMedia


from tgbot.services.db import get_avaible_nft_cars, Car
from tgbot.middlewares.language import ACKMidlleware
from tgbot.keyboards.inline import select_car_keyboard, navigation_car_callback


async def show_avaible_cars(
    message: Message, locale: ACKMidlleware):
    '''Function that show avaible cars in cards'''
    cars: list[Car] = await get_avaible_nft_cars()
    if len(cars) == 0:
        return await message.answer(locale('No avaible cars'))
    car = cars[0]
    await message.answer_photo(
        photo=InputFile(car.picture_path),
        caption=locale(
            '<b>{car_name}</b>\n'
            'Procent: {car_part}%\n'
            # 'Price: {car_price}$\n'
        ).format(
            car_name=car.name,
            car_part=car.part,
        ),
        reply_markup=await select_car_keyboard(0, locale)
    )
    
    
async def avaible_cars_call(
    call: CallbackQuery, locale: ACKMidlleware, callback_data: dict):
    await call.answer()
    index = int(callback_data.get('index', 0))
    car: Car = (await get_avaible_nft_cars())[index]
    media = InputMedia(
        media=InputFile(car.picture_path),
        caption=locale(
            '<b>{car_name}</b>\n'
            'Procent: {car_part}%\n'
            ).format(
                car_name=car.name,
                car_part=car.part,
            ),
        )
    await call.message.edit_media(
        media=media,
        reply_markup=await select_car_keyboard(index, locale),    
    )
    
async def say_that_its_first_item(call: CallbackQuery):
    await call.answer('It\'s first item')

async def say_that_its_last_item(call: CallbackQuery):
    await call.answer('It\'s last item')

async def close_item(call: CallbackQuery):
    await call.answer('Closed')
    await call.message.delete()
    
def register_cars_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_avaible_cars,
        commands=['cars']
    )
    dp.register_callback_query_handler(
        avaible_cars_call,
        navigation_car_callback.filter()
    )
    dp.register_callback_query_handler(
        close_item, 
        text='close',
        state='*')
    dp.register_callback_query_handler(
        say_that_its_first_item,
        text='first'
    )
    dp.register_callback_query_handler(
        say_that_its_last_item,
        text='last'
    )