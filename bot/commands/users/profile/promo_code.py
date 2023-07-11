from aiogram import types, Router, Bot, F
from aiogram.enums import ChatType
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from bot.commands.commandName import PROMO_CODE_COMMAND
from bot.data_base.models import Users
from bot.data_base.repositories import PromoCodeRepo, UsedPromoCodeRepo
from bot.filters import ChatTypeFilter
from bot.keyboards.navigations.promo_code import promo_code_back_menu_keyboard
from bot.middlewares.promo_code import PromoCodeMiddleware
from bot.middlewares.used_promo_code import UsedPromoCodeMiddleware
from bot.parameters.responses_template import PROMO_CODE_START_MESSAGE
from bot.structures.enum.promo_code import OrderPromoCode, PromoCodeStatus
from bot.utils.promo_code.promo_code import check_users_promo_code, get_message_by_promo_code_status, \
    update_used_promo_code

user_promo_code_router = Router()

user_promo_code_router.message.middleware(PromoCodeMiddleware())
user_promo_code_router.message.middleware(UsedPromoCodeMiddleware())


@user_promo_code_router.callback_query(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    Text(PROMO_CODE_COMMAND),
    flags={"chat_action": "typing"})
async def cmd_start_promo_code(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    """ Start set users promo code """
    await state.set_state(OrderPromoCode.promo_code_registrations)
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=callback.message.message_id,
                                text=PROMO_CODE_START_MESSAGE,
                                reply_markup=promo_code_back_menu_keyboard)


@user_promo_code_router.message(
    ChatTypeFilter(chat_type=[ChatType.PRIVATE]),
    F.text,
    OrderPromoCode.promo_code_registrations,
    flags={"chat_action": "typing"})
async def cmd_promo_code(
        message: types.Message,
        bot: Bot,
        promo_codes: PromoCodeRepo,
        used_promo_codes: UsedPromoCodeRepo,
        user: Users,
        state: FSMContext
):
    """ Use users promo code """
    promo_code = message.text
    user_id = message.from_user.id
    keyboard = promo_code_back_menu_keyboard

    status, token = await check_users_promo_code(promo_code, user_id, promo_codes, used_promo_codes)

    if status == PromoCodeStatus.ACTIVE:
        await update_used_promo_code(promo_code, user_id, used_promo_codes)
        await state.clear()

        user.balance += token

        keyboard = None

    result_message = await get_message_by_promo_code_status(status)

    await bot.send_message(chat_id=message.from_user.id,
                           text=result_message.format(token),
                           reply_markup=keyboard)
