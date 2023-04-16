from aiogram import types
from aiogram.dispatcher.filters import Text, Command

import Keyboards

from Command import GPT

from Configs.Template_Responses import AWAIT_RESPONSE_MESSAGE

from SetupBot.Setup import dp
from SetupBot.Setup import bot

from DataBase import DB

from Command.Command_Name import REPLAY_COMMAND


@dp.message_handler(Command(REPLAY_COMMAND))
async def cmd_replay_command(message: types.Message):
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await GPT.run_gpt(message, last_message, user_id)

    await DB.set_working(user_id, False)


@dp.callback_query_handler(Text(REPLAY_COMMAND))
async def cmd_replay_query(callback_query: types.CallbackQuery):
    message = callback_query.message
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await message.delete()

    await GPT.run_gpt(message, last_message, user_id)

    await bot.answer_callback_query(callback_query.id)

    await DB.set_working(user_id, False)
