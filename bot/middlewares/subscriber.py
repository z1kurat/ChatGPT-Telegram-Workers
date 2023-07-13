from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.data_base import Database
from bot.data_base.models import Subscribers
from bot.structures.data_structure import TransferUserData, TransferData


class SubscriberMiddleware(BaseMiddleware):
    """ A class for defining the subscriber """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        db: Database = data.get("db")
        subscriber: Subscribers = await db.subscribers.get(event.from_user.id)
        data["subscriber"] = subscriber

        handler_continue = None

        try:
            handler_continue = await handler(event, data)
        finally:
            await db.subscribers.session.commit()
            return handler_continue
