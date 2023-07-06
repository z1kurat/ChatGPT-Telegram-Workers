from aiogram import types, Router
from aiogram.enums import ChatType
from aiogram.filters import CommandObject, Command

from aiogram import html

from bot.filters.chat_type_filter import ChatTypeFilter

from bot.commands.commandName import COMMENT_COMMAND
from bot.middlewares.end_of_requests import EndOfRequestsMiddleware

from bot.parameters.gpt_parameters import DEFAULT_POST_MOD
from bot.parameters.responses_template import ERROR_RESPONSE_MESSAGE, EMPTY_ARGUMENTS_COMMAND, TOO_FAST_RESPONSE_MESSAGE
from bot.structures.erorrs import TooManyRequests, SomethingWentWrong

from bot.utils.gpt import chatComplete

comment_router = Router(name='Channel')
comment_router.message.middleware(EndOfRequestsMiddleware())


@comment_router.message(
    ChatTypeFilter(chat_type=[ChatType.CHANNEL]),
    Command(COMMENT_COMMAND))
async def comment_gpt(message: types.Message, command: CommandObject):
    arguments = html.quote(command.args)
    message_id = message.reply_to_message.message_id

    if not arguments:
        await message.answer(EMPTY_ARGUMENTS_COMMAND,
                             reply_to_message_id=message_id,
                             disable_notification=True)
        return

    user_messages = [{"role": "system", "content": DEFAULT_POST_MOD},
                     {"role": "users", "content": arguments}]

    try:
        response = await chatComplete.chat_complete(user_messages)
    except TooManyRequests:
        response = TOO_FAST_RESPONSE_MESSAGE
    except SomethingWentWrong:
        response = ERROR_RESPONSE_MESSAGE

    await message.delete()
    await message.answer(response, reply_to_message_id=message_id, disable_notification=True)
