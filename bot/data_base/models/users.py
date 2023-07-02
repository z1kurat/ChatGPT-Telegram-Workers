from dataclasses import dataclass
from datetime import date, datetime

from sqlalchemy import BigInteger, INTEGER, VARCHAR, DATE
from sqlalchemy.orm import mapped_column, Mapped

from bot.data_base.models import Base

from bot.parameters.limit_parametrs import MAX_USER_NAME, DEFAULT_TOKEN_COUNT_GPT

from bot.structures.enum.role import Role


@dataclass
class Users(Base):
    __tablename__ = 'users'

    # Telegram ID
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, primary_key=True)

    # Telegram user_client name
    user_name: Mapped[str] = mapped_column(VARCHAR(MAX_USER_NAME), unique=False, nullable=True)

    # Telegram user_client first name
    first_name: Mapped[str] = mapped_column(VARCHAR(MAX_USER_NAME), unique=False, nullable=True)

    # Telegram user_client second name
    second_name: Mapped[str] = mapped_column(VARCHAR(MAX_USER_NAME), unique=False, nullable=True)

    # Role: user_client, premium, admin
    role: Mapped[Role] = mapped_column(INTEGER, unique=False, nullable=False, default=Role.USER)

    # Balance in token
    balance: Mapped[int] = mapped_column(INTEGER, unique=False, default=DEFAULT_TOKEN_COUNT_GPT, nullable=False)

    # Registration date
    reg_data: Mapped[date] = mapped_column(DATE, default=datetime.now().date(), nullable=False)

    # Telegram ID by whom the users was invited
    referral_id: Mapped[int] = mapped_column(BigInteger, unique=False, nullable=True)

    def __str__(self) -> str:
        return f"<User: {self.user_id}>"
