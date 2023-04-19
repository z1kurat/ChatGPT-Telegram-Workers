from aiogram import types

from Bot_Command.utilitesGPT import collectUserDialog
from Bot_Command.utilitesGPT import chatComplete
from Bot_Command.utilitesGPT import saveUserParameters

from Configs.templateResponses import ERROR_RESPONSE_MESSAGE
from Configs.templateResponses import START_RESPONSE

from DataBase import DB

from SetupBot.Setup import logger_history

import Keyboards


async def gpt(message: types.Message, message_text):
    user_id = message.from_user.id
    start_message = await message.answer(START_RESPONSE,
                                         disable_notification=True,
                                         reply_markup=Keyboards.remove_keyboard)

    is_dialog_correct, current_dialog = await collectUserDialog.get_user_dialog(user_id, message_text)

    if not is_dialog_correct:
        await DB.delete_user_history(user_id)

    response = await chatComplete.get_response_gpt(current_dialog)
    keyboard = Keyboards.reset_context_keyboard

    if response is not None:
        is_done = await saveUserParameters.save_message_history(user_id, message_text, response)
        if not is_done:  # !doDO: notify the user
            await DB.delete_user_history(user_id)
        logger_history.info(f"{message.chat.first_name} + {message.from_user.id} - Good!")

    if response is None:
        response = ERROR_RESPONSE_MESSAGE
        keyboard = Keyboards.reset_and_replay_keyboard
        logger_history.info(f"{message.chat.first_name} + {message.from_user.id} - Fail!")

    await start_message.delete()

    await message.answer(response, reply_markup=keyboard)

    await DB.set_work_state(user_id, False)
