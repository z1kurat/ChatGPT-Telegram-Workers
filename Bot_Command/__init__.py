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
    dp.register_message_handler(Start.cmd_start, filters=[Command(START_COMMAND), IsSubscriber()])
    dp.register_message_handler(Replay.cmd_replay_command, filters=(Command(REPLAY_COMMAND), IsSubscriber()))
    dp.register_message_handler(Reset_Context.cmd_enable_context_command, filters=(Command(RESET_COMMAND), IsSubscriber()))
    dp.register_message_handler(Сhannel_Post_Comment.cmd_comment_gpt, filters=(Command(COMMENT_COMMAND), IsSubscriber()))

    dp.register_callback_query_handler(Replay.cmd_replay_query, filters=(Text(REPLAY_COMMAND)))
    dp.register_callback_query_handler(Reset_Context.cmd_enable_context, filters=(Text(RESET_COMMAND)))

    dp.register_message_handler(GPT.cmd_gpt, filters=(IsSubscriber()))
