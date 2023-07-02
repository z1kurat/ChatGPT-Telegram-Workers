from aiogram import types

buttons = [
    [types.InlineKeyboardButton(text="↩Назад", callback_data="back_to_menu")]
]

help_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
