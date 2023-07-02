from typing import Union

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command, CommandObject, Text

from bot.data_base import Database
from bot.filters.chat_type_filter import ChatTypeFilter
from bot.commands.commandName import START_COMMAND
from bot.parameters.responses_template import START_MESSAGE
from bot.utils.referral import set_referral_by_user

user_start_router = Router()


async def cmd_start(message: types.Message, command: Union[CommandObject, None], db: Database, bot: Bot):
    """
       Registers the users if he has not been registered yet. It also outputs basic commands for the bot's operation.
       :param message: Current message
       :param command: Command
       :param db: Database
       :param bot: Telegram bot
       :return:
       """
    user = await db.users.get(message.from_user.id)
    if user is None:
        user = await db.users.new(user_id=message.from_user.id,
                                  user_name=message.from_user.username,
                                  first_name=message.from_user.first_name,
                                  second_name=message.from_user.last_name)
    if command is not None:
        referral_id_str = command.args
        if referral_id_str is not None:
            await set_referral_by_user(user, referral_id_str, message, db, bot)

    await bot.send_message(text=START_MESSAGE, chat_id=message.from_user.id)


@user_start_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(START_COMMAND),
    flags={"chat_action": "typing", "registrations": False})
async def cmd_start_message(message: types.Message, command: CommandObject, db: Database, bot: Bot):
    await cmd_start(message, command, db, bot)


@user_start_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(START_COMMAND),
    flags={"chat_action": "typing", "registrations": False})
async def cmd_start_callback_query(callback: types.callback_query, db: Database, bot: Bot):
    await cmd_start(callback, None, db, bot)
