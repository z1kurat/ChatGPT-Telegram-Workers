from aiogram import types, Router, Bot, F

from bot.commands.commandName import TOKEN_100, TOKEN_500, TOKEN_1000
from bot.data_base.models import Users
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.responses_template import SUCCESSFUL_PAY

user_pay_router = Router()


@user_pay_router.pre_checkout_query()
async def processing_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)


@user_pay_router.message(types.ContentType.SUCCESSFUL_PAYMENT == F.content_type)
async def processing_pay(message: types.Message, user: Users):
    token: int = 0
    if message.successful_payment.invoice_payload == TOKEN_100:
        token = 1000
    elif message.successful_payment.invoice_payload == TOKEN_500:
        token = 5000
    elif message.successful_payment.invoice_payload == TOKEN_1000:
        token = 10000

    user.balance += token
    await message.answer(text=SUCCESSFUL_PAY.format(token))
