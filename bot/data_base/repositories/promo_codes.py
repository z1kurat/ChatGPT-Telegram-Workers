from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import DATE

from bot.data_base.models import PromoCodes

from .abstract import Repository


class PromoCodeRepo(Repository[PromoCodes]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=PromoCodes, session=session)

    async def new(
        self,
        promo_code: str,
        end_time: DATE
    ) -> PromoCodes:
        """
        :param promo_code: Promo code
        :param end_time: End time promo code
        """
        new_promo_code = await self.session.merge(
            PromoCodes(
                promo_code=promo_code,
                end_time=end_time
            )
        )
        return new_promo_code
