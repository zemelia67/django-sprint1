"""
Конфигурация URL для проекта blogiсum.

Список `urlpatterns` направляет URL-адреса к представлениям.
Документация: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin

from django.urls import include, path


urlpatterns = [
    # Главная страница - включает URL-адреса из приложения blog.
    path('', include('blog.urls', namespace='blog')),

    # Страницы сайта - включает URL-адреса из приложения pages.
    path('pages/', include('pages.urls', namespace='pages')),

    # Административная панель Django.
    path('admin/', admin.site.urls),
]
