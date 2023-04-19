from DataBase import DB

from SetupBot.Setup import logger_error
from SetupBot.Setup import logger_history


async def save_message_history(user_id, message_text, response) -> bool:
    try:
        # !toDO: add check for messages
        await DB.save_message_history(user_id, "user", message_text)
        await DB.save_message_history(user_id, "assistant", response)
        return True
    except Exception as error:
        logger_history.info(f"error form save dialog: {error}")
        logger_error.error(f"error form save dialog: {user_id} : {error}")
        return False


async def save_last_message(user_id, last_message):
    try:
        # !toDO: add check for messages
        await DB.update_last_message(user_id, last_message)
        return True
    except Exception as error:
        logger_history.info(f"error form save last message: {error}")
        logger_error.error(f"error form save last message: {user_id} : {error}")
        return False
