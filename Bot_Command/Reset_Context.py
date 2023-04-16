from aiogram import types

from SetupBot.Setup import bot

from Configs.Template_Responses import MESSAGE_RESET_CONTEXT

from DataBase import DB


async def cmd_enable_context(callback_query: types.CallbackQuery):
    await DB.del_all_message(callback_query.from_user.id)
    await DB.set_working(callback_query.from_user.id, False)
    await bot.send_message(callback_query.from_user.id, MESSAGE_RESET_CONTEXT)
    await bot.answer_callback_query(callback_query.id)


async def cmd_enable_context_command(message: types.Message):
    await DB.del_all_message(message.from_user.id)
    await DB.set_working(message.from_user.id, False)
    await bot.send_message(message.from_user.id, MESSAGE_RESET_CONTEXT)
