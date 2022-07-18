from fcntl import I_CKBAND
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from admin_panel.database.models import CarModel

from tgbot.services.db import Car, get_avaible_nft_cars, get_bought_cars
from tgbot.middlewares.language import ACKMidlleware


navigation_car_callback = CallbackData('navigation', 'index')
async def select_car_keyboard(
    index: int, locale: ACKMidlleware) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    cars: list[Car] = await get_avaible_nft_cars()
    if len(cars) == 1:
        pass
    elif index == 0:
        markup.row(
            InlineKeyboardButton(
                text='⠀', 
                callback_data='first'
                ),
            InlineKeyboardButton(
                text='➡️', 
                callback_data=navigation_car_callback.new(
                    index=index+1,
                    )
                ),            
            )
    elif index == len(cars)-1:
        markup.row(
            InlineKeyboardButton(
                text='⬅️', 
                callback_data=navigation_car_callback.new(
                    index=index-1,
                    )
                ),            
            InlineKeyboardButton(
                text='⠀', 
                callback_data='last'
                ),
        )
    elif index != 0:
        markup.add(
            InlineKeyboardButton(
                text='⬅️', 
                callback_data=navigation_car_callback.new(
                    index=index-1,
                    )
                ),
            InlineKeyboardButton(
                text='➡️', 
                callback_data=navigation_car_callback.new(
                    index=index+1,
                    )
                ),
            )
    markup.add(
        InlineKeyboardButton(
            text=locale('Buy on OpenSea'),
            url=cars[index].url,
        )    
    )
    markup.add(
        InlineKeyboardButton(
            text=locale('❌Close'),
            callback_data='close'
        )
    )
    return markup

bought_cars_callback = CallbackData('bought_car', 'id')
async def bought_cars_markup(bought_cars: list[CarModel]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for car in bought_cars:
        markup.add(
            InlineKeyboardButton(
                text=car.name,
                callback_data=bought_cars_callback.new(
                    id=car.id
                )
            )
        )
    return markup


async def close_markup(locale=None):
    if locale is None:
        locale = lambda x: x
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=locale('❌Close'),
                    callback_data='close'
                )
            ]
        ]
    )

async def back_to_my_nfts(locale: ACKMidlleware) :
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=locale('🔙Back to my NFTs'),
                    callback_data='back_to_my_nfts'
                )
            ],
            [
                InlineKeyboardButton(
                    text=locale('❌Close'),
                    callback_data='close'
                )
            ]
        ]
    )

usernfts_markup_callback = CallbackData('usernfts', 'id')
async def usernfts_markup(user_nfts: list[CarModel]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for car in user_nfts:
        markup.add(
            InlineKeyboardButton(
                text=car.name,
                callback_data=usernfts_markup_callback.new(
                    id=car.id
                )
            )
        )
    return markup

request_money_callback = CallbackData('request_money', 'amount')
async def request_money(
    money_to_be_paid: int, locale: ACKMidlleware) -> InlineKeyboardMarkup:
    if money_to_be_paid == 0: return
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=locale(
                        '💸Request {money_to_be_paid}$'
                        ).format(money_to_be_paid=money_to_be_paid),
                    callback_data=request_money_callback.new(
                        amount=money_to_be_paid)
                )
            ]
        ]
    )
    
choose_language_callback = CallbackData('choose_language', 'lang')
choose_language_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🇺🇸 English',
                callback_data=choose_language_callback.new(lang='en')
            ),
            InlineKeyboardButton(
                text='🇮🇹 Italiano',
                callback_data=choose_language_callback.new(lang='it')
            ),
        ],
        [ 
            InlineKeyboardButton(
                text='🇷🇺 Русский',
                callback_data=choose_language_callback.new(lang='ru')
            )
        ],
        [
            InlineKeyboardButton(
                text='❌Close',
                callback_data='close'
            )
        ]
    ]
)