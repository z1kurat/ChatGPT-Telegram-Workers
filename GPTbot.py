import asyncio

import Command

from SetupBot.Setup import dp
from SetupBot.Setup import bot


async def main():
    Command.Start.register_handlers(dp)
    Command.Reset_Context.register_handlers(dp)
    Command.GPT.register_handlers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete((main()))
