from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    Конфигурационный класс для приложения 'pages'.

    Определяет базовые настройки приложения статических страниц.
    Наследуется от базового класса AppConfig Django.
    """

    # Тип поля для автоматически создаваемых первичных ключей.
    default_auto_field = 'django.db.models.BigAutoField'

    # Имя приложения (должно соответствовать имени папки приложения).
    name = 'pages'
