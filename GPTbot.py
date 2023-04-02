import openai

import Config

import telebot
import cherrypy


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                'content-type' in cherrypy.request.headers and \
                cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


user_history = {'id': 0, 'history': []}

openai.api_key = Config.OPENAI_KEY

bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def get_start(message):
    bot.send_message(message.chat.id, "Привет, я умнее тебя!")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print("-----Gotcha-----")
    message = message.text

    chat_id = message.chat.id

    print(f"User: {message.chat.first_name}")
    print(f"message: {message.text}")
    print(f"id: {chat_id}")

    user_history.setdefault(chat_id, [])

    messages = user_history[chat_id]
    messages.append(
        {"role": "system", "content": "You are a kind and helpful assistant who gives detailed and useful answers"})
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

        bot.reply_to(chat_id, completion.choices[0].message.content)
        print(f"send: {completion.choices[0].message.content}")

        user_history[chat_id].append({"role": "assistant", "content": completion.choices[0].message.content})

    except:
        bot.reply_to(chat_id, "Ты дурка? Я думаю, что да!")

    print("----------------\n")


bot.remove_webhook()

bot.set_webhook(url=Config.WEBHOOK_URL_BASE + Config.WEBHOOK_URL_PATH,
                certificate=open(Config.WEBHOOK_SSL_CERT, 'r'))

cherrypy.config.update({
    'server.socket_host': Config.WEBHOOK_LISTEN,
    'server.socket_port': Config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': Config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': Config.WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), Config.WEBHOOK_URL_PATH, {'/': {}})
