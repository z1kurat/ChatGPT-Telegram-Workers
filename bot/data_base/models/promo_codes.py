from datetime import date

from sqlalchemy import DATE, VARCHAR, INT
from sqlalchemy.orm import mapped_column, Mapped

from bot.data_base.models import Base

from bot.parameters.limit_parametrs import MAX_PROMO_CODE


class PromoCodes(Base):
    __tablename__ = 'promo_codes'
    # promo code
    promo_code: Mapped[str] = mapped_column(VARCHAR(MAX_PROMO_CODE), unique=True, nullable=False, primary_key=True)

    # token
    token: Mapped[int] = mapped_column(INT, unique=False, nullable=False, primary_key=False)

    # is promo code active
    end_time: Mapped[date] = mapped_column(DATE, unique=False, nullable=False)

    def __str__(self) -> str:
        return f"<User: {self.promo_code}>"
