from aiogram import types

from bot.commands.commandName import HELP_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=HELP_MENU)]
]

help_back_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
