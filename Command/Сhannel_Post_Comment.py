from aiogram import types
from aiogram import Dispatcher

import openai_async

from Configs.API import OPENAI_KEY

from Configs.GPT_Setting import MODEL
from Configs.GPT_Setting import TEMPERATURE
from Configs.GPT_Setting import MAX_VALUE_COUNT
from Configs.GPT_Setting import TIME_OUT
from Configs.GPT_Setting import STOP

import Keyboards

from SetupBot.Setup import bot

from Filters.All import ForAll


async def cmd_gpt(message: types.Message):
    print("-----Gotcha-----")
    message_text = message.text

    print(f"message: {message_text}")

    user_messages = [{"role": "system",
                      "content": "Ты комментируешь на русском языке посты в Telegram канале. Твои посты короткие и "
                                 "забавные."},
                     {"role": "user", "content": message_text}]

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

        content = completion.json()["choices"][0]["message"]["content"]

        post_id = message.message_id
        chat_id = message.chat.id
        await bot.send_message(chat_id=chat_id, text=content, reply_to_message_id=post_id)

        print(f"send: {content}")
        print(f"message history: {user_messages}")

    except Exception as err:
        print(f"error: {err.args}")

    print("----------------\n")


def register_handlers(dp: Dispatcher):
    dp.register_channel_post_handler(cmd_gpt, ForAll())
