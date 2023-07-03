import os

from httpx import ReadTimeout
from openai_async import openai_async

from bot.parameters.gpt_parameters import MAX_VALUE_COUNT, TIME_OUT, IMAGE_SIZE, IMAGE_TOKEN_COUNT
from bot.structures.erorrs import TooManyRequests, SomethingWentWrong


async def image_complete(prompt: str) -> [str, int]:
    """
    Getting a response from GPT
    :param prompt: users template
    :return: response and token
    """
    try:
        completion = await openai_async.generate_img(
            os.getenv("OPENAI_KEY"),
            timeout=TIME_OUT,
            payload={
                "prompt": prompt,
                "n": MAX_VALUE_COUNT,
                "size": IMAGE_SIZE
            }
        )

        response = completion.json()["data"][0]["url"]

        return response, IMAGE_TOKEN_COUNT

    except Exception as err:
        if completion.status_code == 429:
            raise TooManyRequests(err)

        if isinstance(err, ReadTimeout):
            raise

        raise SomethingWentWrong(err)
