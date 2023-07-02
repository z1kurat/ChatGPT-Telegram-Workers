from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.data_base.models import Users
from bot.structures import Role
from bot.structures.data_structure import TransferUserData, TransferData


class RoleMiddleware(BaseMiddleware):
    """ A class for defining the users role """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        user: Users = data.get("user")
        data["role"] = Role(user.role)
        return await handler(event, data)
