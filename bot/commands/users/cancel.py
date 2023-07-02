from typing import Union

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from bot.commands.commandName import CANCEL_COMMAND
from bot.filters import ChatTypeFilter
from bot.parameters.responses_template import CANCEL_MESSAGE

user_cancel_router = Router()


@user_cancel_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(CANCEL_COMMAND),
    flags={"chat_action": "typing"})
@user_cancel_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(CANCEL_COMMAND),
    flags={"chat_action": "typing"})
async def cmd_cancel(event: Union[types.Message, types.CallbackQuery], state: FSMContext, bot: Bot):
    """ Cancel FSM """
    await bot.send_message(chat_id=event.from_user.id,
                           text=CANCEL_MESSAGE,
                           disable_notification=True)
    await state.clear()
