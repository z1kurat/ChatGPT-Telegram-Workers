import logging

from db import database

from Config import WEBHOOK_HOST
from Config import WEBHOOK_SSL_CERT
from Config import WEBHOOK_PORT
from Config import WEBHOOK_LISTEN
from Config import WEBHOOK_SSL_PRIV
from Config import WEBHOOK_URL_BASE
from Config import WEBHOOK_URL_PATH
from Config import dp
from Config import bot

from aiogram import types
from aiogram.utils.executor import start_webhook


async def on_startup(dispatcher):
    #database.connection()
    await bot.set_webhook(WEBHOOK_HOST, certificate=WEBHOOK_SSL_CERT, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    #database.disconnect()
    await bot.delete_webhook()


async def save(user_id, text):
    pass
    #await database.execute(f"INSERT INTO messages(telegram_id, text) "
    #                       f"VALUES (:telegram_id, :text)", values={'telegram_id': user_id, 'text': text})


async def read(user_id):
    return ""
    # results = await database.fetch_all('SELECT text '
    #                                    'FROM messages '
    #                                    'WHERE telegram_id = :telegram_id ',
    #                                    values={'telegram_id': user_id})
    # return [next(result.values()) for result in results]


@dp.message_handler()
async def echo(message: types.Message):
    #await save(message.from_user.id, message.text)
    #messages = await read(message.from_user.id)
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBHOOK_HOST,
        port=WEBHOOK_PORT,
    )

# bot.set_webhook(url=Config.WEBHOOK_URL_BASE + Config.WEBHOOK_URL_PATH,
#                certificate=open(Config.WEBHOOK_SSL_CERT, 'r'))

# cherrypy.config.update({
#    'server.socket_host': Config.WEBHOOK_LISTEN,
#    'server.socket_port': Config.WEBHOOK_PORT,
#    'server.ssl_module': 'builtin',
#    'server.ssl_certificate': Config.WEBHOOK_SSL_CERT,
#    'server.ssl_private_key': Config.WEBHOOK_SSL_PRIV
# })

# cherrypy.quickstart(WebhookServer(), Config.WEBHOOK_URL_PATH, {'/': {}})
