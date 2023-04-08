import asyncio

import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from DataBase import DB

db = asyncio.get_event_loop().run_until_complete(DB.set_sql_connect())

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

