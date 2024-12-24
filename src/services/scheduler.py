from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from src.services.database import Session
from src.models.user import User


scheduler = AsyncIOScheduler()

# Запуск планировщика
scheduler.start()


# Функция для рассылки сообщения всем пользователям
async def send_message_to_all_users(message):
    session = Session()
    users = session.query(User).all()

    for user in users:
        print(f"Отправлено сообщение пользователю {user.user_id}: {message}")

    session.close()


# Функция для планирования рассылки
def schedule_broadcast(message, send_time):
    trigger = DateTrigger(run_date=send_time)
    scheduler.add_job(send_message_to_all_users, trigger, args=[message])
