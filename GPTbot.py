import Command

import Filters

from aiogram.utils import executor

from SetupBot.Setup import dp


if __name__ == "__main__":
    executor.start_polling(dp)
