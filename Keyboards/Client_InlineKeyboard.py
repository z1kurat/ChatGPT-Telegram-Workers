from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from Configs.Template_Responses import MESSAGE_TO_RESET_CONTEXT
from Configs.Template_Responses import SUBSCRIBE
from Configs.Template_Responses import URL_TO_SUBSCRIBE

from Command.Command_Name import RESET_COMMAND

reset_context_keyboard = InlineKeyboardMarkup(row_width=2)
enable_button = InlineKeyboardButton(text=MESSAGE_TO_RESET_CONTEXT, callback_data=RESET_COMMAND)
reset_context_keyboard.add(enable_button)

subscriber_keyboard = InlineKeyboardMarkup(row_width=2)
button_to_subscribe = InlineKeyboardButton(text=SUBSCRIBE, url=URL_TO_SUBSCRIBE)
