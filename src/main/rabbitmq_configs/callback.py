import json
from src.drivers.telegram_sender import send_telegram_message

def rebbitmq_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    formated_msg = json.loads(msg)

    telegram_message = formated_msg["msg"]

    send_telegram_message(telegram_message)