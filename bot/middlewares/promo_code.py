from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.data_base import Database
from bot.structures.data_structure import TransferUserData, TransferData


class PromoCodeMiddleware(BaseMiddleware):
    """ A class for defining the promo code """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        db: Database = data.get("db")
        data["promo_codes"] = db.promo_codes

        handler_continue = None

        try:
            handler_continue = await handler(event, data)
        finally:
            await db.promo_codes.session.commit()
            return handler_continue
