from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.parameters.responses_template import SUBSCRIBE, URL_TO_SUBSCRIBE

subscriber_button = InlineKeyboardButton(text=SUBSCRIBE, url=URL_TO_SUBSCRIBE)
subscriber_keyboard = InlineKeyboardMarkup(inline_keyboard=[[subscriber_button]])
