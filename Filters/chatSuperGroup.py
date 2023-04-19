from aiogram import types

from aiogram.dispatcher.filters import BoundFilter


class IsChatSuperGroup(BoundFilter):
    async def check(self, message: types.Message):
        if message.chat.type == 'supergroup':
            return True
        return False

