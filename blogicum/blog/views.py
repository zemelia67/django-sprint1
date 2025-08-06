from django.shortcuts import render
from django.http import Http404

# Список словарей с данными постов блога
posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]


def index(request):
    """
    Главная страница блога - отображает все посты в обратном порядке.

    Args:
        request: HttpRequest объект

    Returns:
        HttpResponse с рендеренным шаблоном blog/index.html,
        содержащим перевернутый список постов
    """
    template = 'blog/index.html'
    newlist = sorted(posts, key=lambda d: -d['id'])
    context = {'posts': newlist}
    return render(request, template, context)


def post_detail(request, post_id):
    """
    Страница просмотра отдельного поста.

    Args:
        request: HttpRequest объект
        post_id: ID поста (индекс в списке posts)

    Returns:
        HttpResponse с шаблоном blog/detail.html,
        содержащим данные конкретного поста

    Note:
        При несуществующем post_id вызовет IndexError
    """
    template = 'blog/detail.html'
    try:
        # Преобразуем post_id в число (на случай если пришла строка)/
        post_id = int(post_id)

        # Проверяем что ID находится в допустимом диапазоне
        if post_id < 0 or post_id >= len(posts):
            raise IndexError("ID поста вне допустимого диапазона")

        post = posts[post_id]
        context = {'post': post}
        return render(request, template, context)
    except (IndexError):
        raise Http404("Некорректный ID поста")


def category_posts(request, post_category):
    """
    Отображает посты определенной категории.

    Args:
        request: HttpRequest объект
        post_category: Название категории для фильтрации

    Returns:
        HttpResponse с шаблоном blog/category.html,
        содержащим отфильтрованные по категории посты
        и название категории
    """
    template = 'blog/category.html'
    filtered_posts = [post for post in posts
                      if post['category'] == post_category]
    context = {'posts': filtered_posts, 'category': post_category}

    return render(request, template, context)
