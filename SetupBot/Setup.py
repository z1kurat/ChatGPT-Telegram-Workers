import logging.handlers

import openai

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN
from Configs.API import OPENAI_KEY

logger_history = logging.getLogger("bot_history")
logger_history.setLevel(logging.INFO)

logger_error = logging.getLogger("bot_error")
logger_error.setLevel(logging.ERROR)

FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'

file_handler_history = logging.handlers.RotatingFileHandler(filename='bot_history')
file_handler_history.setFormatter(logging.Formatter(FORMAT))
file_handler_history.setLevel(logging.INFO)

file_handler_error = logging.handlers.RotatingFileHandler(filename='bot_error')
file_handler_error.setFormatter(logging.Formatter(FORMAT))
file_handler_error.setLevel(logging.ERROR)

logger_history.addHandler(file_handler_history)
logger_error.addHandler(file_handler_error)

logger_error.error("Start debug...")
logger_history.info("Start info...")

openai.api_key = OPENAI_KEY

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
