from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Text

from bot.commands.commandName import SUBSCRIPTION_1, SUBSCRIPTION_3, SUBSCRIPTION_6
from bot.commands.users.profile.pay import send_invoice

from bot.filters import ChatTypeFilter

user_subscription_router = Router()


@user_subscription_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(SUBSCRIPTION_1),
    flags={"chat_action": "typing"})
async def cmd_subscription_1(callback: types.CallbackQuery, bot: Bot):
    """ Subscription to the bot for 1 month """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="Месяц подписки🤑",
                       description="Используй бота без ограничений один месяц...",
                       payload=SUBSCRIPTION_1,
                       label="399 руб.",
                       amount=39900)


@user_subscription_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(SUBSCRIPTION_3),
    flags={"chat_action": "typing"})
async def cmd_subscription_3(callback: types.CallbackQuery, bot: Bot):
    """ Subscription to the bot for 3 months """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="Три месяца подписки🤑",
                       description="Используй бота без ограничений три месяца...",
                       payload=SUBSCRIPTION_3,
                       label="999 руб.",
                       amount=99900)


@user_subscription_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(SUBSCRIPTION_6),
    flags={"chat_action": "typing"})
async def cmd_subscription_6(callback: types.CallbackQuery, bot: Bot):
    """ Subscription to the bot for 6 months """
    await send_invoice(bot=bot,
                       chat_id=callback.from_user.id,
                       title="Шесть месяцев подписки🤑",
                       description="Используй бота без ограничений шесть месяцев...",
                       payload=SUBSCRIPTION_6,
                       label="1499 руб.",
                       amount=149900)
