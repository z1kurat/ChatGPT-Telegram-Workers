from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from Configs.templateResponses import MESSAGE_TO_RESET_CONTEXT
from Configs.templateResponses import MESSAGE_TO_REPLAY
from Configs.templateResponses import SUBSCRIBE
from Configs.templateResponses import URL_TO_SUBSCRIBE

from Bot_Command.commandName import RESET_COMMAND
from Bot_Command.commandName import REPLAY_COMMAND

reset_button = InlineKeyboardButton(text=MESSAGE_TO_RESET_CONTEXT, callback_data=RESET_COMMAND)
replay_button = InlineKeyboardButton(text=MESSAGE_TO_REPLAY, callback_data=REPLAY_COMMAND)
button_to_subscribe = InlineKeyboardButton(text=SUBSCRIBE, url=URL_TO_SUBSCRIBE)

reset_context_keyboard = InlineKeyboardMarkup(row_width=2)
reset_context_keyboard.add(reset_button)

reset_and_replay_keyboard = InlineKeyboardMarkup(row_width=2)
reset_and_replay_keyboard.add(reset_button)
reset_and_replay_keyboard.add(replay_button)

subscriber_keyboard = InlineKeyboardMarkup(row_width=2)
subscriber_keyboard.add(button_to_subscribe)
