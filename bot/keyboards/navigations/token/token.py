from aiogram import types

from bot.commands.commandName import TOKEN_100, TOKEN_500, TOKEN_1000, BACK_TO_MENU

buttons = [
    [
        types.InlineKeyboardButton(text="🐥100 р. - 1000 токенов", callback_data=TOKEN_100),
        types.InlineKeyboardButton(text="🦊500 р. - 5000 токенов", callback_data=TOKEN_500),
     ],

    [types.InlineKeyboardButton(text="🐸1000 р. - 10.000 токенов", callback_data=TOKEN_1000)],

    [types.InlineKeyboardButton(text="↩Назад", callback_data=BACK_TO_MENU)]

]

token_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
