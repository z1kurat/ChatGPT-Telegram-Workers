from aiogram import types
from aiogram import Dispatcher

import openai_async

from Configs.API import OPENAI_KEY
from Configs.Template_Responses import ERROR_RESPONSE_MESSAGE
from Configs.GPT_Setting import DEFAULT_MOD
from Configs.GPT_Setting import MODEL
from Configs.GPT_Setting import TEMPERATURE
from Configs.GPT_Setting import MAX_VALUE_COUNT
from Configs.GPT_Setting import TIME_OUT

from Keyboards import reset_context_keyboard


async def cmd_gpt(message: types.Message):
    print("-----Gotcha-----")
    message_text = message.text
    chat_id = message.from_user.id

    print(f"User: {message.chat.first_name}")
    print(f"message: {message_text}")
    print(f"id: {chat_id}")

    user_messages = [
        {"role": "system", "content": DEFAULT_MOD},
        {"role": "user", "content": message_text}]

    try:
        completion = await openai_async.chat_complete(
            OPENAI_KEY,
            timeout=TIME_OUT,
            payload={
                "model": MODEL,
                "user_messages": user_messages,
                "temperature": TEMPERATURE,
                "n": MAX_VALUE_COUNT
            }
        )

        content = completion.json()["choices"][0]["message"]["content"]
        await message.answer(content, reply_markup=reset_context_keyboard)
        print(f"send: {content}")

    except Exception as err:
        print(err.args)
        await message.answer(ERROR_RESPONSE_MESSAGE)

    print("----------------\n")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_gpt)
