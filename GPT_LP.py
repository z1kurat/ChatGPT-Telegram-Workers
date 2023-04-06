import asyncio

import logging

import openai
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from Config import TELEGRAM_BOT_TOKEN
from Config import OPENAI_KEY

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_KEY


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message_handler()
async def gpt(message: types.Message):
    print("-----Gotcha-----")
    message_text = message.text
    chat_id = message.from_user.id

    print(f"User: {message.chat.first_name}")
    print(f"message: {message_text}")
    print(f"id: {chat_id}")

    messages = [
        {"role": "system", "content": "You are a kind and helpful assistant who gives detailed and useful answers"},
        {"role": "user", "content": message_text}]

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            n=1
        )

        await bot.send_message(chat_id, completion.choices[0].message.content)
        print(f"send: {completion.choices[0].message.content}")

    except Exception as err:
        await bot.send_message(chat_id, f"В данный момент невохможно обработать Ваш запрос. \n {err.args}")

    print("----------------\n")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
