import asyncio

import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from DataBase import DB

loop = asyncio.get_event_loop()
db = await DB.set_sql_connect(loop)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

