import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator
from apscheduler.jobstores.redis import RedisJobStore
from aiogram.contrib.middlewares.environment import EnvironmentMiddleware
from tgbot.misc.setup_django import setup_django
setup_django()
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.addnft import AddNFTFilter
from tgbot.filters.is_owner import OwnerFilter
from tgbot.handlers.my import register_my_handlers
from tgbot.handlers.lang import register_lang_handlers
from tgbot.handlers.cars import register_cars_handlers
from tgbot.handlers.help import register_help_handlers
from tgbot.handlers.menu import register_menu_handlers
from tgbot.handlers.start import register_start_handlers
from tgbot.middlewares.scheduler import SchedulerMiddleware
from tgbot.handlers.request import register_request_handlers
from tgbot.handlers.newrent import register_newrent_handlers
from tgbot.middlewares.language import ACKMidlleware, LanguageMidlleware

logger = logging.getLogger(__name__)


def register_all_middlewares(
    dp: Dispatcher, i18n: ACKMidlleware, scheduler: AsyncIOScheduler):
    # dp.setup_middleware(LanguageMidlleware(i18n))
    dp.middleware.setup(
        EnvironmentMiddleware(
            context={'locale': i18n.gettext}
        )
    )
    dp.middleware.setup(i18n)
    dp.setup_middleware(SchedulerMiddleware(scheduler))
    

def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AddNFTFilter)
    dp.filters_factory.bind(OwnerFilter)


def register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_cars_handlers(dp)
    register_menu_handlers(dp)
    register_my_handlers(dp)
    register_newrent_handlers(dp)
    register_lang_handlers(dp)
    register_request_handlers(dp)
    register_help_handlers(dp)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    job_stores = {
        "default": RedisJobStore(
            host=config.redis.host,
            jobs_key="dispatched_trips_jobs",
            run_times_key="dispatched_trips_running"
        )
    }
    
    storage = RedisStorage2(
        host=config.redis.host
        ) if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)
    i18n = ACKMidlleware(config.misc.locale_domain, config.misc.locale_dir)
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(jobstores=job_stores))
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    logging.info(config.misc.locale_dir)
    bot['config'] = config

    register_all_middlewares(dp, i18n, scheduler)
    register_all_filters(dp)
    register_all_handlers(dp)

    

    # start
    try:
        scheduler.start()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
