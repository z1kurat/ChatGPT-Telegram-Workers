from server import HOST
from server import PORT

from API import TELEGRAM_BOT_TOKEN

WEBHOOK_SSL_CERT = './cert/webhook_cert.pem'
WEBHOOK_SSL_PRIV = './cert/webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (HOST, PORT)
WEBHOOK_URL_PATH = "/%s/" % TELEGRAM_BOT_TOKEN

