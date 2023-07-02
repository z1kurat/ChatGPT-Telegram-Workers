from aiogram import types

buttons = [
    [
        types.InlineKeyboardButton(text="1 Месяц - 399 р.", callback_data="buy_subscription_1"),
        types.InlineKeyboardButton(text="🔥3 Месяца - 999 р.", callback_data="buy_subscription_3"),
     ],

    [types.InlineKeyboardButton(text="6 Месяцев - 1499", callback_data="buy_subscription_6")],

    [types.InlineKeyboardButton(text="↩Назад", callback_data="back_to_menu")]

]

subscription_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
