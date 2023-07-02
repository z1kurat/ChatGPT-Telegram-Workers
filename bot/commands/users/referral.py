from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from bot.commands.commandName import REFERRAL_CODE_COMMAND, REFERRAL_CODE_LINK, REFERRAL_ADD
from bot.data_base import Database
from bot.data_base.models import Users
from bot.filters import ChatTypeFilter
from bot.keyboards.navigations.referral import referral_back_menu_keyboard
from bot.parameters.bot_parameters import PARSE_MODE
from bot.parameters.responses_template import REFERRAL_GET_CODE, REFERRAL_GET_LINK, REFERRAL_START_ADD_BY_CODE, \
    REFERRAL_LINK_TEMPLATE
from bot.structures.enum.referral import OrderReferralRegistrations
from bot.utils.referral import set_referral_by_user
from bot.keyboards.navigations import referral_keyboard

user_referral_router = Router()


@user_referral_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(REFERRAL_CODE_COMMAND),
    flags={"chat_action": "typing"})
async def cmd_referral_code(callback: types.CallbackQuery, bot: Bot):
    """ Get a referral registration code """
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=REFERRAL_GET_CODE + markdown.code(callback.from_user.id),
                                parse_mode=PARSE_MODE,
                                reply_markup=referral_keyboard)


@user_referral_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(REFERRAL_CODE_LINK),
    flags={"chat_action": "typing"})
async def cmd_referral_code(callback: types.CallbackQuery, bot: Bot):
    """ Get a referral registration link """
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=REFERRAL_GET_LINK + markdown.code(
                                    REFERRAL_LINK_TEMPLATE.format(callback.from_user.id)),
                                parse_mode=PARSE_MODE,
                                reply_markup=referral_keyboard)


@user_referral_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(REFERRAL_ADD),
    flags={"chat_action": "typing"})
async def cmd_referral_starting_add_by_code(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    """ Start adding a referral by users code """
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=REFERRAL_START_ADD_BY_CODE,
                                parse_mode=PARSE_MODE,
                                reply_markup=referral_back_menu_keyboard)
    await state.set_state(OrderReferralRegistrations.referral_registrations)


@user_referral_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    OrderReferralRegistrations.referral_registrations,
    flags={"chat_action": "typing"})
async def cmd_referral_add_by_code(message: types.Message, user: Users, db: Database, bot: Bot, state: FSMContext):
    """ Add a referral by users code """
    # Нельзя туда передавать message, bot - это другой уровень абстракции. Семён, пожалуйста, спасай!
    # db - тоже не хорошо, но терпимо...
    added_referral = await set_referral_by_user(user, message.text, message, db, bot)

    if not added_referral:
        await bot.send_message(chat_id=message.from_user.id,
                               text=REFERRAL_START_ADD_BY_CODE,
                               parse_mode=PARSE_MODE,
                               reply_markup=referral_back_menu_keyboard)
        return

    await state.set_state(OrderReferralRegistrations.referral_registrations)
