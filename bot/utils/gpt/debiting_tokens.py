from bot.data_base.models import Users
from bot.structures import Role


async def debiting_tokens(user: Users, token: int):
    if user.role == Role.USER:
        user.balance = max(0, user.balance - token)
