from .users import user_router
from .groups import group_router
from .admins import admin_router
from .channels import channel_router

routers = (user_router, channel_router, group_router, admin_router)
