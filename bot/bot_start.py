import asyncio

import logging

from aiogram import Bot

from bot.structures.dispatcher import get_dispatcher, get_redis_storage
from bot.structures.data_structure import TransferData
from bot.cache import Cache
from bot.structures import conf, set_bot_commands
from bot.data_base.data_base import create_session_maker


logger = logging.getLogger(__name__)


async def start_bot():
    logging.basicConfig(
        level=logging.DEBUG,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
        #filename='../bot_history'
    )
    logger.info("Starting bot")

    bot = Bot(token=conf.bot.token)
    cache: Cache = Cache()
    storage = get_redis_storage(redis=cache.fsm_client.redis_client)

    dp = get_dispatcher(storage=storage)

    transfer_data: TransferData = TransferData(pool=create_session_maker(), cache=cache)

    await set_bot_commands(bot)

    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            **transfer_data
        )
    finally:
        await bot.session.close()
        await cache.close()

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
