import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from document import Document
from reading import Reader
from gpt import GPT

from params import TG_TOKEN, INPUT_FILE_PATH, OUTPUT_FILE_PATH
from main import Main

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(commands=['document'])
async def process_get_document(message: types.Document):
    await Main().main()
    with open("Answers_GPT-3.5-turbo.docx", 'rb') as file:
        await message.reply_document(file)
        print(f'User {message.chat.id} got file...')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def scan_message(message: types.Message):
    print(f'User {message.chat.id} started downloading file...')
    destination_file = await message.document.download(destination_file = INPUT_FILE_PATH.format(message.chat.id))
    print("File was downloaded...")

    getting_file = Reader(r"INPUT_DOCS\input_file.txt")
    data = getting_file.data
    document = Document()

    message_start = await message.answer(f"Файл получен, пожалуйста, ожидайте...\nПримерное время ожидания: {getting_file.time_waiting} минут...")

    for question in data:
        document.filling(question=question, answer=(await GPT().chat_complete(question)))
        # break

    document.saving(message.chat.id)

    # await message.reply(f"Файл получен, примерное время ожидения: {main_process.time_waiting} минут...")
    with open(OUTPUT_FILE_PATH.format(message.chat.id), 'rb') as file:
        await message.reply_document(file)
        print(f'User {message.chat.id} got file...')
        await message_start.delete()


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)