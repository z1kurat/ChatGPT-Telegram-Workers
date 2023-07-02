from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands.commandName import START_COMMAND
from bot.parameters.responses_template import REGISTRATIONS

registrations_button = InlineKeyboardButton(text=REGISTRATIONS, callback_data=START_COMMAND)
registrations_keyboard = InlineKeyboardMarkup(inline_keyboard=[[registrations_button]])
