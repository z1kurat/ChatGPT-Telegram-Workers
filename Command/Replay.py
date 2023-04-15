from aiogram import types
from aiogram.dispatcher.filters import Text, Command

import Keyboards

from Command import GPT
from Command.GPT import save_data

from Configs.GPT_Setting import DEFAULT_MOD

from Configs.Template_Responses import START_RESPONSE, ERROR_RESPONSE_MESSAGE

from SetupBot.Setup import logger_history
from SetupBot.Setup import dp

from DataBase import DB

from Command.Command_Name import REPLAY_COMMAND


@dp.callback_query_handler(Text(REPLAY_COMMAND))
async def cmd_replay_context(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    last_message = await DB.read_last_message(user_id)
    message = callback_query.message

    await message.delete()

    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    user_messages = await GPT.get_user_messages(user_id)

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": last_message})

    response = await GPT.get_response_gpt(user_messages)

    await start_response_message.delete()

    if response is None:
        await message.answer(ERROR_RESPONSE_MESSAGE, reply_markup=Keyboards.reset_and_replay_keyboard)
        return

    await message.answer(response, reply_markup=Keyboards.reset_context_keyboard)

    await save_data(user_id, last_message, response)

    logger_history.info(message.chat.first_name + " - Good!")


@dp.message_handler(Command(REPLAY_COMMAND))
async def cmd_replay_context(message: types.Message):
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)
    message = message.text

    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    user_messages = await GPT.get_user_messages(user_id)

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": last_message})

    response = await GPT.get_response_gpt(user_messages)

    await start_response_message.delete()

    if response is None:
        await message.answer(ERROR_RESPONSE_MESSAGE, reply_markup=Keyboards.reset_and_replay_keyboard)
        return

    await message.answer(response, reply_markup=Keyboards.reset_context_keyboard)

    await save_data(user_id, last_message, response)

    logger_history.info(message.chat.first_name + " - Good!")
