from typing import Union

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command, Text

from bot.keyboards.context import reset_context_keyboard, reset_and_replay_keyboard
from bot.cache import Cache
from bot.data_base.models import Users
from bot.filters import ChatTypeFilter
from bot.commands.commandName import REPLAY_COMMAND
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.responses_template import MESSAGE_RESET_CONTEXT, NONE_LAST_MESSAGE, START_RESPONSE
from bot.commands.commandName import RESET_COMMAND
from bot.utils.gpt.get_chat_response import get_chat_response_from_user

user_context_router = Router()


@user_context_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(REPLAY_COMMAND),
    flags={"chat_action": "typing"})
@user_context_router.callback_query(Text(REPLAY_COMMAND))
async def replay(message: Union[types.Message, types.CallbackQuery], bot: Bot, user: Users, cache: Cache):
    radis_key = f"last_message_{message.from_user.id}"
    binary_last_message = await cache.misc_client.get(radis_key)

    if not binary_last_message:
        await bot.send_message(chat_id=message.from_user.id,
                               text=NONE_LAST_MESSAGE,
                               disable_notification=True)
        return

    opening_message = await bot.send_message(chat_id=message.from_user.id,
                                             text=START_RESPONSE.format(user.balance),
                                             disable_notification=True,
                                             parse_mode=PARSE_MODE)

    last_message = binary_last_message.decode()
    success, response, token = await get_chat_response_from_user(user_id=message.from_user.id,
                                                                 message=last_message,
                                                                 cache=cache)
    keyboard = reset_and_replay_keyboard

    if success:
        user.balance -= token
        keyboard = reset_context_keyboard

    await opening_message.delete()
    await bot.send_message(chat_id=message.from_user.id,
                           text=response,
                           reply_markup=keyboard)


@user_context_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(RESET_COMMAND),
    flags={"chat_action": "typing"})
@user_context_router.callback_query(Text(RESET_COMMAND))
async def reset_conntext(event: [types.Message, types.CallbackQuery], bot: Bot, cache: Cache):
    await cache.user_client.delete(event.from_user.id)
    await cache.misc_client.delete(f"last_message_{event.from_user.id}")
    await bot.send_message(chat_id=event.from_user.id,
                           text=MESSAGE_RESET_CONTEXT,
                           disable_notification=True)
