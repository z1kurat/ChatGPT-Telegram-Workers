import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from Configs.Logging_Parametrs import LOGGING_PATH

file_handler = logging.FileHandler(LOGGING_PATH)
stream_handler = logging.StreamHandler()

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
