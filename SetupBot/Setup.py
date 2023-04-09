import logging

from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN

from Configs.Logging_Parametrs import LOGGING_PATH
from Configs.Logging_Parametrs import LOGGING_NAME

logging.basicConfig(filename=LOGGING_PATH,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(LOGGING_NAME, encoding='utf-8'),
                        logging.StreamHandler()
                        ]
                    )

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
