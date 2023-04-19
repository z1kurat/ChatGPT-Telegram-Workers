import aiogram

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text

from Bot_Command import start
from Bot_Command import replay
from Bot_Command import resetContext
from Bot_Command import сhannelPostComment
from Bot_Command import GPT

from Bot_Command.commandName import START_COMMAND
from Bot_Command.commandName import REPLAY_COMMAND
from Bot_Command.commandName import COMMENT_COMMAND
from Bot_Command.commandName import RESET_COMMAND

from Filters.chatSubscriber import IsSubscriber
from Filters.botIsFree import IsBotFree
from Filters.chatPrivate import IsChatPrivate
from Filters.chatSuperGroup import IsChatSuperGroup


def register_handler(dp: aiogram.Dispatcher):
    dp.register_message_handler(start.cmd_start, IsBotFree(), Command(START_COMMAND), IsChatPrivate())
    dp.register_message_handler(replay.replay_cmd, IsBotFree(), Command(REPLAY_COMMAND), IsChatPrivate(), IsSubscriber())
    dp.register_message_handler(resetContext.reset_context_cmd, IsBotFree(), Command(RESET_COMMAND), IsChatPrivate(), IsSubscriber())
    dp.register_message_handler(сhannelPostComment.comment_gpt_cmd, Command(COMMENT_COMMAND), IsChatSuperGroup())

    dp.register_callback_query_handler(replay.replay_callback, IsBotFree(), Text(REPLAY_COMMAND), IsChatPrivate(), IsSubscriber())
    dp.register_callback_query_handler(resetContext.reset_context_callback, IsBotFree(), Text(RESET_COMMAND), IsChatPrivate(), IsSubscriber())

    dp.register_message_handler(GPT.cmd_gpt, IsBotFree(), IsChatPrivate(), IsSubscriber())
