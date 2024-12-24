import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from src.services.scheduler import send_message_to_all_users, schedule_broadcast
from src.models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Фикстура для сессии базы данных с использованием SQLite
@pytest.fixture(scope="function")
def db_session():
    engine = create_engine('sqlite:///:memory:')  # Используем SQLite в памяти
    Session = sessionmaker(bind=engine)
    session = Session()

    # Создаем таблицы
    User.metadata.create_all(engine)

    yield session

    # Закрываем сессию после тестов
    session.close()


# Тестирование функции send_message_to_all_users
@patch('src.services.scheduler.Session', return_value=MagicMock())
def test_send_message_to_all_users(mock_session, db_session):
    # Создаем пользователей в базе данных для теста
    user_1 = User(user_id=1, first_name="User1", last_name="Test1")
    user_2 = User(user_id=2, first_name="User2", last_name="Test2")
    db_session.add(user_1)
    db_session.add(user_2)
    db_session.commit()

    # Мокируем поведение send_message_to_all_users
    mock_session.query().all.return_value = [user_1, user_2]

    # Выполняем тестируемую функцию
    message = "Test broadcast message"
    with patch("builtins.print") as mock_print:
        mock_print.reset_mock()
        send_message_to_all_users(message)
        mock_print.assert_any_call("Отправлено сообщение пользователю 1: Test broadcast message")
        mock_print.assert_any_call("Отправлено сообщение пользователю 2: Test broadcast message")


# Тестирование функции schedule_broadcast
def test_schedule_broadcast(db_session):
    message = "Scheduled broadcast message"
    send_time = datetime.now() + timedelta(seconds=10)

    # Мокируем планировщик задач
    with patch.object(AsyncIOScheduler, 'add_job') as mock_add_job:
        schedule_broadcast(message, send_time)
        mock_add_job.assert_called_once()  # Проверяем, что задача была добавлена
        args, kwargs = mock_add_job.call_args
        assert args[0] == send_message_to_all_users  # Проверяем, что передали правильную функцию
        assert args[1] == DateTrigger(run_date=send_time)  # Проверяем, что передали правильный триггер
        assert args[2] == [message]  # Проверяем, что передали сообщение
