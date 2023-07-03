from bot.parameters.responses_template import TOO_FAST_RESPONSE_MESSAGE, ERROR_RESPONSE_MESSAGE
from bot.structures.erorrs import TooManyRequests, SomethingWentWrong
from bot.utils.gpt.imageComplete import image_complete


async def get_image_response(prompt: str) -> [bool, str, int]:
    """ Processing GPT text queries """
    try:
        response, token = await image_complete(prompt)
    except TooManyRequests:
        return False, TOO_FAST_RESPONSE_MESSAGE, None
    except SomethingWentWrong:
        return False, ERROR_RESPONSE_MESSAGE, None

    return True, response, token
