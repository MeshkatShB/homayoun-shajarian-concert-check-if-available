from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient
from telegram_credentials import api_id, api_hash, phone, get_access_hash, username

MESSAGE = 'TICKET SELL STARTED! GO GO GO!'


def send_telegram_message():
    client = TelegramClient('session',
                            api_id,
                            api_hash)

    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)

        client.sign_in(phone, input('Enter the code: '))

    try:
        response = client(ResolveUsernameRequest(username))

        receiver = InputPeerUser(get_access_hash[0][0], get_access_hash[0][1], )
        client.send_message(receiver, MESSAGE, )

        receiver = InputPeerUser(get_access_hash[1][0], get_access_hash[1][1], )
        client.send_message(receiver, MESSAGE, )

        receiver = InputPeerUser(get_access_hash[2][0], get_access_hash[2][1],)
        client.send_message(receiver, MESSAGE, )

    except Exception as e:
        print(e)

    client.disconnect()
