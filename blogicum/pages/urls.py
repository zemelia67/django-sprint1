from django.urls import path

from . import views

# Пространство имен для URL-адресов приложения.
app_name = 'pages'

# Список URL-шаблонов приложения.
urlpatterns = [
    # Страница "О проекте".
    path('about/', views.about, name='about'),

    # Страница "Наши правила".
    path('rules/', views.rules, name='rules'),
]
