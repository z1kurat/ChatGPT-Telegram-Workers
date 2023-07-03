from aiogram.utils import markdown

MESSAGE_RESET_CONTEXT = r'✅Запущен новый диалог'
MESSAGE_TO_RESET_CONTEXT = r'🧹Завершить диалог...'
MESSAGE_TO_REPLAY = r'🔁Повторить попытку...'

ERROR_RESPONSE_MESSAGE = r'😢В данный момент невозможно обработать Ваш запрос, повторите попытку позже...'
TOO_FAST_RESPONSE_MESSAGE = "Нам нужно больше скорости🏎️💨\nПодождите 10 секунд и повторите запрос..."
AWAIT_RESPONSE_MESSAGE = r'😬Дождитесь загрузки предыдущего запроса.'
NONE_LAST_MESSAGE = r'❌Отсутсвует сообщение для повторной отправки.'

REGISTRATIONS_MESSAGE = "😢Нет, нет, нет, Вы незарегистрированы...\n⬇Но это можно легко исправить"
REGISTRATIONS = r'➡Зарегистрироваться'

NOT_ENOUGH_FUNDS = r'💸Не достаточно средств для выполения запроса. Вы можете запросить пару золотых монет или пополнить баланс иными способами...'

START_MESSAGE = "😎Приветствую! Я бот ChatGPT и готов отвечать на Ваши вопросы. Вот лишь небольшая часть того, с чем я могу помочь:\n" \
                "\n" \
                "- Поиск информации по любой теме;\n" \
                "- Подсказки и советы по решению задач из любой области;\n" \
                "- Помощь в написании текстов, рефератов, докладов на различные темы;\n" \
                "- Изучение иностранных языков (Перевод текстов с сохранением контекста, объяснение тем по грамматике и не только)\n" \
                "\n" \
                "🚀Не стесняйтесь обращаться ко мне в любое время🚀"

START_RESPONSE = markdown.bold("⌛Подготовка ответа...\n") + markdown.italic("Текущий баланс: {}")

SUBSCRIBER_TO_CHANNEL = "🤓Для работы бота необходимо подписаться на Telegram канал..."
SUBSCRIBE = "🔔Подписаться... "
URL_TO_SUBSCRIBE = "https://t.me/HomeDigestIT"

THROTTLED_MESSAGE = "🌈Вы начали бездумно бить по клавиатуре? Все будет хорошо, пожалуйста, успокойтесь и подождите {} секунду..."

EMPTY_ARGUMENTS_COMMAND = "🤖И что мне тут комментировать? Подумайте еще над своим сообщением..."

REFERRAL_OF_YOURSELF = "🤓Задумка интересная, но баллы за это мы Вам не дадим..."
REFERRAL_BAD_CODE = "🤔Не понял, это что такое? Введен неверный код..."
REFERRAL_SUCCESS = "👍Вы успешно зарегистировались, как реферал {}. Поздравляю, Вам начислено {} токенов..."
YOUR_REFERRAL_SUCCESS = "👍По Вашей ссылке успешно зарегистировался новый реферал - {}. Поздравляю, Вам начислено {} " \
                        "токенов... "
REFERRAL_NOT_EXIST = "🤔Такого пользователя не существует на просторах нашего уютного сообщества..."
REFERRAL_EXIST = "🙉Вы уже зарегистрированы в качестве реферала {}, так что никаких бонусных токенов..."
REFERRAL_UNAVAILABLE = "🤖К сожеланию, {} давно к нам не заходил. Если можете, то напомните ему о нас..."
REFERRAL_GET_CODE = markdown.bold(r'🤖Ваш код для регистрации рефералов: ')
REFERRAL_GET_LINK = markdown.bold(r'🤖Ваша ссылка для регистрации рефералов: ')
REFERRAL_LINK_TEMPLATE = r'https://t.me/HomeGPTbot?start={}'
REFERRAL_START_ADD_BY_CODE = markdown.bold(r'🤖Отправьте реферальный код для регистрации...')

PROMO_CODE_START_MESSAGE = r'🎫Введите промокод: '
PROMO_CODE_ACTIVE_STATUS = r'🔖Промокод успешно активирован. Вам начислено {} токенов...'
PROMO_CODE_USED_STATUS = r'😊Да, мы не начислим Вам токенов, потому что Вы уже активировали этот промокод...'
PROMO_CODE_DISABLE_STATUS = r'😗Нет, нет, промокод уже старый... Промокод уже неактивен...'
PROMO_CODE_NONE_STATUS = r'💨Это что такое? Такого кода не существует...'

CANCEL_MESSAGE = r'🦖Отменено...'
TO_CANCEL_MESSAGE = r'⛔Отменить...'

CHOSE_ACTIONS = r'💡Выберите опцию:'

TOKEN_ABOUT = "💰Токены используются для выполения запросов ChatGPT и генерации изобаражений. Количество токенов " \
              "можно посмотреть в профиле.\n\n🎟️Выберите количество токенов, которое хотите приобрести:"

IMAGE_MESSAGE = r'🖼️Введите описание изображения для генерации...'

PROFILE = "Личный профиль\n\n" \
          "👤Пользователь: {}\n\n" \
          "💎Статус: {}\n" \
          "🎉Токены: {}\n"
