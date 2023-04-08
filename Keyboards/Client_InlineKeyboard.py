from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from Configs.Template_Responses import MESSAGE_TO_RESET_CONTEXT

from Command.Command_Name import RESET_COMMAND

reset_context_keyboard = InlineKeyboardMarkup(row_width=2)
enable_button = InlineKeyboardButton(text=MESSAGE_TO_RESET_CONTEXT, callback_data=RESET_COMMAND)
reset_context_keyboard.add(enable_button)
