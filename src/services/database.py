from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.user import Base
import os

DATABASE_URL = os.getenv("DATABASE_URL")  # Из .env

# Настройка подключения
engine = create_engine(DATABASE_URL, echo=True)

# Создание сессии
Session = sessionmaker(bind=engine)

# Создание всех таблиц, если они еще не созданы
Base.metadata.create_all(bind=engine)
