from aiogram import types

from SetupBot.Setup import bot

from Configs.templateResponses import MESSAGE_RESET_CONTEXT

from DataBase import DB


async def reset_conntext(message: types.Message, is_callback=False, callback_id=-1):
    user_id = message.from_user.id

    await DB.delete_user_history(user_id)
    await bot.send_message(user_id, MESSAGE_RESET_CONTEXT)

    if is_callback:
        await bot.answer_callback_query(callback_id)

    await DB.set_work_state(user_id, False)


async def reset_context_callback(callback_query: types.CallbackQuery):
    message = callback_query.message
    callback_id = callback_query.id
    await reset_conntext(message, True, callback_id)


async def reset_context_cmd(message: types.Message):
    await reset_conntext(message)

