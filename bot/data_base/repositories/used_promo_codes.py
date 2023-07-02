from sqlalchemy.ext.asyncio import AsyncSession
from bot.data_base.models import UsedPromoCodes

from .abstract import Repository


class UsedPromoCodeRepo(Repository[UsedPromoCodes]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=UsedPromoCodes, session=session)

    async def new(
        self,
        user_id: int,
        promo_code: str
    ) -> UsedPromoCodes:
        """
        :param promo_code: Use promo code
        :param user_id: User Telegram ID
        """
        new_used_promo_code = await self.session.merge(
            UsedPromoCodes(
                user_id=user_id,
                promo_code=promo_code
            )
        )
        return new_used_promo_code
