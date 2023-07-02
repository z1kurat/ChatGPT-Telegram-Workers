from aiogram import types

from bot.commands.commandName import PROMO_CODE_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=PROMO_CODE_MENU)]
]

promo_code_back_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
