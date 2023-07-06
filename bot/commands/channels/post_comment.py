from aiogram import types, Router
from aiogram.enums import ChatType
from aiogram.filters import CommandObject, Command
from aiogram import html

from bot.data_base.models import Users
from bot.filters.chat_type_filter import ChatTypeFilter
from bot.commands.commandName import COMMENT_COMMAND
from bot.parameters.gpt_parameters import DEFAULT_POST_MOD
from bot.parameters.responses_template import EMPTY_ARGUMENTS_COMMAND
from bot.utils.gpt import get_chat_response, debiting_tokens

comment_router = Router(name='Channel')


@comment_router.message(
    ChatTypeFilter(chat_type=[ChatType.SUPERGROUP]),
    Command(COMMENT_COMMAND))
async def comment_gpt(message: types.Message, user: Users, command: CommandObject):
    arguments = html.quote(command.args)
    message_id = message.reply_to_message.message_id

    if not arguments:
        await message.answer(EMPTY_ARGUMENTS_COMMAND,
                             reply_to_message_id=message_id,
                             disable_notification=True)
        return

    user_messages = [{"role": "system", "content": DEFAULT_POST_MOD},
                     {"role": "user", "content": arguments}]

    success, response, token = await get_chat_response(user_messages)

    if success:
        await debiting_tokens(user, token)

    await message.delete()
    await message.answer(response, reply_to_message_id=message_id, disable_notification=True)
