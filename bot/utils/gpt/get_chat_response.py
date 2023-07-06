import json

import typing

from bot.cache import Cache
from bot.parameters.gpt_parameters import MAX_SAVE_MESSAGE_HISTORY, DEFAULT_PROMPT
from bot.parameters.responses_template import TOO_FAST_RESPONSE_MESSAGE, ERROR_RESPONSE_MESSAGE
from bot.structures.erorrs import TooManyRequests, SomethingWentWrong
from bot.utils.gpt import chat_complete


async def get_chat_response_from_user(user_id: int, message: str, cache: Cache) -> [bool, str, int]:
    """ Processing GPT text queries from user """
    radis_key = f"last_message_{user_id}"
    await cache.misc_client.set(radis_key, message)

    user_dialog = await get_user_messages(message, user_id, cache)
    success, response, token = await get_chat_response(user_dialog)

    if not success:
        return success, response, token

    user_dialog.append({"role": "assistant", "content": response})
    await cache.user_client.set(user_id, json.dumps(user_dialog))

    return success, response, token


async def get_chat_response(user_dialog: [typing.Dict[str, str]]) -> [bool, str, int]:
    """ Processing GPT text queries """
    try:
        response, token = await chat_complete(user_dialog)
    except TooManyRequests:
        return False, TOO_FAST_RESPONSE_MESSAGE, None
    except SomethingWentWrong:
        return False, ERROR_RESPONSE_MESSAGE, None

    return True, response, token


async def get_user_messages(message: str, user_id: int, cache: Cache) -> [typing.Dict[str, str]]:
    """ Collect or create users message history """
    user_history_binary = await cache.user_client.get(user_id)
    if user_history_binary:
        user_history: [typing.Dict[str, str]] = json.loads(user_history_binary.decode())

        if len(user_history) == MAX_SAVE_MESSAGE_HISTORY:
            del user_history[1:3]

        user_history.append({"role": "user", "content": message})
        return user_history

    user_history = [{"role": "system", "content": DEFAULT_PROMPT},
                    {"role": "user", "content": message}]

    return user_history
