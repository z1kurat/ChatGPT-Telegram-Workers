from typing import Union

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from bot.structures import conf

from .repositories import UserRepo, PromoCodeRepo, UsedPromoCodeRepo


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    """
    :param url:
    :return:
    """
    return _create_async_engine(
        url=url, echo=conf.debug, pool_pre_ping=True
    )


def create_session_maker(engine: AsyncEngine = None) -> sessionmaker:
    """
    :param engine:
    :return:
    """
    return sessionmaker(
        engine or create_async_engine(conf.db.build_connection_str()),
        class_=AsyncSession,
        expire_on_commit=False,
    )


class Database:
    """
    Database class is the highest abstraction level of database and
    can be used in the commands or any others bot-side functions
    """

    users: UserRepo
    """ User repository """
    promo_codes: PromoCodeRepo
    """ Promo code repository """
    used_promo_codes: UsedPromoCodeRepo
    """ Used promo code repository """

    session: AsyncSession

    def __init__(
        self, session: AsyncSession,
            user: UserRepo = None,
            promo_code: PromoCodeRepo = None,
            used_pomo_code: UsedPromoCodeRepo = None,
    ):
        self.session = session
        self.users = user or UserRepo(session=session)
        self.promo_codes = promo_code or PromoCodeRepo(session=session)
        self.used_promo_codes = used_pomo_code or UsedPromoCodeRepo(session=session)
