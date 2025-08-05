from django.urls import path

from . import views

app_name = 'blog'  # Пространство имен для URL.

urlpatterns = [
    # Главная страница со списком всех постов.
    path('', views.index, name='index'),

    # Страница отдельного поста (по ID).
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),

    # Страница с постами определенной категории.
    path('category/<slug:post_category>/',
         views.category_posts,
         name='category_posts'),
]
