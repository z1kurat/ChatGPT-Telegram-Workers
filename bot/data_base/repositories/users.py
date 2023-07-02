from datetime import date, datetime

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from bot.structures.enum.role import Role

from bot.data_base.models import Users

from .abstract import Repository

from ...parameters.limit_parametrs import DEFAULT_TOKEN_COUNT_GPT


class UserRepo(Repository[Users]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Users, session=session)

    async def new(
            self,
            user_id: int,
            user_name: Optional[str] = None,
            first_name: Optional[str] = None,
            second_name: Optional[str] = None,
            role: Optional[Role] = Role.USER,
            balance: int = DEFAULT_TOKEN_COUNT_GPT,
            reg_data: date = datetime.now().date(),
            referral_id: int = None
    ) -> Users:
        """
        :param referral_id: Telegram ID by whom the users was invited
        :param reg_data: Registrations data
        :param balance: Balance Users
        :param user_id: Telegram user_client id
        :param user_name: Telegram username
        :param first_name: Telegram profile first name
        :param second_name: Telegram profile second name
        :param role: User's role
        """
        new_user = await self.session.merge(
            Users(user_id=user_id,
                  user_name=user_name,
                  first_name=first_name,
                  second_name=second_name,
                  role=role,
                  balance=balance,
                  reg_data=reg_data,
                  referral_id=referral_id)
        )
        return new_user
