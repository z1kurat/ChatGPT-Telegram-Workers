import Command

from aiogram.utils import executor

from SetupBot.Setup import dp


if __name__ == "__main__":
    Command.Start.register_handlers(dp)
    Command.Reset_Context.register_handlers(dp)
    Command.GPT.register_handlers(dp)

    executor.start_polling(dp)
