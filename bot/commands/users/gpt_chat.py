from aiogram import types, Router, F
from aiogram.enums import ChatType

from bot.cache import Cache
from bot.data_base.models import Users
from bot.filters import ChatTypeFilter
from bot.middlewares import RoleMiddleware, BalanceMiddleware
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.responses_template import START_RESPONSE
from bot.utils.gpt import get_chat_response_from_user, debiting_tokens
from bot.keyboards.context import reset_context_keyboard, reset_and_replay_keyboard

user_gpt_chat_router = Router()

user_gpt_chat_router.message.middleware(RoleMiddleware())
user_gpt_chat_router.message.middleware(BalanceMiddleware())


@user_gpt_chat_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    F.text,
    flags={"chat_action": "typing"})
async def cmd_gpt(message: types.Message, user: Users, cache: Cache):
    """ Processing GPT text queries """
    opening_message = await message.answer(START_RESPONSE.format(user.balance),
                                           disable_notification=True,
                                           parse_mode=PARSE_MODE)

    success, response, token = await get_chat_response_from_user(user_id=message.from_user.id,
                                                                 message=message.text,
                                                                 cache=cache)

    keyboard = reset_and_replay_keyboard

    if success:
        await debiting_tokens(user, token)
        keyboard = reset_context_keyboard

    await opening_message.delete()
    await message.answer(response, reply_markup=keyboard)
