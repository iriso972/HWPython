import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Создаем фикстуру pytest
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine("postgresql://postgres:1@localhost:5432/TEST_DB")
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, primary_key=True)
    subject_id = Column(Integer, primary_key=True)


# Добавление нового пользователя
def test_add_user(db_session):
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    db_session.add(users)
    db_session.commit()

    saved = db_session.query(User).filter_by(user_id=18).first()
    assert saved.user_email == "sashaivanov@mail.ru"

    db_session.delete(saved)
    db_session.commit()
    db_session.close()


# Изменение user_email пользователя
def test_query_user(db_session):
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    db_session.add(users)
    db_session.commit()

    # Получение пользователя и смена email
    saved = db_session.query(User).filter_by(user_id=18).first()
    saved.user_email = "mashaivanova@mail.ru"
    db_session.commit()

    # Проверка изменения
    updated = db_session.query(User).filter_by(user_id=18).first()
    assert updated.user_email == "mashaivanova@mail.ru"

    # Удаление тестовых данных
    db_session.delete(updated)
    db_session.commit()
    db_session.close()


# Удаление пользователя
def test_delete_user(db_session):
    users = User(user_id=18, user_email="sashaivanov@mail.ru", subject_id=1)
    db_session.add(users)
    db_session.commit()

    saved = db_session.query(User).filter_by(user_id=18).first()
    assert saved.user_email == "sashaivanov@mail.ru"

    # Удаление тестовых данных
    db_session.delete(saved)
    db_session.commit()
    db_session.close()
