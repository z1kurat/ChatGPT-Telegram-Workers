from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from bot.data_base.models import Subscribers

from .abstract import Repository


class SubscribersRepo(Repository[Subscribers]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Subscribers, session=session)

    async def new(
            self,
            user_id: int,
            subscription_end_date: date
    ) -> Subscribers:
        """
        :param user_id: User telegram ID
        :param subscription_end_date: Subscription end date
        """
        new_subscribers = await self.session.merge(
            Subscribers(user_id=user_id,
                        subscription_end_date=subscription_end_date)
        )
        return new_subscribers
