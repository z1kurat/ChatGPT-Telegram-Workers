from Configs.parametersGPT import MODEL
from Configs.parametersGPT import TEMPERATURE
from Configs.parametersGPT import MAX_VALUE_COUNT
from Configs.parametersGPT import TIME_OUT
from Configs.parametersGPT import STOP

from Configs.API import OPENAI_KEY

import openai_async

from SetupBot.Setup import logger_history
from SetupBot.Setup import logger_error


async def get_response_gpt(user_dialog):
    try:
        completion = await openai_async.chat_complete(
            OPENAI_KEY,
            timeout=TIME_OUT,
            payload={
                "model": MODEL,
                "messages": user_dialog,
                "temperature": TEMPERATURE,
                "stop": STOP,
                "n": MAX_VALUE_COUNT
            }
        )

        return completion.json()["choices"][0]["message"]["content"]

    except Exception as err:
        logger_error.error(f"{err.args} : {user_dialog[-1]}")
        logger_history.info(f"{err.args} : {user_dialog[-1]}")
        return None
