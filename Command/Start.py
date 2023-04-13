from aiogram import types
from aiogram.dispatcher.filters import Command

from SetupBot.Setup import dp

from Filters.Chat_Subscriber import IsSubscriber

from Configs.Template_Responses import START_MESSAGE

from DataBase import DB


@dp.message_handler(Command("start"), IsSubscriber())
async def cmd_start(message: types.Message):
    await DB.add_new_user(message.from_user.id)
    await DB.create_if_not_exists_message_history(message.from_user.id)
    await message.answer(START_MESSAGE)
