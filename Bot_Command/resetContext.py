from aiogram import types

from SetupBot.Setup import bot

from Configs.templateResponses import MESSAGE_RESET_CONTEXT

from DataBase import DB


async def reset_conntext(message: types.Message, is_callback=False, callback_id=-1):
    user_id = message.chat.id
    try:
        await DB.delete_user_history(user_id)
        await bot.send_message(user_id, MESSAGE_RESET_CONTEXT, disable_notification=True)

        if is_callback:
            await bot.answer_callback_query(callback_id)
    finally:
        await DB.set_work_state(user_id, False)


async def reset_context_callback(callback_query: types.CallbackQuery):
    await reset_conntext(callback_query.message, True, callback_query.id)


async def reset_context_cmd(message: types.Message):
    await reset_conntext(message.chat.id, False)

