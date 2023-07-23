from openai_async import openai_async
from params import DEFAULT_PROMPT, MODEL, TEMPERATURE, STOP, N_AMOUNT, API_KEY, TIMEOUT

class GPT():
    async def chat_complete(self, single_question) -> str:
        completion = await openai_async.chat_complete(
        API_KEY,
        timeout=TIMEOUT,
        payload={
            "model": MODEL,
            "messages":  [{"role": "system", "content": DEFAULT_PROMPT},
                        {"role": "user", "content": single_question}],
            "temperature": TEMPERATURE,
            "stop": STOP,
            "n": N_AMOUNT
        }
        )

        response = completion.json()["choices"][0]["message"]["content"]
        return response