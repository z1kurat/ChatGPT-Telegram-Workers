from sqlalchemy import BigInteger, INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped

from bot.data_base.models import Base

from bot.parameters.limit_parametrs import MAX_PROMO_CODE


class UsedPromoCodes(Base):
    __tablename__ = 'used_promo_codes'

    # Primary key
    id: Mapped[int] = mapped_column(INTEGER, unique=True, nullable=False, primary_key=True, autoincrement=True)

    # Telegram ID
    user_id: Mapped[int] = mapped_column(BigInteger, unique=False, nullable=False)

    # Telegram user_client name
    promo_code: Mapped[str] = mapped_column(VARCHAR(MAX_PROMO_CODE), unique=False, nullable=False)

    def __str__(self) -> str:
        return f"<User: {self.user_id}, {self.promo_code}>"
