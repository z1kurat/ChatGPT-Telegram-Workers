from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.data_base import Database
from bot.data_base.models import Users
from bot.structures.data_structure import TransferUserData, TransferData


class UserMiddleware(BaseMiddleware):
    """ A class for defining the users """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        db: Database = data.get("db")
        user: Users = await db.users.get(event.from_user.id)
        data["user"] = user

        handler_continue = None

        try:
            handler_continue = await handler(event, data)
        finally:
            await db.users.session.commit()
            return handler_continue
