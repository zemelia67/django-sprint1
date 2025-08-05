from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Конфигурация Django-приложения 'blog'.

    Наследуется от базового класса AppConfig и определяет
    основные параметры конфигурации приложения.
    """

    # Автоматическое поле для первичных ключей моделей.
    default_auto_field = 'django.db.models.BigAutoField'

    # Имя приложения (должно соответствовать имени папки приложения).
    name = 'blog'
