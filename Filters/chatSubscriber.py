from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler

from Configs.channel import ID_CHANNEL
from Configs.templateResponses import SUBSCRIBER_TO_CHANNEL

from SetupBot.Setup import bot

import Keyboards


class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        sub = await bot.get_chat_member(chat_id=ID_CHANNEL, user_id=message.from_user.id)
        if sub.status == types.ChatMemberStatus.MEMBER \
                or sub.status == types.ChatMemberStatus.ADMINISTRATOR \
                or sub.status == types.ChatMemberStatus.OWNER:

            return True

        await message.answer(text=SUBSCRIBER_TO_CHANNEL,
                             reply_markup=Keyboards.subscriber_keyboard)

        raise CancelHandler()

