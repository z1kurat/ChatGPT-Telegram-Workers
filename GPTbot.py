import Command

from aiogram.utils import executor

from SetupBot.Setup import dp

import Filters


if __name__ == "__main__":
    Filters.Chat_Subscriber.register_filters(dp)

    Command.Start.register_handlers(dp)
    Command.Сhannel_Post_Comment.register_handlers(dp)
    Command.Reset_Context.register_handlers(dp)
    Command.GPT.register_handlers(dp)

    executor.start_polling(dp)
