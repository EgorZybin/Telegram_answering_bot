from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=False)  # id пользователя Telegram
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    language_code = Column(String, nullable=True)
    date_joined = Column(DateTime, server_default=func.now())  # Дата присоединения пользователя

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, first_name={self.first_name})>"


