from aiogram import types
from aiogram import Dispatcher

import openai_async

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

import Keyboards


@dp.message_handler(IsSubscriber())
async def cmd_gpt(message: types.Message):
    print("-----Gotcha-----")
    message_text = message.text
    user_id = message.from_user.id

    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    print(f"User: {message.chat.first_name}")
    print(f"message: {message_text}")
    print(f"id: {user_id}")

    user_messages = await DB.read_message_history(user_id)

    if user_messages is None:
        user_messages = []

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": message_text})

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

        await start_response_message.delete()

        content = completion.json()["choices"][0]["message"]["content"]
        await message.answer(content, reply_markup=Keyboards.reset_context_keyboard)

        print(f"send: {content}")
        print(f"message history: {user_messages}")

        await DB.save_message_history(user_id, "user", message_text)
        await DB.save_message_history(user_id, "assistant", content)

        # await DB.del_old_message(user_id)

    except Exception as err:
        print(f"error: {err.args}")
        await message.answer(ERROR_RESPONSE_MESSAGE)

    print("----------------\n")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_gpt, IsSubscriber())
