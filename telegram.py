from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient, sync, events

from telegram_credentials import api_id, api_hash, phone, get_access_hash

# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


def send():
    # get your api_id, api_hash, token
    # from telegram as described above
    message = "TICKET SELL STARTED! GO GO GO!"

    # your phone number

    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)

    # connecting and building the session
    client.connect()

    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the code: '))

    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        receiver = InputPeerUser(get_access_hash[2][0], get_access_hash[2][1])
        client.send_message(receiver, message, parse_mode='html')

        receiver = InputPeerUser(get_access_hash[1][0], get_access_hash[1][1])
        client.send_message(receiver, message, parse_mode='html')

        # sending message using telegram client
        receiver = InputPeerUser(get_access_hash[0][0], get_access_hash[0][1])
        client.send_message(receiver, message, parse_mode='html')
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e)

    # disconnecting the telegram session
    client.disconnect()
