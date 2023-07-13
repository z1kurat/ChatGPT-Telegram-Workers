from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Text

from bot.commands.commandName import TOKEN_100, TOKEN_500, TOKEN_1000
from bot.commands.users.profile.pay import send_invoice

from bot.filters import ChatTypeFilter

user_token_router = Router()


@user_token_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(TOKEN_100),
    flags={"chat_action": "typing"})
async def cmd_token_100(callback: types.CallbackQuery, bot: Bot):
    """ Billing for 1000 tokens """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="1000 токенов🤑",
                       description="Покупка 1000 токнов - 100 руб.",
                       payload=TOKEN_100,
                       label="100 руб.",
                       amount=10000)


@user_token_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(TOKEN_500),
    flags={"chat_action": "typing"})
async def cmd_token_100(callback: types.CallbackQuery, bot: Bot):
    """ Billing for 5000 tokens """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="5000 токенов🤑",
                       description="Покупка 5000 токнов - 500 руб.",
                       payload=TOKEN_500,
                       label="500 руб.",
                       amount=50000)


@user_token_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(TOKEN_1000),
    flags={"chat_action": "typing"})
async def cmd_token_100(callback: types.CallbackQuery, bot: Bot):
    """ Billing for 10.000 tokens """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="10.000 токенов🤑",
                       description="Покупка 10.000 токнов - 1000 руб.",
                       payload=TOKEN_1000,
                       label="1000 руб.",
                       amount=100000)


