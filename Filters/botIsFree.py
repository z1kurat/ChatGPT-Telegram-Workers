from aiogram import types

from aiogram.dispatcher.filters import BoundFilter

from Configs.templateResponses import AWAIT_RESPONSE_MESSAGE

from DataBase import DB

import Keyboards


class IsBotFree(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id
        is_bot_work = await DB.get_work_state(user_id)

        if is_bot_work:
            await message.answer(AWAIT_RESPONSE_MESSAGE, reply_markup=Keyboards.remove_keyboard)
            return False

        await DB.set_work_state(user_id, True)

        return True
