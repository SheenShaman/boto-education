## Тестовое задание для Boto Education
Небольшой сервис для сокращения ссылок с HTTP API.

### Возможности:
- Создание короткой ссылки
- Редирект по короткому коду
- Хранение данных в SQLite
- Тесты на pytest
- Логирование

### Технологии

- Python 3.12+
- FastAPI
- SQLite
- pytest


## Установка и запуск
- git clone https://github.com/SheenShaman/boto-education.git
- cd boto-education
- python -m venv .venv
- source .venv/bin/activate
- pip install poetry
- poetry install
- uvicorn app.main:app --reload
- pytest (для тестирования)