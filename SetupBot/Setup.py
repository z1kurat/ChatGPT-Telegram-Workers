import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from Configs.Logging_Parametrs import LOGGING_PATH

logging.basicConfig(filename=LOGGING_PATH, level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
