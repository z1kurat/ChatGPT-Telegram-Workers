from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, TelegramObject, CallbackQuery
from aiogram.dispatcher.flags import get_flag

from bot.data_base import Database
from bot.keyboards.misc import registrations_keyboard
from bot.parameters.responses_template import REGISTRATIONS_MESSAGE
from bot.structures.data_structure import TransferUserData, TransferData


class RegistrationsMiddleware(BaseMiddleware):
    """ Checking whether the users are registered in the database """
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Union[TransferUserData, TransferData],
    ) -> Any:
        enable_registrations = get_flag(data, "registrations")

        if enable_registrations is not None and not enable_registrations:
            return await handler(event, data)

        bot: Bot = data.get("bot")
        async with data.get("pool")() as session:
            database = Database(session)
            exists = await database.users.exists(event.from_user.id)
            if not exists:
                await bot.send_message(chat_id=event.from_user.id,
                                       text=REGISTRATIONS_MESSAGE,
                                       reply_markup=registrations_keyboard)
                return False

        return await handler(event, data)
