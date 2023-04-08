import asyncio

import aiomysql

import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB


loop = asyncio.get_event_loop()

db = loop.run_until_complete(aiomysql.connect(host=HOST,
                                              port=PORT,
                                              user=USER,
                                              password=PASSWORD,
                                              db=NAME_DB))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

