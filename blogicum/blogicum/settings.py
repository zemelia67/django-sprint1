"""
Настройки Django для проекта blogicum.

Сгенерировано командой 'django-admin startproject' с использованием Django 5.1.1.

Для получения дополнительной информации о файле настроек см.:
https://docs.djangoproject.com/en/5.1/topics/settings/

Полный список настроек и их значений:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# BASE_DIR - абсолютный путь к корневой директории проекта.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ.
SECRET_KEY = 'django-insecure-%jz#q0-n+^g!a8=m#$$bf-30)c-6(8t2)gocu4%7(tff*+s2w$'

# Режим отладки - показывает подробные ошибки.
DEBUG = True

# Разрешенные хосты (домены), которые могут обслуживать этот сайт.
ALLOWED_HOSTS = []


# Определение установленных приложений и middleware.

INSTALLED_APPS = [
    # Стандартные приложения Django.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Мои приложения.
    'blog.apps.BlogConfig',
    'pages.apps.PagesConfig',
]

# Middleware - промежуточные слои обработки запросов.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневая конфигурация URL.
ROOT_URLCONF = 'blogicum.urls'

# Путь к директории с шаблонами.
TEMPLATES_DIR = BASE_DIR / 'templates'

# Настройки шаблонов.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # Где искать шаблоны.
        'APP_DIRS': True,  # Искать шаблоны в поддиректориях 'templates'.
        'OPTIONS': {
            'context_processors': [  # Процессоры контекста.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение для развертывания.
WSGI_APPLICATION = 'blogicum.wsgi.application'


# Настройки базы данных.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite.
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу БД.
    }
}


# Валидаторы паролей.

AUTH_PASSWORD_VALIDATORS = [
    {
        # Проверяет схожесть пароля с атрибутами пользователя.
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Проверяет минимальную длину пароля.
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Проверяет, не является ли пароль слишком распространенным.
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Проверяет, не состоит ли пароль только из цифр.
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Настройки интернационализации

LANGUAGE_CODE = 'en-us'  # Язык по умолчанию - английский (США)

TIME_ZONE = 'UTC'  # Часовой пояс - UTC

USE_I18N = True  # Включена система интернационализации

USE_TZ = True  # Использовать часовые пояса


# Настройки статических файлов (CSS, JavaScript, Images)

STATIC_URL = 'static/'  # URL-префикс для статических файлов

# Дополнительные директории со статическими файлами.
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',  # Директория для статических файлов в разработке
]

# Тип поля для автоматических первичных ключей

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
