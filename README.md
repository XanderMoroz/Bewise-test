# Bewise-test

Bewise-test - backend-сервис на основе FastAPI, позволяющий извлекать англоязычные вопросы для викторин из публичного API(jService). База данных - `PostgreSQL`. ORM - `SqlAlchemy`. Миграции - `Alembic`. Валидация данных - `Pydantic`. Зависимости - `Poetry`. Линтер - `Flake8`. Контейнеризация - `Docker`.

## Краткая документация API
Работа с моделями БД осуществляется по следующим эндпоинтам: 

Method | HTTP request                  | Description
------------- |-------------------------------| -------------
[**create_question**] | **POST** /questions             | Извлечение произвольного количества вопросов.

#### Пример запроса в формате JSON 

```sh
{"questions_num": integer} 
```

#### Пример ответа в формате JSON

```sh
[
  {
    "question_id": 70005,
    "question_text": "Your brother's outgrown clothes worn by you... whether you like it or not",
    "answer_text": "hand-me-downs",
    "time_created": "2022-10-12T18:16:09.395248Z"
  }
]
```
Исчерпывающую информацию по работе API можно получить после запуска. Документация на основе Swagger, в соответствии со стандартом OpenAPI.

## Инструкция по установке
1. ### Подготовка проекта

1.1 Клонируете репозиторий
```sh
git clone https://github.com/XanderMoroz/Bewise-test.git
```

1.2 В корневой папки клонированного репозитория создаете файл .env

1.3 В файлe .env создаете переменные для для подключеня к базе данных. Например:

```sh
# POSTGRESQL DEFAULT DATABASE
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=bewise
```
2. ### Запуск проекта с Doker

2.1 Создаете и запускаете контейнер через терминал:
```sh
sudo docker-compose up --build
```
2.2 Сервис доступен по адресу: http://0.0.0.0:8000/