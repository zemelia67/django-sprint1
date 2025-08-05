# Blogicum
Блогикум - Платформа для ведения блога

Описание проекта

Блогикум - это веб-приложение для ведения персонального блога с возможностью публикации записей, их категоризации и комментирования.
Основные возможности

    📝 Публикация записей с указанием места и даты

    🗂️ Категоризация записей

    🔍 Фильтрация по категориям

    📱 Адаптивный дизайн для всех устройств

    🔐 Система аутентификации (в разработке)

Технологический стек
Backend

    Python 3.10+

    Django 4.2

    Django Templates

Frontend

    Bootstrap 5

    HTML5, CSS3

    JavaScript (минимально)


Установка и запуск
Требования

    Python 3.10+

    pip

Инструкция по установке

    Клонировать репозиторий:

bash

git clone https://github.com/zemelia67/django-sprint1.git
cd blogikum

    Создать и активировать виртуальное окружение:

bash

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

    Установить зависимости:

bash

pip install -r requirements.txt

    Применить миграции:

bash

python manage.py migrate

    Создать суперпользователя:

bash

python manage.py createsuperuser

    Запустить сервер разработки:

bash

python manage.py runserver

Приложение будет доступно по адресу: http://127.0.0.1:8000
Структура проекта
text

blogikum/
├── blog/                  # Приложение блога
│   ├── migrations/        # Миграции базы данных
│   ├── templates/         # Шаблоны
│   ├── urls.py            # URL-маршруты
│   ├── views.py           # Представления
│   └── ...
├── pages/                 # Приложение статических страниц
├── static/                # Статические файлы (CSS, JS, изображения)
├── templates/             # Базовые шаблоны
├── manage.py              # Скрипт управления Django
└── settings.py            # Настройки проекта

🧑‍💻 Об авторе

Привет! Меня зовут Кирилл, я начинающий Python-разработчик.
Это мой первый проект на Django, созданный в рамках изучения языка Python.

🔹 Цель проекта: Изучение основ Django  
🔹 Дата создания: Август 2025 