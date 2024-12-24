from datetime import datetime
from src.services.scheduler import schedule_broadcast
import re
from src.services.user_service import add_or_update_user


async def handle_message(event):
    user_id = event.sender_id
    message = event.raw_text

    # Получаем информацию о пользователе
    user = await event.get_sender()

    # Добавляем или обновляем пользователя в базе данных
    add_or_update_user(
        user_id=user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        language_code=user.language_code
    )

    # Логика обработки сообщений
    if "привет" in message.lower():
        await event.respond("Привет! Чем могу помочь?")
    elif "услуги" in message.lower():
        await event.respond("Вот список услуг, которые мы предоставляем: ...")
    elif "рассылка" in message.lower():
        match = re.match(r"рассылка (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) (.+)", message)
        if match:
            send_time_str = match.group(1)
            send_message = match.group(2)

            try:
                send_time = datetime.strptime(send_time_str, "%Y-%m-%d %H:%M")
                schedule_broadcast(send_message, send_time)
                await event.respond(f"Сообщение запланировано на {send_time}.")
            except ValueError:
                await event.respond("Ошибка в формате времени. Пожалуйста, используйте формат 'ГГГГ-ММ-ДД ЧЧ:ММ'.")
        else:
            await event.respond("Неверная команда для рассылки. Формат: 'рассылка ГГГГ-ММ-ДД ЧЧ:ММ Сообщение'.")
