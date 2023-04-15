from SetupBot.Setup import dp

from aiogram.utils import executor

import Command

if __name__ == "__main__":
    executor.start_polling(dp)
