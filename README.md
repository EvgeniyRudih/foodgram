# Foodgram

[![Foodgram CI/CD](https://github.com/EvgeniyRudih/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/EvgeniyRudih/foodgram/actions/workflows/main.yml)

Foodgram это веб-приложение для публикации рецептов. Пользователи могут создавать собственные рецепты, добавлять понравившиеся рецепты в избранное, подписываться на авторов и формировать список покупок.

## Возможности проекта

- Регистрация и авторизация пользователей
- Создание, редактирование и удаление рецептов
- Добавление рецептов в избранное
- Подписка на авторов
- Добавление рецептов в список покупок
- Скачивание списка покупок с суммированием ингредиентов
- Фильтрация рецептов по тегам
- Смена пароля
- Загрузка и удаление аватара
- Админ-зона Django

## Технологии

- Python 3.10
- Django
- Django REST Framework
- Djoser
- PostgreSQL
- Gunicorn
- Nginx
- Docker
- Docker Compose
- GitHub Actions
- React (готовый frontend)

## Запуск проекта локально

Клонируйте репозиторий:

```bash
git git@github.com:EvgeniyRudih/foodgram.git
cd foodgram
```

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost 127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost
CORS_ALLOWED_ORIGINS=http://localhost

POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_HOST=db
DB_PORT=5432
```

Перейдите в папку `infra` и запустите контейнеры:

```bash
cd infra
docker compose up -d --build
```

После запуска проект будет доступен по адресам:

- Frontend: [http://localhost/](http://localhost/)
- API Docs: [http://localhost/api/docs/](http://localhost/api/docs/)
- Admin: [http://localhost/admin/](http://localhost/admin/)

## Загрузка данных

После запуска проекта можно загрузить ингредиенты и теги:

```bash
docker exec foodgram-backend python manage.py load_ingredients
docker exec foodgram-backend python manage.py load_tags
```

Создание суперпользователя:

```bash
docker exec -it foodgram-backend python manage.py createsuperuser
```

## Деплой

Проект поддерживает автоматический деплой через GitHub Actions.

После успешного деплоя проект доступен по адресу:

[http://footgram.ddns.net](http://footgram.ddns.net)

## Автор

Разработчик: EvgeniyRudih