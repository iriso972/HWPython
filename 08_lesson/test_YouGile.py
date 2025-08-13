import pytest
import requests

base_url = 'https://ru.yougile.com'
user = {
    "e843f31f-426b-4707-9650-d6f29aa1205a": "admin"
    }
author = "Bearer rjSQmrVbmWcctvKoyZQexdhRRsEZdJo9V7ZeEU4NG01I4tzem3Zxyiftbbet+SFh"


@pytest.fixture
def get_project_id():
    body = {
        "title": "ГосУслуги",
        "users": user
    }

    headers = {
        "Authorization": author
    }

    resp = requests.post(base_url + '/api-v2/projects', json=body, headers=headers)
    yield resp.json()["id"]

# Создать проект (позитивный тест)


def test_create():
    body = {
        "title": "ГосУслуги",
        "users": user
    }

    headers = {
        "Authorization": author,
        "Content-Type": "application/json"
    }

    resp = requests.post(base_url + '/api-v2/projects', json=body, headers=headers)
    print(resp.json())

    assert resp.status_code == 201


# Создать проект с невалидным токеном (негативный тест)


def test_create_n():
    body = {
        "title": "ГосУслуги",
        "users": user
    }

    headers = {
        "Authorization": "Bearer rjSQmrVbmWcctvKoyZQexdhRRsEZdJo9V7ZeEU4NG01I4tzem3Zxyiftbbet+",
        "Content-Type": "application/json"
    }

    resp = requests.post(base_url + '/api-v2/projects', json=body, headers=headers)
    print(resp.json())

    assert resp.status_code == 401

# Изменить проект


def test_update(get_project_id):
    body = {
        "title": "НеГосУслуги",
        "deleted": False,
        "users": user
    }

    id = get_project_id
    headers = {
        "Authorization": author,
        "Content-Type": "application/json"
    }

    resp = requests.put(base_url + f'/api-v2/projects/{id}', json=body, headers=headers)

    assert resp.status_code == 200

# Изменить проект в title нет значения (негативный тест)


def test_update_n(get_project_id):
    body = {
        "title": "",
        "deleted": False,
        "users": user
    }

    id = get_project_id
    headers = {
        "Authorization": author,
        "Content-Type": "application/json"
    }

    resp = requests.put(base_url + f'/api-v2/projects/{id}', json=body, headers=headers)

    assert resp.status_code == 400

# Получить проект по ID


def test_give(get_project_id):
    body = {
        "title": "СовсемНеГосУслуги",
        "deleted": False,
        "timestamp": 202508071850,
        "users": user
        }

    id = get_project_id
    headers = {
        "Authorization": author,
        "Content-Type": "application/json"
    }

    resp = requests.get(base_url + f'/api-v2/projects/{id}', headers=headers)

    assert resp.status_code == 200

    # Получить проект по ID метод POST (негативный тест)


def test_give_n(get_project_id):
    body = {
        "title": "СовсемНеГосУслуги",
        "deleted": False,
        "timestamp": 202508071850,
        "users": user
    }

    id = get_project_id
    headers = {
        "Authorization": author,
        "Content-Type": "application/json"
    }

    resp = requests.post(base_url + f'/api-v2/projects/{id}', json=body, headers=headers)

    assert resp.status_code == 404
