from SetupBot.Setup import dp

import Bot_Command

from aiogram.utils import executor


if __name__ == "__main__":
    executor.start_polling(dp)
