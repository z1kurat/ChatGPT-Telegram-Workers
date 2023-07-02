from aiogram import Router

from bot.middlewares import ThrottlingMiddleware

group_router = Router(name='Group')

group_router.message.outer_middleware(ThrottlingMiddleware())
