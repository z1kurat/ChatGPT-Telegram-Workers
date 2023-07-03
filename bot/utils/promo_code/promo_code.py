from datetime import datetime
from typing import Union

from bot.data_base.models import PromoCodes, UsedPromoCodes
from bot.data_base.repositories import PromoCodeRepo, UsedPromoCodeRepo
from bot.parameters.responses_template import PROMO_CODE_ACTIVE_STATUS, PROMO_CODE_NONE_STATUS, PROMO_CODE_USED_STATUS,\
                                              PROMO_CODE_DISABLE_STATUS
from bot.structures.enum.promo_code import PromoCodeStatus


async def check_users_promo_code(
        input_code: str,
        user_id: int,
        promo_codes: PromoCodeRepo,
        used_promo_codes: UsedPromoCodeRepo
) -> [PromoCodeStatus, Union[int, None]]:
    """ Checking the availability of a promo code in the database """
    promo_code: PromoCodes = await promo_codes.get_by_where(promo_codes.promo_code == input_code)

    if promo_code is None:
        return PromoCodeStatus.NONE, None

    if promo_code.end_time <= datetime.now().date():
        return PromoCodeStatus.DISABLE, None

    used_promo_code = await used_promo_codes.get_by_where(UsedPromoCodes.user_id == user_id
                                                          and UsedPromoCodes.promo_code == input_code)

    if used_promo_code is not None:
        return PromoCodeStatus.USED, None

    return PromoCodeStatus.ACTIVE, promo_code.token


async def get_message_by_promo_code_status(pomo_code_status: PromoCodeStatus) -> str:
    """ Return message status by promo code status """
    if pomo_code_status == PromoCodeStatus.ACTIVE:
        return PROMO_CODE_ACTIVE_STATUS

    if pomo_code_status == PromoCodeStatus.USED:
        return PROMO_CODE_USED_STATUS

    if pomo_code_status == PromoCodeStatus.DISABLE:
        return PROMO_CODE_DISABLE_STATUS

    if pomo_code_status == PromoCodeStatus.NONE:
        return PROMO_CODE_NONE_STATUS


async def update_used_promo_code(
        promo_code: str,
        user_id: int,
        used_promo_codes: UsedPromoCodeRepo
) -> None:
    """ Update used promo code database """
    await used_promo_codes.new(user_id=user_id, promo_code=promo_code)
