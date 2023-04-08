from aiogram import types
from aiogram import Dispatcher

from Configs.Template_Responses import START_MESSAGE

from DataBase import DB

from SetupBot.Setup import db


async def cmd_start(message: types.Message):
    await DB.create_if_not_exists_message_history(message.from_user.id, db)
    await message.answer(START_MESSAGE)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
