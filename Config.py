from aiogram.dispatcher import Dispatcher
from aiogram import Bot

# api key
OPENAI_KEY = "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"
TELEGRAM_BOT_TOKEN = "5853486557:AAHnqhu_7CqePUhU29S27AhrrHVZqiC0MBI"

# webserver settings
WEBHOOK_HOST = '85.193.83.52'
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443
WEBHOOK_LISTEN = '0.0.0.0'

# webhook settings
WEBHOOK_SSL_CERT = './cert/webhook_cert.pem'
WEBHOOK_SSL_PRIV = './cert/webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % TELEGRAM_BOT_TOKEN

DB_URL = "postgresql+asyncpg://bot@localhost/bot"
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

