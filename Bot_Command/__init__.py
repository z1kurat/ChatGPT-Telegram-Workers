import aiogram

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text

from Bot_Command import Start
from Bot_Command import Replay
from Bot_Command import Reset_Context
from Bot_Command import Сhannel_Post_Comment
from Bot_Command import GPT

from Bot_Command.Command_Name import START_COMMAND
from Bot_Command.Command_Name import REPLAY_COMMAND
from Bot_Command.Command_Name import COMMENT_COMMAND
from Bot_Command.Command_Name import RESET_COMMAND

from Filters.Chat_Subscriber import IsSubscriber


def register_handler(dp: aiogram.Dispatcher):
    dp.register_message_handler(Start.cmd_start, Command(START_COMMAND))
    dp.register_message_handler(Replay.cmd_replay_command, Command(REPLAY_COMMAND), IsSubscriber())
    dp.register_message_handler(Reset_Context.cmd_enable_context_command, Command(RESET_COMMAND), IsSubscriber())
    dp.register_message_handler(Сhannel_Post_Comment.cmd_comment_gpt, Command(COMMENT_COMMAND))

    dp.register_callback_query_handler(Replay.cmd_replay_query, Text(REPLAY_COMMAND))
    dp.register_callback_query_handler(Reset_Context.cmd_enable_context, Text(RESET_COMMAND))

    dp.register_message_handler(GPT.cmd_gpt, IsSubscriber())
