from src.services.database import Session
from src.models.user import User
from sqlalchemy.exc import IntegrityError


def add_or_update_user(user_id, first_name=None, last_name=None, username=None, language_code=None):
    # Создаем сессию
    session = Session()

    try:
        # Проверяем, существует ли пользователь
        user = session.query(User).filter_by(user_id=user_id).first()

        if user:
            # Если пользователь существует, обновляем его данные
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.language_code = language_code
        else:
            # Если пользователя нет, создаем нового
            user = User(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                language_code=language_code
            )
            session.add(user)

        session.commit()
    except IntegrityError:
        session.rollback()
        print(f"Ошибка при добавлении/обновлении пользователя с id {user_id}")
    finally:
        session.close()
