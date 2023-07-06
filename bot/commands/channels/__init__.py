from aiogram import Router

from bot.middlewares import ThrottlingMiddleware, UserMiddleware, DatabaseMiddleware, RoleMiddleware

from .post_comment import comment_router
from ...middlewares.administrators import AdministratorsMiddleware
from ...middlewares.registrations import RegistrationsMiddleware

channel_router = Router(name='Channel')

channel_router.message.middleware(RegistrationsMiddleware())
channel_router.message.middleware(DatabaseMiddleware())
channel_router.message.middleware(UserMiddleware())
channel_router.message.middleware(RoleMiddleware())
channel_router.message.middleware(AdministratorsMiddleware())

channel_router.include_routers(comment_router)

