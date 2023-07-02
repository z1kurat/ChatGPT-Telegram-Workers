from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.parameters.responses_template import MESSAGE_TO_RESET_CONTEXT, MESSAGE_TO_REPLAY
from bot.commands.commandName import RESET_COMMAND, REPLAY_COMMAND

reset_button = InlineKeyboardButton(text=MESSAGE_TO_RESET_CONTEXT, callback_data=RESET_COMMAND)

replay_button = InlineKeyboardButton(text=MESSAGE_TO_REPLAY, callback_data=REPLAY_COMMAND)

reset_context_keyboard = InlineKeyboardMarkup(inline_keyboard=[[reset_button]])
reset_and_replay_keyboard = InlineKeyboardMarkup(inline_keyboard=[[reset_button], [replay_button]])
