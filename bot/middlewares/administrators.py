from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.structures import Role
from bot.structures.data_structure import TransferUserData, TransferData


class AdministratorsMiddleware(BaseMiddleware):
    """ A class for verifying that a user has an administrator status """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        role: Role = data.get("role")
        if role != Role.ADMINISTRATOR:
            return False

        return await handler(event, data)
