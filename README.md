# Telegram Bot

Этот проект представляет собой Telegram-бота для автоматизации обработки входящих сообщений, реализации исходящих
сообщений по триггеру и рассылки с планированием времени.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/EgorZybin/Telegram_answering_bot.git
   cd Telegram_answering_bot
   ```

2. Установите зависимости:

```
pip install -r requirements.txt
```

3. Запустите бота:

```
python bot.py
```

## Запуск в Docker

1. Построить Docker-образ:

```
docker build -t telegram-bot .
```

2. Запустить бота в Docker-контейнере:

```
docker-compose up -d
```

## Тестирование

1. Запустите тесты:
```
pytest tests/
```

# Используемые технологии

- Python 
- telethon
- APScheduler для планирования рассылок
- Docker для контейнеризации
- pytest для тестирования

### Заключение

Проект включает в себя:
- Полный функционал Telegram-бота: обработка команд, триггеров, настройка рассылок.
- Тесты с использованием библиотеки `pytest` для проверки работы бота и планировщика.
- Контейнеризация через Docker для упрощения развертывания.

Этот код можно сразу развернуть и использовать, подставив свой `BOT_TOKEN` в .env.

