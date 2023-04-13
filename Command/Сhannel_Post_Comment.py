from aiogram import types
from aiogram.dispatcher.filters import Command

import openai_async

from Configs.API import OPENAI_KEY

from Configs.GPT_Setting import MODEL
from Configs.GPT_Setting import TEMPERATURE
from Configs.GPT_Setting import MAX_VALUE_COUNT
from Configs.GPT_Setting import TIME_OUT
from Configs.GPT_Setting import STOP

from SetupBot.Setup import dp
from SetupBot.Setup import bot


@dp.message_handler(Command("comment"))
async def cmd_comment_gpt(message: types.Message):
    if message.chat.type != 'group':
        return

    print("-----Gotcha-----")

    message_text = message.text.split(' ', 1)[1]

    print(f"message: {message_text}")

    user_messages = [{"role": "system",
                      "content": "Тебя зовут - 'IT по-домашнему', ты комментируешь посты на русском языке Telegram канале. Твои посты короткие и "
                                 "забавные. Ты не даешь рекомендаций - ты только шутишь и комментируешь."},
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

        chat_id = message.chat.id
        post_id = message.reply_to_message.message_id

        await bot.send_message(chat_id, content, reply_to_message_id=post_id)

        await message.delete()

        print(f"send: {content}")
        print(f"message history: {user_messages}")

    except Exception as err:
        print(f"error: {err.args}")

    print("----------------\n")

