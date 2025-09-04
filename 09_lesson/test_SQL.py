from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Создаем подключение к базе данных
db_connection_string = "postgresql://postgres:1@localhost:5432/TEST_DB"
db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, primary_key=True)
    subject_id = Column(Integer, primary_key=True)


# Добавление нового пользователя
def test_add_user():
    session = Session()
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    session.add(users)
    session.commit()

    saved = session.query(User).filter_by(user_id=18).first()
    assert saved.user_email == "sashaivanov@mail.ru"

    session.delete(saved)
    session.commit()
    session.close()


# Изменение user_email пользователя
def test_query_user():
    session = Session()
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    session.add(users)
    session.commit()

    # Получение пользователя и смена email
    saved = session.query(User).filter_by(user_id=18).first()
    saved.user_email = "mashaivanova@mail.ru"
    session.commit()

    # Проверка изменения
    updated = session.query(User).filter_by(user_id=18).first()
    assert updated.user_email == "mashaivanova@mail.ru"

    # Удаление тестовых данных
    session.delete(updated)
    session.commit()
    session.close()


# Удаление пользователя
def test_delete_user():
    session = Session()
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    session.add(users)
    session.commit()

    saved = session.query(User).filter_by(user_id=18).first()
    assert saved.user_email == "sashaivanov@mail.ru"

    # Удаление тестовых данных
    session.delete(saved)
    session.commit()
    session.close()
