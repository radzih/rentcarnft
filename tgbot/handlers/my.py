import logging
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import Dispatcher
from aiogram.types.input_file import InputFile
from aiogram.types.input_media import InputMedia
from admin_panel.database.models import NFTCar

from tgbot.middlewares.language import ACKMidlleware
from tgbot.services.db import Car, get_car, get_user_nfts
from tgbot.keyboards.inline import back_to_my_nfts, usernfts_markup, usernfts_markup_callback

async def show_users_nfts(message: Message | CallbackQuery, locale: ACKMidlleware):
    user_nfts: list[NFTCar] = await get_user_nfts(message.from_user.id)
    amount_rent_days = sum(nft.rent_days for nft in user_nfts)
    total_earnings = sum(nft.earned_money for nft in user_nfts)
    await message.answer_photo(
        photo=InputFile('./images/my.png'),
        caption=locale(
            'Statistics on all NFTs:\n'
            '   You have {amount_user_nfts} NFTs\n'
            '   Rented days: {amount_rent_days}\n'
            '   Total earnings: {total_earnings}$\n'
            'You can see statistics about each NFT separately ⬇'
        ).format(
            amount_user_nfts=len(user_nfts),
            amount_rent_days=amount_rent_days,
            total_earnings=total_earnings
            ),
        reply_markup=await usernfts_markup(user_nfts)
    )

async def show_users_nfts_callback(call: CallbackQuery, locale: ACKMidlleware):
    await call.answer()
    user_nfts: list[NFTCar] = await get_user_nfts(call.from_user.id)
    amount_rent_days = sum(nft.rent_days for nft in user_nfts)
    total_earnings = sum(nft.earned_money for nft in user_nfts)
    
    media = InputMedia(
        media=InputFile('./images/my.png'),
        caption=locale(
            'Statistics on all NFTs:\n'
            '   You have {amount_user_nfts} NFTs\n'
            '   Rented days: {amount_rent_days}\n'
            '   Total earnings: {total_earnings}$\n'
            'You can see statistics about each NFT separately ⬇'
        ).format(
            amount_user_nfts=len(user_nfts),
            amount_rent_days=amount_rent_days,
            total_earnings=total_earnings
            ),
        )
    await call.message.edit_media(
        media=media,
        reply_markup=await usernfts_markup(user_nfts)
    )
    
async def show_statistics_about_nft(
    call: CallbackQuery, callback_data: dict, locale: ACKMidlleware):
    await call.answer()
    nftcar_id: int = int(callback_data.get('id'))
    car: Car = await get_car(nftcar_id)
    media = InputMedia(
        media=InputFile(car.picture_path),
        caption=locale(
            '<b>{car_name}</b>\n'
            'Procent: {car_part}%\n'
            'Rented days: {rented_days}\n'
            'Earned money: {earned_money}$\n'
            ).format(
                car_name=car.name,
                car_part=car.part,
                rented_days=car.rent_days,
                earned_money=car.earned_money
            ),
        )
    await call.message.edit_media(
        media=media,
        reply_markup=await back_to_my_nfts(locale)
    )

def register_my_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_users_nfts,
        commands=['my'],
        is_owner=True
    )
    dp.register_callback_query_handler(
        show_statistics_about_nft,
        usernfts_markup_callback.filter()
    )
    dp.register_callback_query_handler(
        show_users_nfts_callback,
        text='back_to_my_nfts'
    )