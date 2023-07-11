from os import getenv

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Text
from aiogram.types import LabeledPrice

from bot.commands.commandName import TOKEN_100, TOKEN_500, TOKEN_1000

from bot.filters import ChatTypeFilter

user_token_router = Router()


async def send_invoice(bot: Bot,
                       chat_id: int,
                       title: str,
                       description: str,
                       payload: str,
                       label: str,
                       amount: int,
                       currency: str = 'rub',
                       start_parameter: str = 'gpt',
                       protect_content: bool = True):
    """
    Function for invoicing for service payment
    :param bot: Telegram bot
    :param chat_id: User Telegram ID
    :param title: Title for product
    :param description: Description for product
    :param payload: Unique Product Identifier
    :param label: Short product name
    :param amount: The cost of the product in minimum currency values
    :param currency: The currency in which the payment is accepted
    :param start_parameter: A value that should not be left empty
    :param protect_content: Is it possible to pay outside the dialogue with the bot
    :return: None
    """
    await bot.send_invoice(chat_id=chat_id,
                           title=title,
                           description=description,
                           payload=payload,
                           provider_token=getenv("UKASSA_TOKEN"),
                           currency=currency,
                           prices=[LabeledPrice(
                               label=label,
                               amount=amount)
                           ],
                           start_parameter=start_parameter,
                           protect_content=protect_content)


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


