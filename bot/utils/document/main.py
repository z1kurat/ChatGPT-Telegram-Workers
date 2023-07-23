import asyncio

from document import Document
from reading import Reader
from gpt import GPT

class Main():
    async def main(self, chat_id):
        getting_file = Reader(r"INPUT_DOCS\input_file.txt")
        data = getting_file.data
        self.time_waiting = getting_file.time_waiting
        document = Document()

        for question in data:
            document.filling(question=question, answer=(await GPT().chat_complete(question)))
            # break

        document.saving(chat_id)


# if __name__ == '__main__':
#     asyncio.run(main())

