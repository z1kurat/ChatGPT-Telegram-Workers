from aiogram import types

from SetupBot.Setup import bot

from Configs.templateResponses import MESSAGE_RESET_CONTEXT

from DataBase import DB


async def reset_conntext(user_id, is_callback=False, callback_id=-1):
    await DB.delete_user_history(user_id)
    await bot.send_message(user_id, MESSAGE_RESET_CONTEXT, disable_notification=True)

    if is_callback:
        await bot.answer_callback_query(callback_id)

    await DB.set_work_state(user_id, False)


async def reset_context_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    callback_id = callback_query.id
    await reset_conntext(user_id, True, callback_id)


async def reset_context_cmd(message: types.Message):
    user_id = message.from_user.id
    await reset_conntext(user_id, False)

