from aiogram import types

from Configs.templateResponses import START_MESSAGE

from DataBase import DB


async def cmd_start(message: types.Message):
    await DB.add_new_user(message.from_user.id)
    await DB.create_if_not_exists_message_history(message.from_user.id)
    await message.answer(START_MESSAGE)