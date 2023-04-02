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

DB_URL = "./DB/bot.db"

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# print("-----Gotcha-----")
#     message = message.text
#
#     chat_id = message.chat.id
#
#     print(f"User: {message.chat.first_name}")
#     print(f"message: {message.text}")
#     print(f"id: {chat_id}")
#
#     user_history.setdefault(chat_id, [])
#
#     messages = user_history[chat_id]
#     messages.append(
#         {"role": "system", "content": "You are a kind and helpful assistant who gives detailed and useful answers"})
#     messages.append({"role": "user", "content": message.text})
#
#     user_history[chat_id].append({"role": "user", "content": message.text})
#
#     if len(user_history[chat_id]) >= 22:
#         user_history[chat_id].pop(0)
#         user_history[chat_id].pop(0)
#
#     try:
#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#             temperature=0.7,
#             n=1
#         )
#
#         bot.reply_to(chat_id, completion.choices[0].message.content)
#         print(f"send: {completion.choices[0].message.content}")
#
#         user_history[chat_id].append({"role": "assistant", "content": completion.choices[0].message.content})
#
#     except:
#         bot.reply_to(chat_id, "Ты дурка? Я думаю, что да!")
#
#     print("----------------\n")