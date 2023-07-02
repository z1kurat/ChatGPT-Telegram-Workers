import enum

from aiogram.fsm.state import StatesGroup, State


class OrderPromoCode(StatesGroup):
    promo_code_registrations = State()


class PromoCodeStatus(enum.IntEnum):
    ACTIVE = 0
    USED = 1
    DISABLE = 2
    NONE = 3
