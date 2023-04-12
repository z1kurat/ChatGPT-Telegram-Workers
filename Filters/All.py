from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter


class ForAll(BoundFilter):
    async def check(self, message: types.Message):
        return True


def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(ForAll)
