from aiogram import types

import Keyboards

from Bot_Command import GPT

from SetupBot.Setup import bot

from Configs.Template_Responses import MESSAGE_RESET_CONTEXT, AWAIT_RESPONSE_MESSAGE

from DataBase import DB


async def cmd_enable_context(callback_query: types.CallbackQuery):
    message = callback_query.message
    user_id = callback_query.from_user.id

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await DB.set_working(user_id, True)

    await DB.del_all_message(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, MESSAGE_RESET_CONTEXT)
    await bot.answer_callback_query(callback_query.id)

    await DB.set_working(callback_query.from_user.id, False)


async def cmd_enable_context_command(message: types.Message):
    user_id = message.from_user.id

    ready_to_work = await GPT.prepare_for_work(user_id)

    if not ready_to_work:
        await message.answer(AWAIT_RESPONSE_MESSAGE, disable_notification=True, reply_markup=Keyboards.remove_keyboard)
        return

    await DB.set_working(user_id, True)

    await DB.del_all_message(user_id)
    await bot.send_message(message.from_user.id, MESSAGE_RESET_CONTEXT)

    await DB.set_working(user_id, False)
