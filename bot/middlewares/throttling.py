from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.cache import Cache
from bot.structures.data_structure import TransferUserData, TransferData
from bot.parameters.responses_template import THROTTLED_MESSAGE


class ThrottlingMiddleware(BaseMiddleware):
    """ This class serves to ban the flood """
    SENT_THROTTLED_MESSAGE = 1
    NOT_SENT_THROTTLED_MESSAGE = 0

    RATE_LIMIT = 1

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Union[TransferUserData, TransferData],
    ) -> Any:
        cache: Cache = data.get("cache")

        user_id = event.from_user.id
        radis_key = f"throttling_{user_id}"

        user_session_binary = await cache.misc_client.get(radis_key)

        if user_session_binary:
            user_session = int(user_session_binary.decode())
            if user_session == self.NOT_SENT_THROTTLED_MESSAGE:
                await cache.misc_client.set(radis_key, self.SENT_THROTTLED_MESSAGE, self.RATE_LIMIT)
                await event.answer(THROTTLED_MESSAGE.format(self.RATE_LIMIT))
                return
            return

        await cache.misc_client.set(radis_key, self.NOT_SENT_THROTTLED_MESSAGE, self.RATE_LIMIT)
        return await handler(event, data)
