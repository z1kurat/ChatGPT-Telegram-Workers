from SetupBot.Setup import dp

import Bot_Command

from aiogram.utils import executor


if __name__ == "__main__":
    Bot_Command.register_handler(dp)
    executor.start_polling(dp)
