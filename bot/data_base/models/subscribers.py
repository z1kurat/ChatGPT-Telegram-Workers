from dataclasses import dataclass
from datetime import date, datetime

from sqlalchemy import BigInteger, DATE
from sqlalchemy.orm import mapped_column, Mapped

from bot.data_base.models import Base


@dataclass
class Subscribers(Base):
    __tablename__ = 'subscribers'

    # Telegram ID
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, primary_key=True)

    # Subscription end date
    subscription_end_date: Mapped[date] = mapped_column(DATE, default=datetime.now().date(), nullable=False)

    def __str__(self) -> str:
        return f"<Subscribers: {self.user_id}, {self.subscription_end_date}>"
