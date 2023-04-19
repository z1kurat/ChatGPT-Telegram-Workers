from aiogram import types

from utilitesGPT import run


async def cmd_gpt(message: types.Message):
    await run.gpt(message)


