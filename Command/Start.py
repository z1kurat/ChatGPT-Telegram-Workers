from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram import Dispatcher


async def cmd_start(message: types.Message):
    await message.answer("Hello!")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
