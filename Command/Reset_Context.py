from aiogram import types
from aiogram.dispatcher.filters import Text

from SetupBot.Setup import bot
from SetupBot.Setup import dp

from Configs.Template_Responses import MESSAGE_RESET_CONTEXT

from DataBase import DB

from Command.Command_Name import RESET_COMMAND


@dp.callback_query_handler(Text(RESET_COMMAND))
async def cmd_enable_context(callback_query: types.CallbackQuery):
    await DB.del_all_message(callback_query.from_user.id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGE_RESET_CONTEXT)
