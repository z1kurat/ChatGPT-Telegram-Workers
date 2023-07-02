from aiogram import types

from bot.commands.commandName import REFERRAL_MENU, PROMO_CODE_MENU, TOKEN_MENU, SUBSCRIPTION_MENU, HELP_MENU,\
                                     SETTINGS_MENU

buttons = [
    [
        types.InlineKeyboardButton(text="💎Подписка", callback_data=SUBSCRIPTION_MENU),
        types.InlineKeyboardButton(text="🟡Токены", callback_data=TOKEN_MENU)
    ],

    [
        types.InlineKeyboardButton(text="🆘Помощь", callback_data=HELP_MENU),
        types.InlineKeyboardButton(text="⚙Настройки бота", callback_data=SETTINGS_MENU)
    ],

    [types.InlineKeyboardButton(text="🎟️Промокоды", callback_data=PROMO_CODE_MENU)],

    [types.InlineKeyboardButton(text="🫂Рефералы", callback_data=REFERRAL_MENU)]
]

menu_keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
