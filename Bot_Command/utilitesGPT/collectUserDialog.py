from typing import Tuple

from Configs.parametersGPT import DEFAULT_MOD

from DataBase import DB


async def get_user_dialog(user_id, message_text) -> Tuple[bool, list[dict[str, str]]]:
    # !toDO: add system prompt
    is_dialog_correct = True
    current_dialog = [{"role": "system", "content": DEFAULT_MOD}]

    user_messages_history = await DB.read_message_history(user_id)

    if is_user_messages_history_correct(user_messages_history):
        current_dialog.extend(user_messages_history)
    else:
        is_dialog_correct = False

    current_dialog.append({"role": "user", "content": message_text})

    return is_dialog_correct, current_dialog


async def is_user_messages_history_correct(user_messages_history: list[dict[str, str]]) -> bool:
    if user_messages_history is None or len(user_messages_history) == 0:
        return False
    # !toDO: add enum for role
    for message_index in range(0, len(user_messages_history)):
        if message_index % 2 == 0:
            if user_messages_history[message_index]["role"] != 'user':
                return False
        else:
            if user_messages_history[message_index]["role"] != 'assistant':
                return False

    return True

