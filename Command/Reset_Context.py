from aiogram import types
from aiogram.dispatcher.filters import Text, Command

from Command import GPT
from Configs.GPT_Setting import DEFAULT_MOD
from SetupBot.Setup import bot, logger_history
from SetupBot.Setup import dp

from Configs.Template_Responses import MESSAGE_RESET_CONTEXT, START_RESPONSE, ERROR_RESPONSE_MESSAGE

from DataBase import DB

from Command.Command_Name import RESET_COMMAND, REPLAY_COMMAND


@dp.callback_query_handler(Text(RESET_COMMAND))
async def cmd_enable_context(callback_query: types.CallbackQuery):
    await DB.del_all_message(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, MESSAGE_RESET_CONTEXT)
    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(Command(RESET_COMMAND))
async def cmd_enable_context_command(message: types.Message):
    await DB.del_all_message(message.from_user.id)
    await bot.send_message(message.from_user.id, MESSAGE_RESET_CONTEXT)


@dp.message_handler(Command(REPLAY_COMMAND))
async def cmd_replay_context_command(message: types.Message):
    user_id = message.from_user.id
    last_message = await DB.read_last_message(user_id)
    message = message.text

    import Keyboards
    start_response_message = await message.answer(START_RESPONSE,
                                                  disable_notification=True,
                                                  reply_markup=Keyboards.remove_keyboard)

    user_messages = await GPT.get_user_messages(user_id)

    user_messages.append({"role": "system", "content": DEFAULT_MOD})
    user_messages.append({"role": "user", "content": last_message})

    response = await GPT.get_response_gpt(user_messages)

    await start_response_message.delete()

    if response is None:
        await message.answer(ERROR_RESPONSE_MESSAGE, reply_markup=Keyboards.reset_and_replay_keyboard)
        return

    await message.answer(response, reply_markup=Keyboards.reset_context_keyboard)

    await GPT.save_data(user_id, last_message, response)

    logger_history.info(message.chat.first_name + " - Good!")