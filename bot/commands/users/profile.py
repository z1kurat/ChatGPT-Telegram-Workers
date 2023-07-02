from typing import Union

from aiogram import types, Router, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command, Text

from bot.data_base.models import Users
from bot.filters.chat_type_filter import ChatTypeFilter
from bot.commands.commandName import PROFILE_COMMAND, REFERRAL_MENU, BACK_TO_MENU, PROMO_CODE_MENU, TOKEN_MENU,\
                                     SUBSCRIPTION_MENU, SETTINGS_MENU, HELP_MENU
from bot.middlewares.fsm_state import FSMStateMiddleware
from bot.parameters.responses_template import PROFILE, CHOSE_ACTIONS, TOKEN_ABOUT
from bot.keyboards.navigations import menu_keyboard
from bot.keyboards.navigations.referral import referral_keyboard
from bot.keyboards.navigations.promo_code import promo_code_keyboard
from bot.keyboards.navigations.help import help_keyboard
from bot.keyboards.navigations.settings import settings_keyboard
from bot.keyboards.navigations.subscription import subscription_keyboard
from bot.keyboards.navigations.token import token_keyboard
from bot.structures.enum import get_name

user_profile_router = Router()

user_profile_router.message.middleware(FSMStateMiddleware())
user_profile_router.callback_query.middleware(FSMStateMiddleware())


@user_profile_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Command(PROFILE_COMMAND),
    flags={"chat_action": "typing"})
@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(PROFILE_COMMAND),
    flags={"chat_action": "typing"})
async def cmd_profile_send(event: Union[types.Message, types.CallbackQuery], user: Users, bot: Bot):
    await bot.send_message(chat_id=event.from_user.id,
                           text=PROFILE.format(user.user_name, get_name(user.role), user.balance),
                           reply_markup=menu_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(REFERRAL_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_referral(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=CHOSE_ACTIONS,
                                reply_markup=referral_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(PROMO_CODE_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_promo_code(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=CHOSE_ACTIONS,
                                reply_markup=promo_code_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(TOKEN_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_token(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=TOKEN_ABOUT,
                                reply_markup=token_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(SUBSCRIPTION_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_subscription(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=CHOSE_ACTIONS,
                                reply_markup=subscription_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(SETTINGS_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_settings(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=CHOSE_ACTIONS,
                                reply_markup=settings_keyboard)


@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(HELP_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_help(callback: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=CHOSE_ACTIONS,
                                reply_markup=help_keyboard)

@user_profile_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(BACK_TO_MENU),
    flags={"chat_action": "typing"})
async def cmd_profile_edit(callback: types.CallbackQuery, bot: Bot, user: Users):
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=PROFILE.format(user.user_name, get_name(user.role), user.balance),
                                reply_markup=menu_keyboard)
