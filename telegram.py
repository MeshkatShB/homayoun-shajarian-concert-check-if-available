from telegram_credentials import api_id, api_hash, phone, get_access_hash
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


def send():
    message = "TICKET SELL STARTED! GO GO GO!"

    client = TelegramClient('session', api_id, api_hash)

    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)

        client.sign_in(phone, input('Enter the code: '))

    try:
        for gah in get_access_hash:
            receiver = InputPeerUser(gah[0], gah[1])
            client.send_message(receiver, message, parse_mode='html')

    except Exception as e:

        print(e)

    client.disconnect()
