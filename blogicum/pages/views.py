from django.shortcuts import render


def about(request):
    """
    Обрабатывает запрос страницы "О проекте".

    Args:
        request (HttpRequest): Объект HTTP-запроса

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном about.html
    """
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """
    Обрабатывает запрос страницы "Правила сайта".

    Args:
        request (HttpRequest): Объект HTTP-запроса

    Returns:
        HttpResponse: Ответ с отрендеренным шаблоном rules.html
    """
    template = 'pages/rules.html'
    return render(request, template)
