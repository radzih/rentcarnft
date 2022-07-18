import logging
from uuid import UUID
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from admin_panel.database.models import NFTCar
from tgbot.config import Config

from tgbot.filters.addnft import AddNFTFilter
from tgbot.middlewares.language import ACKMidlleware
from tgbot.misc.scheduler_jobs import check_owner, get_owner_nft
from tgbot.services.db import add_user_to_db, get_nft, get_user, db_add_nft_to_user




async def start(message: Message, locale: ACKMidlleware):
    user = await get_user(message.from_user.id)
    if not user:
        user = await add_user_to_db(message.from_user.id)
    await message.answer(locale('Hi, you can see comands in /menu'))
    
    
    
async def add_nft_to_user(
    message: Message, locale: ACKMidlleware,
    scheduler: AsyncIOScheduler):
    config: Config = message.bot.get('config')
    user = await get_user(message.from_user.id)
    if not user: user = await add_user_to_db(message.from_user.id)
    nft_secret_code: UUID = UUID(message.get_args())
    car: NFTCar = await get_nft(nft_secret_code)
    owner_addr = await get_owner_nft(car.address, car.token_id, config)
    logging.info(owner_addr)
    await db_add_nft_to_user(user, car, owner_addr)
    await message.answer(locale('You added new NFT you can see it in /my'))
    scheduler.add_job(
        check_owner,
        'interval',
        minutes=30,
        kwargs={'car': car, 'config': config}
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart(deep_link='')
    )
    dp.register_message_handler(
        add_nft_to_user,
        CommandStart(),
        add_nft=True,
    )