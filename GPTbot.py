from SetupBot.Setup import dp

from aiogram.utils import executor

import Command

import Filters


if __name__ == "__main__":
    Filters.Chat_Subscriber.register_filters(dp)

    executor.start_polling(dp)
