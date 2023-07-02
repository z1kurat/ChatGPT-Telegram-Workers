from aiogram import types

from bot.commands.commandName import SETTINGS_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=SETTINGS_MENU)]
]

settings_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
