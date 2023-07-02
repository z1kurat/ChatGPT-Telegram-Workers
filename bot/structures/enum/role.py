import enum


class Role(enum.IntEnum):
    USER = 0
    PREMIUM = 1
    ADMINISTRATOR = 2


def get_name(role: Role) -> str:
    if role == Role.USER:
        return "Пользователь"

    if role == Role.PREMIUM:
        return "Премиум"

    if role == Role.ADMINISTRATOR:
        return "Администратор"
