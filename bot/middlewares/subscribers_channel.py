from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware, Bot
from aiogram.enums import ChatMemberStatus
from aiogram.types import Message, TelegramObject, CallbackQuery

from bot.keyboards.misc import subscriber_keyboard
from bot.parameters.responses_template import SUBSCRIBER_TO_CHANNEL
from bot.structures.data_structure import TransferUserData, TransferData


class SubscribersMiddleware(BaseMiddleware):
    """ Checking channel subscription """
    def __init__(self, channel_id: int):
        super().__init__()
        self.channel_id = channel_id

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Union[TransferUserData, TransferData],
    ) -> Any:
        bot: Bot = data.get("bot")
        user = await bot.get_chat_member(self.channel_id, event.from_user.id)
        if user.status == ChatMemberStatus.LEFT or user.status == ChatMemberStatus.KICKED:
            await bot.send_message(text=SUBSCRIBER_TO_CHANNEL,
                                   chat_id=event.from_user.id,
                                   reply_markup=subscriber_keyboard)
            return
        return await handler(event, data)
