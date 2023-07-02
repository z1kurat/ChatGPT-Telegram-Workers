from aiogram import types

from bot.commands.commandName import BACK_TO_MENU, PROMO_CODE_COMMAND

buttons = [
    [types.InlineKeyboardButton(text="📲Ввести промокод", callback_data=PROMO_CODE_COMMAND)],
    [types.InlineKeyboardButton(text="↩Назад", callback_data=BACK_TO_MENU)]
]

promo_code_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
