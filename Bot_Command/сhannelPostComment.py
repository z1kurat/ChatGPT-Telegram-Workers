from aiogram import types

from Bot_Command.utilitesGPT import chatComplete

from Configs.templateResponses import ERROR_RESPONSE_MESSAGE

from SetupBot.Setup import bot

from Configs.parametersGPT import DEFAULT_POST_MOD


async def comment_gpt_cmd(message: types.Message):
    # !doDO: add a check from message
    message_text = message.text.split(' ', 1)[1]

    user_messages = [{"role": "system", "content": DEFAULT_POST_MOD},
                     {"role": "user", "content": message_text}]

    response = await chatComplete.get_response_gpt(user_messages)

    if response is None:
        response = ERROR_RESPONSE_MESSAGE

    await bot.send_message(message.chat.id, response, reply_to_message_id=message.reply_to_message.message_id,
                           disable_notification=True)

    await message.delete()

