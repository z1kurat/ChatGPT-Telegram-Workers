from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.structures.data_structure import TransferData, TransferUserData
from bot.data_base import Database


class DatabaseMiddleware(BaseMiddleware):
    """This middleware throw a Database class to handler"""
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Union[TransferData, TransferUserData],
    ) -> Any:
        async with data.get("pool")() as session:
            data["db"] = Database(session)
            return await handler(event, data)
