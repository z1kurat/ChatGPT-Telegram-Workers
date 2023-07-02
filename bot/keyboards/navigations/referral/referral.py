from aiogram import types

from bot.commands.commandName import REFERRAL_CODE_LINK, REFERRAL_CODE_COMMAND, REFERRAL_ADD, BACK_TO_MENU

buttons = [
    [
        types.InlineKeyboardButton(text="🐊Получить ссылку", callback_data=REFERRAL_CODE_LINK),
        types.InlineKeyboardButton(text="🧸Получить код", callback_data=REFERRAL_CODE_COMMAND),
     ],

    [types.InlineKeyboardButton(text="👥Ввести код", callback_data=REFERRAL_ADD)],

    [types.InlineKeyboardButton(text="↩Назад", callback_data=BACK_TO_MENU)]

]

referral_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
