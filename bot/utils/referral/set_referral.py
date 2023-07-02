from aiogram import types, Bot

from bot.data_base.models import Users
from bot.data_base import Database
from bot.parameters.limit_parametrs import REFERRAL_TOKEN_COUNT
from bot.parameters.responses_template import REFERRAL_OF_YOURSELF, REFERRAL_SUCCESS, \
    REFERRAL_NOT_EXIST, YOUR_REFERRAL_SUCCESS, REFERRAL_UNAVAILABLE, REFERRAL_EXIST, REFERRAL_BAD_CODE


async def set_referral_by_user(
        user: Users,
        referral_id_str: str,
        message: types.Message,
        db: Database,
        bot: Bot) -> bool:
    """
    Checking the correctness for adding a referral and adding a referral
    :param referral_id_str: Telegram ID referral
    :param user: Current users
    :param message: Current message
    :param db: Database
    :param bot: Telegram bot
    :return:
    """
    if not referral_id_str.isdigit():
        await message.answer(REFERRAL_BAD_CODE)
        return False

    referral_id = int(referral_id_str)

    if referral_id == message.from_user.id:
        await message.answer(REFERRAL_OF_YOURSELF)
        return False

    ref_user = await db.users.get(referral_id)
    if ref_user is None:
        await message.answer(REFERRAL_NOT_EXIST)
        return False

    if user.referral_id is not None:
        current_ref = await db.users.get(user.referral_id)
        await message.answer(REFERRAL_EXIST.format(current_ref.user_name))
        return False

    await message.answer(REFERRAL_SUCCESS.format(ref_user.user_name, REFERRAL_TOKEN_COUNT))

    try:
        await bot.send_message(chat_id=ref_user.user_id,
                               text=YOUR_REFERRAL_SUCCESS.format(user.user_name, REFERRAL_TOKEN_COUNT))
    except:
        await message.answer(REFERRAL_UNAVAILABLE, disable_notification=True)

    user.balance += REFERRAL_TOKEN_COUNT
    user.referral_id = referral_id

    ref_user.balance += REFERRAL_TOKEN_COUNT

    return True
