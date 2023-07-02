from aiogram import Router

from bot.middlewares import ThrottlingMiddleware

channel_router = Router(name='Channel')

channel_router.message.outer_middleware(ThrottlingMiddleware())

