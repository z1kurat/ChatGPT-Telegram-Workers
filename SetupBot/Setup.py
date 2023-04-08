import logging

from DataBase import DB

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN


logging.basicConfig(level=logging.INFO)

db_conn = DB.set_sql_connect()

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

