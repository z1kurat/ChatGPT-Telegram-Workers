from aiogram import types

from bot.commands.commandName import SUBSCRIPTION_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=SUBSCRIPTION_MENU)]
]

subscription_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
