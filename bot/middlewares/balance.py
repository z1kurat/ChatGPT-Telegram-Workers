from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message

from bot.data_base.models import Users
from bot.structures.data_structure import TransferUserData, TransferData
from bot.parameters.responses_template import NOT_ENOUGH_FUNDS
from bot.structures import Role


class BalanceMiddleware(BaseMiddleware):
    """ Checking the user's balance """
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Union[TransferUserData, TransferData],
    ) -> Any:
        role: Role = data.get("role")

        if role == Role.PREMIUM or role == Role.ADMINISTRATOR:
            return await handler(event, data)

        user: Users = data.get("user")
        balance = user.balance

        if balance <= 0:
            await event.answer(NOT_ENOUGH_FUNDS, reply_markup=None)
            return

        return await handler(event, data)
