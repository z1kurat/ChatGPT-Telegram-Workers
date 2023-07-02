from aiogram import types

from bot.commands.commandName import TOKEN_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=TOKEN_MENU)]
]

token_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
