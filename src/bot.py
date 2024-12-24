from telethon import TelegramClient, events
from src.handlers.messages import handle_message
import os
from dotenv import load_dotenv
from src.services.scheduler import scheduler

# Загрузка переменных окружения
load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
bot_token = os.getenv("TELEGRAM_TOKEN")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Запуск планировщика
scheduler.start()


@client.on(events.NewMessage)
async def handler(event):
    # Логика обработки сообщения
    await handle_message(event)  # Вызов вашей функции для обработки сообщения


client.run_until_disconnected()
