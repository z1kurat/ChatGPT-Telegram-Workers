import openai_async

from aiogram import types

from Filters.Chat_Subscriber import IsSubscriber

from DataBase import DB

from Configs.API import OPENAI_KEY

from Configs.Template_Responses import ERROR_RESPONSE_MESSAGE
from Configs.Template_Responses import AWAIT_RESPONSE_MESSAGE

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


@dp.message_handler(IsSubscriber(), content_types=['text'])
async def cmd_gpt(message: types.Message):
    await gpt_command(message, message.text)


async def get_user_messages(user_id) -> list[dict[str, str]]:
    user_messages = await DB.read_message_history(user_id)

    if user_messages is None or len(user_messages) == 0:
        user_messages = []

    return user_messages


async def get_response_gpt(user_messages):
    try:
        completion = await openai_async.chat_complete(
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
    await DB.save_message_history(user_id, "user", message_text)
    await DB.save_message_history(user_id, "assistant", response)


async def prepare_for_work(user_id) -> bool:
    is_working = await DB.get_working(user_id)

    if is_working:
        return False

    await DB.set_working(user_id, True)

    return True


async def gpt_command(message: types.Message, message_text, update_last_message=True):
    user_id = message.from_user.id
    ready_to_work = await prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await run_gpt(message, message_text, user_id)

    if update_last_message:
        await DB.update_last_message(user_id, message_text)

    await DB.set_working(user_id, False)


async def run_gpt(message: types.Message, message_text, user_id):
    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    current_message = [{"role": "system", "content": DEFAULT_MOD}]

    user_messages = await get_user_messages(user_id)

    if user_messages is not None and len(user_messages) != 0:
        current_message.extend(user_messages)

    current_message.append({"role": "user", "content": message_text})
    response = await get_response_gpt(current_message)

    await start_response_message.delete()
    keyboard = Keyboards.reset_context_keyboard

    if response is not None:
        await save_data(user_id, message_text, response)

    if response is None:
        response = ERROR_RESPONSE_MESSAGE
        keyboard = Keyboards.reset_and_replay_keyboard

    await message.answer(response, reply_markup=keyboard)

    logger_history.info(message.chat.first_name + " - Good!")
