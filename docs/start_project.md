# Инструкция к запуску проекта

## Настройка проекта.

1. Создать файл `.env`. Или скопировать его: `cp .env.example .env`
2. Заполнить полня в `env` файле.
- - `POSTGRES_DB` --  Имя Базы Данных(БД)
- - `POSTGRES_USER`-- Имя пользователя БД
- - `POSTGRES_PASSWORD` -- Пароль БД
- - `PG_HOST` -- Хот БД взят из docker `db`
- - `FLASK_APP=main.py` -- Имя эндпоинта.


## Запуск проекта
Выполнить `docker-compose up`
Сайт будет доступен адресу `0.0.0.0:8001`

## Так же нужно накатить миграции.

1. выпалнить команду `make ssh_web`
2. выполнить команду в `flask db upgrade`

Альтернативный способ:
1. make upgrade

более подробно:
https://flask-migrate.readthedocs.io/en/latest/