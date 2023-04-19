from aiogram import types

from Bot_Command.utilitesGPT import run

from SetupBot.Setup import bot

import Keyboards

from Configs.templateResponses import NONE_LAST_MESSAGE

from DataBase import DB


async def replay(message: types.Message, is_callback=False, callback_id=-1):
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)

    if last_message is None:
        await message.answer(NONE_LAST_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    if is_callback:
        await bot.answer_callback_query(callback_id)
        await message.delete()

    await run.gpt(message, last_message)

    await DB.set_work_state(user_id, False)


async def replay_callback(callback_query: types.CallbackQuery):
    message = callback_query.message
    callback_id = callback_query.id
    print("asd")
    await replay(message, True, callback_id)


async def replay_cmd(message: types.Message):
    await replay(message)
