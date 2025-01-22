from telethon import TelegramClient
from telethon.events import NewMessage

APP_ID = 1252636
API_HASH = '4037e9f957f6f17d461b0c288ffa50f1'

usersId = {
    "Telegram": 1102014206,
    "Т-БАНК": 6630508220,
    "Альфа Банк": 6990842482
}

client = TelegramClient('tg-account', APP_ID, API_HASH)

@client.on(NewMessage(incoming=True))
async def handle_message(event):
    for keyword, userId in usersId.items():
        if keyword in event.message.message:
            await client.send_message(userId, event.message.message)
            break

if __name__ == '__main__':
    print('[*] Connect to client...')
    client.start()
    client.run_until_disconnected()
