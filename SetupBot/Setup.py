from aiogram import Bot, Dispatcher

from Configs.API import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
