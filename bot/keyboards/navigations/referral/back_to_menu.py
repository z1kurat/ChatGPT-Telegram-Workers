from aiogram import types

from bot.commands.commandName import REFERRAL_MENU

buttons = [
    [types.InlineKeyboardButton(text="⛔Отменить", callback_data=REFERRAL_MENU)]
]

referral_back_menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
