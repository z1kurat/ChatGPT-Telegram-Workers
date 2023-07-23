from aiogram import types, Router, F, Bot
from aiogram.enums import ChatType
from aiogram.types import InputFile, FSInputFile

from bot.cache import Cache
from bot.data_base.models import Users
from bot.filters import ChatTypeFilter
from bot.middlewares import RoleMiddleware, BalanceMiddleware
from bot.middlewares.subscriber_check_date import SubscriberCheckDateMiddleware
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.gpt_parameters import DEFAULT_PROMPT
from bot.parameters.responses_template import START_RESPONSE
from bot.utils.gpt import get_chat_response, debiting_tokens
from bot.keyboards.context import reset_context_keyboard, reset_and_replay_keyboard
from bot.utils.document.reading import Reader
from bot.utils.document.document import Document
from bot.utils.document.params import INPUT_FILE_PATH, OUTPUT_FILE_PATH

user_doc_response_router = Router()

user_doc_response_router.message.middleware(RoleMiddleware())
user_doc_response_router.message.middleware(SubscriberCheckDateMiddleware())
user_doc_response_router.message.middleware(BalanceMiddleware())


@user_doc_response_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    F.document,
    flags={"chat_action": "typing"})
async def cmd_gpt(message: types.Message, user: Users, bot: Bot):
    """ Processing GPT text queries """
    opening_message = await message.answer(START_RESPONSE.format(user.balance),
                                           disable_notification=True,
                                           parse_mode=PARSE_MODE)

    keyboard = reset_and_replay_keyboard

    # print(f'User {message.chat.id} started downloading file...')
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, INPUT_FILE_PATH.format(message.chat.id))
    # print("File was downloaded...")

    getting_file = Reader(INPUT_FILE_PATH.format(message.chat.id))
    data = getting_file.data
    document = Document()

    message_start = await message.answer(START_RESPONSE.format(getting_file.time_waiting))

    for question in data:
        user_history = [{"role": "system", "content": DEFAULT_PROMPT},
                        {"role": "user", "content": question}]
        success, response, token = await get_chat_response(user_dialog=user_history)
        if success:
            document.filling(question=question, answer=response)
            user.balance -= token
            # break

    document.saving(message.chat.id)
    try:
        await bot.send_document(chat_id=message.chat.id,
                                document=FSInputFile(OUTPUT_FILE_PATH.format(message.chat.id)),
                                caption='ne lox')
    except Exception as e:
        pass

    await message_start.delete()

    if success:
        await debiting_tokens(user, token)
        keyboard = reset_context_keyboard

    await opening_message.delete()
