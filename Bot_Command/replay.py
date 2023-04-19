from aiogram import types

from Bot_Command.utilitesGPT import run

from SetupBot.Setup import bot

import Keyboards

from Configs.templateResponses import NONE_LAST_MESSAGE

from DataBase import DB


async def replay(message: types.Message, is_callback=False, callback_id=-1):
    user_id = message.chat.id
    last_message = await DB.read_last_message(user_id)

    if is_callback:
        await bot.answer_callback_query(callback_id)
        await message.delete()

    if last_message is None:
        await bot.send_message(user_id, NONE_LAST_MESSAGE, disable_notification=True,
                               reply_markup=Keyboards.remove_keyboard)
        return

    await run.gpt(message, last_message)

    await DB.set_work_state(user_id, False)


async def replay_callback(callback_query: types.CallbackQuery):
    await replay(callback_query.message, True, callback_query.id)


async def replay_cmd(message: types.Message):
    await replay(message, False)
