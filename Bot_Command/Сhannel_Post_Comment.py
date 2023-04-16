from aiogram import types
from aiogram.dispatcher.filters import Command

from Bot_Command.Command_Name import COMMENT_COMMAND

from Bot_Command import GPT

from SetupBot.Setup import dp
from SetupBot.Setup import bot


@dp.message_handler(Command(COMMENT_COMMAND))
async def cmd_comment_gpt(message: types.Message):
    if message.chat.type != 'supergroup':
        return

    message_text = message.text.split(' ', 1)[1]

    user_messages = [{"role": "system",
                      "content": "Тебя зовут - 'IT по-домашнему', ты комментируешь посты на русском языке Telegram канале. Твои посты короткие и "
                                 "забавные. Ты не даешь рекомендаций - ты только шутишь и комментируешь."},
                     {"role": "user", "content": message_text}]

    response = await GPT.get_response_gpt(user_messages)

    chat_id = message.chat.id
    post_id = message.reply_to_message.message_id

    await bot.send_message(chat_id, response, reply_to_message_id=post_id)

    await message.delete()

