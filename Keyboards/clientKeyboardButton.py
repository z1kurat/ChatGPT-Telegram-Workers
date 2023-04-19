from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import KeyboardButton


enable_context = KeyboardButton('/enable_context')
disable_context = KeyboardButton('/disable_context')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True)

kb_client.add(enable_context)
kb_client.add(disable_context)

remove_keyboard = ReplyKeyboardRemove()

