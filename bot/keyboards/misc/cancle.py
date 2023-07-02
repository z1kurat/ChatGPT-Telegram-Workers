from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands.commandName import CANCEL_COMMAND
from bot.parameters.responses_template import TO_CANCEL_MESSAGE

cancel_button = InlineKeyboardButton(text=TO_CANCEL_MESSAGE, callback_data=CANCEL_COMMAND)
cancel_keyboard = InlineKeyboardMarkup(inline_keyboard=[[cancel_button]])
