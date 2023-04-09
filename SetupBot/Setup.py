import logging

import tg_logger

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from Configs.Logging_Parametrs import LOGGING_ID

logger = logging.getLogger()

my_tg_logger = tg_logger.setup(
    logger,
    token=TELEGRAM_BOT_TOKEN,
    users=LOGGING_ID
)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
