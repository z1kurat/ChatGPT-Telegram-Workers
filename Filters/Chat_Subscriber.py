from aiogram import types
from aiogram import Dispatcher

from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler

from Configs.Channel import ID_CHANNEL
from Configs.Template_Responses import SUBSCRIBER_TO_CHANNEL

from SetupBot.Setup import bot

import Keyboards


class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        if message.chat.type != 'private':
            raise CancelHandler()

        sub = await bot.get_chat_member(chat_id=ID_CHANNEL, user_id=message.from_user.id)
        if sub.status == types.ChatMemberStatus.MEMBER \
                or sub.status == types.ChatMemberStatus.ADMINISTRATOR \
                or sub.status == types.ChatMemberStatus.OWNER:

            return True

        await message.answer(text=SUBSCRIBER_TO_CHANNEL,
                             reply_markup=Keyboards.subscriber_keyboard)

        raise CancelHandler()


def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsSubscriber)
