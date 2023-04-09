import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
