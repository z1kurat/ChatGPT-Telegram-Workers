from os import getenv

import datetime
import calendar

from aiogram import types, Router, Bot, F
from aiogram.types import LabeledPrice

from bot.commands.commandName import TOKEN_100, TOKEN_500, TOKEN_1000, SUBSCRIPTION_1, SUBSCRIPTION_3, SUBSCRIPTION_6
from bot.data_base import Database
from bot.data_base.models import Users, Subscribers
from bot.parameters.responses_template import SUCCESSFUL_PAY, SUCCESSFUL_SUBSCRIBER
from bot.structures import Role

user_pay_router = Router()


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


@user_pay_router.pre_checkout_query()
async def processing_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery, bot: Bot):
    """ Confirmation of product availability """
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)


async def add_token(user: Users, invoice_payload: str) -> str:
    """ Adds the required amount of toxins to the user and returns the final status line """
    token: int = 0
    if invoice_payload == TOKEN_100:
        token = 1000
    elif invoice_payload == TOKEN_500:
        token = 5000
    elif invoice_payload == TOKEN_1000:
        token = 10000

    user.balance += token
    return SUCCESSFUL_PAY.format(token)


async def subscription_user(user: Users, db: Database, subscriber: Subscribers, invoice_payload: str) -> str:
    """ Sets the premium status to the user and returns progress information """
    today = datetime.datetime.now()
    current_subscription_end_date = subscriber.subscription_end_date if subscriber else today
    date_end_subscription = max(today, current_subscription_end_date)

    mount: int = 0

    if invoice_payload == SUBSCRIPTION_1:
        mount = 1
    elif invoice_payload == SUBSCRIPTION_3:
        mount = 3
    elif invoice_payload == SUBSCRIPTION_6:
        mount = 6

    date_end_subscription = add_months(date_end_subscription, mount)

    if not subscriber:
        await db.subscribers.new(user_id=user.user_id,
                                 subscription_end_date=date_end_subscription)
    else:
        subscriber.subscription_end_date = date_end_subscription

    user.role = Role.PREMIUM

    return SUCCESSFUL_SUBSCRIBER.format(mount)


@user_pay_router.message(types.ContentType.SUCCESSFUL_PAYMENT == F.content_type)
async def processing_pay(message: types.Message, user: Users, db: Database, subscriber: Subscribers):
    """ Main payment processing function """
    invoice_payload = message.successful_payment.invoice_payload

    token_invoice_payload = [TOKEN_100, TOKEN_500, TOKEN_1000]
    subscription_invoice_payload = [SUBSCRIPTION_1, SUBSCRIPTION_3, SUBSCRIPTION_6]

    response = ""

    if invoice_payload in token_invoice_payload:
        response = await add_token(user, invoice_payload)
    elif invoice_payload in subscription_invoice_payload:
        response = await subscription_user(user, db, subscriber, invoice_payload)

    await message.answer(response)


def add_months(date: datetime, months: int):
    """
    Func to add mounts at date
    :param date: The date to which months of months will be added
    :param months: Number of months to be added
    :return:
    """

    months_count = date.month + months
    year = date.year + int(months_count / 12)

    month = (months_count % 12)
    if month == 0:
        month = 12

    day = date.day
    last_day_of_month = calendar.monthrange(year, month)[1]
    if day > last_day_of_month:
        day = last_day_of_month

    return datetime.date(year, month, day)
