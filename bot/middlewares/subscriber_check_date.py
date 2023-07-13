import datetime
from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message

from bot.data_base.models import Users, Subscribers
from bot.structures.data_structure import TransferUserData, TransferData
from bot.structures import Role


class SubscriberCheckDateMiddleware(BaseMiddleware):
    """ Checking the premium users date """
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Union[TransferUserData, TransferData],
    ) -> Any:
        role: Role = data.get("role")

        if role != Role.PREMIUM:
            return await handler(event, data)

        subscriber: Subscribers = data.get("subscriber")

        if subscriber.subscription_end_date < datetime.datetime.now():
            user: Users = data.get("user")
            user.role = Role.USER

        return await handler(event, data)
