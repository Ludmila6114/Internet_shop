"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Главная',
            'year': datetime.now().year,
        }
    )


def your_choice(request):
    """Renders the blog page."""

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/your_choice.html',
        {
            'title': 'Корзина',
            'year': datetime.now().year,
        }
    )


def products(request):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products.html',
        {
            'title': 'Каталог товаров',
            'message': 'Описания основных товаров (цены, характеристики, изображения)',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Контакты со мной',
            'year': datetime.now().year,
        }
    )

