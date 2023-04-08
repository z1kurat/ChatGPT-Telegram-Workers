from aiogram import types
from aiogram import Dispatcher

import openai_async

from DataBase import DB

from SetupBot.Setup import db

from Configs.API import OPENAI_KEY
from Configs.Template_Responses import ERROR_RESPONSE_MESSAGE
from Configs.GPT_Setting import DEFAULT_MOD
from Configs.GPT_Setting import MODEL
from Configs.GPT_Setting import TEMPERATURE
from Configs.GPT_Setting import MAX_VALUE_COUNT
from Configs.GPT_Setting import TIME_OUT

import Keyboards


async def cmd_gpt(message: types.Message):
    print("-----Gotcha-----")
    message_text = message.text
    user_id = message.from_user.id

    print(f"User: {message.chat.first_name}")
    print(f"message: {message_text}")
    print(f"id: {user_id}")

    user_messages = await DB.read_message_history(user_id, db)

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": message_text})

    print(f"history: {user_messages}")

    try:
        completion = await openai_async.chat_complete(
            OPENAI_KEY,
            timeout=TIME_OUT,
            payload={
                "model": MODEL,
                "messages": user_messages,
                "temperature": TEMPERATURE,
                "n": MAX_VALUE_COUNT
            }
        )

        content = completion.json()["choices"][0]["message"]["content"]
        await message.answer(content, reply_markup=Keyboards.reset_context_keyboard)
        print(f"send: {content}")

        await DB.save_message_history(user_id, "user", message_text, db)
        await DB.save_message_history(user_id, "assistant", content, db)

        await DB.del_old_message(user_id, db)

    except Exception as err:
        print(err.args)
        await message.answer(ERROR_RESPONSE_MESSAGE)

    print("----------------\n")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_gpt)
