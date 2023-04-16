from aiogram import types

from SetupBot.Setup import bot

import Keyboards

from Bot_Command import GPT

from Configs.Template_Responses import AWAIT_RESPONSE_MESSAGE, NONE_LAST_MESSAGE

from DataBase import DB


async def cmd_replay_query(callback_query: types.CallbackQuery):
    message = callback_query.message
    user_id = callback_query.message.from_user.id

    last_message = await DB.read_last_message(user_id)

    if last_message is None:
        await message.answer(NONE_LAST_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await message.delete()

    await GPT.run_gpt(message, last_message, user_id)

    await bot.answer_callback_query(callback_query.id)

    await DB.set_working(user_id, False)


async def cmd_replay_command(message: types.Message):
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)

    if last_message is None:
        await message.answer(NONE_LAST_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await GPT.run_gpt(message, last_message, user_id)

    await DB.set_working(user_id, False)
