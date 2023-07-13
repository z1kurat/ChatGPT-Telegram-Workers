from aiogram import types, Router, F, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.commands.commandName import IMAGE_COMMAND
from bot.data_base.models import Users
from bot.filters import ChatTypeFilter
from bot.keyboards.misc import cancel_keyboard
from bot.middlewares import RoleMiddleware, BalanceMiddleware
from bot.middlewares.subscriber_check_date import SubscriberCheckDateMiddleware
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.responses_template import START_RESPONSE, IMAGE_MESSAGE
from bot.structures.enum.image import OrderImageGenerate
from bot.utils.gpt import debiting_tokens
from bot.utils.gpt.get_image_response import get_image_response

user_gpt_image_router = Router()

user_gpt_image_router.message.middleware(RoleMiddleware())
user_gpt_image_router.message.middleware(SubscriberCheckDateMiddleware())
user_gpt_image_router.message.middleware(BalanceMiddleware())


@user_gpt_image_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(IMAGE_COMMAND),
    flags={"chat_action": "typing"})
async def cmd_start_image_generate(message: types.Message, state: FSMContext):
    """ Start processing GPT image queries """
    await message.answer(IMAGE_MESSAGE,
                         disable_notification=True,
                         reply_markup=cancel_keyboard)
    await state.set_state(OrderImageGenerate.image_generate)


@user_gpt_image_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    OrderImageGenerate.image_generate,
    F.text,
    flags={"chat_action": "upload_photo"})
async def cmd_image_generate(message: types.Message, user: Users, state: FSMContext, bot: Bot):
    """ Processing GPT image queries """
    opening_message = await message.answer(START_RESPONSE.format(user.balance),
                                           disable_notification=True,
                                           parse_mode=PARSE_MODE)

    success, response, token = await get_image_response(message.text)

    if success:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=response)
        await debiting_tokens(user, token)
        await state.clear()

    if not success:
        await bot.send_message(chat_id=message.from_user.id,
                               text=response)

    await opening_message.delete()

