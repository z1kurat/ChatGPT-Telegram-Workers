from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from bot.commands.commandName import START_COMMAND, RESET_COMMAND, REPLAY_COMMAND, CANCEL_COMMAND, PROFILE_COMMAND, \
    IMAGE_COMMAND


async def set_bot_commands(bot: Bot):
    data = [
        (
            [
                BotCommand(command=START_COMMAND, description="Регистрация"),
                BotCommand(command=RESET_COMMAND, description="Завершить диалог"),
                BotCommand(command=REPLAY_COMMAND, description="Повторитить последений запрос"),
                BotCommand(command=IMAGE_COMMAND, description="Создание изображений"),
                BotCommand(command=PROFILE_COMMAND, description="Профиль"),
                BotCommand(command=CANCEL_COMMAND, description="Отменить все команды")
            ],
            BotCommandScopeAllPrivateChats(),
            None
        )
    ]

    for commands_list, commands_scope, language in data:
        await bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)
