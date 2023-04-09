import asyncio

import Command

from aiogram.utils import executor

from SetupBot.Setup import dp


async def main():
    Command.Start.register_handlers(dp)
    Command.Reset_Context.register_handlers(dp)
    Command.GPT.register_handlers(dp)

    await executor.start_polling(dp)


if __name__ == "__main__":
    asyncio.run(main())
