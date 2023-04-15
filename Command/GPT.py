from aiogram import types

import openai

from Filters.Chat_Subscriber import IsSubscriber

from DataBase import DB

from Configs.API import OPENAI_KEY

from Configs.Template_Responses import ERROR_RESPONSE_MESSAGE

from Configs.GPT_Setting import DEFAULT_MOD
from Configs.GPT_Setting import MODEL
from Configs.GPT_Setting import TEMPERATURE
from Configs.GPT_Setting import MAX_VALUE_COUNT
from Configs.GPT_Setting import TIME_OUT
from Configs.GPT_Setting import STOP

from Configs.Template_Responses import START_RESPONSE

from SetupBot.Setup import dp
from SetupBot.Setup import logger_error
from SetupBot.Setup import logger_history

import Keyboards


async def get_user_messages(user_id) -> list[dict[str, str]]:
    user_messages = await DB.read_message_history(user_id)

    if user_messages is None or len(user_messages) == 0:
        user_messages = []

    return user_messages


async def get_response_gpt(user_messages):
    try:
        completion = await openai.ChatCompletion.create(
            OPENAI_KEY,
            timeout=TIME_OUT,
            payload={
                "model": MODEL,
                "messages": user_messages,
                "temperature": TEMPERATURE,
                "stop": STOP,
                "n": MAX_VALUE_COUNT
            }
        )

        return completion.json()["choices"][0]["message"]["content"]

    except Exception as err:
        logger_error.error(err.args)
        return None


async def save_data(user_id, message_text, response):
    if message_text is not None:
        await DB.save_message_history(user_id, "user", message_text)

    if response is not None:
        await DB.save_message_history(user_id, "assistant", response)


@dp.message_handler(IsSubscriber())
async def cmd_gpt(message: types.Message):
    message_text = message.text
    user_id = message.from_user.id

    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    user_messages = await get_user_messages(user_id)

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": message_text})

    response = await get_response_gpt(user_messages)

    await start_response_message.delete()

    if response:
        await message.answer(ERROR_RESPONSE_MESSAGE, reply_markup=Keyboards.reset_and_replay_keyboard)
        return

    await message.answer(response, reply_markup=Keyboards.reset_context_keyboard)

    await save_data(user_id, message_text, response)

    await DB.update_last_message(user_id, message_text)

    logger_history.info(message.chat.first_name + " - Good!")

