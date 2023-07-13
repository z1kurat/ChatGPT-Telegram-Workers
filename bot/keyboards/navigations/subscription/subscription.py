from aiogram import types

from bot.commands.commandName import SUBSCRIPTION_1, SUBSCRIPTION_3, SUBSCRIPTION_6, BACK_TO_MENU

buttons = [
    [
        types.InlineKeyboardButton(text="1 Месяц - 399 р.", callback_data=SUBSCRIPTION_1),
        types.InlineKeyboardButton(text="🔥3 Месяца - 999 р.", callback_data=SUBSCRIPTION_3),
     ],

    [types.InlineKeyboardButton(text="6 Месяцев - 1499", callback_data=SUBSCRIPTION_6)],

    [types.InlineKeyboardButton(text="↩Назад", callback_data=BACK_TO_MENU)]

]

subscription_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
