import openai

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters


def message_handler(bot: Bot, update: Update):
    print("-----Gotcha-----")
    message = update.effective_message

    chat_id = message.chat.id

    print(f"User: {message.chat.first_name}")
    print(f"message: {message.text}")
    print(f"id: {chat_id}")

    user_history.setdefault(chat_id, [])

    messages = user_history[chat_id]
    messages.append({"role": "system", "content": "You are a kind and helpful assistant who gives detailed and useful answers"})
    messages.append({"role": "user", "content": message.text})

    user_history[chat_id].append({"role": "user", "content": message.text})

    if len(user_history[chat_id]) >= 22:
        user_history[chat_id].pop(0)
        user_history[chat_id].pop(0)

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            n=1
        )

        bot.send_message(chat_id=update.effective_message.chat_id, text=completion.choices[0].message.content)
        print(f"send: {completion.choices[0].message.content}")

        user_history[chat_id].append({"role": "assistant", "content": completion.choices[0].message.content})

    except:
        bot.send_message(chat_id=update.effective_message.chat_id, text="Ты дурка? Я думаю, что да!")

    print("----------------\n")


def main():
    global user_history
    user_history = {'id': 0, 'history': []}

    openai.api_key = "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"

    bot = Bot(token='5853486557:AAHnqhu_7CqePUhU29S27AhrrHVZqiC0MBI')
    updater = Updater(bot=bot)

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
