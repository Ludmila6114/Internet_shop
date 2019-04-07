"""internet_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.conf.urls import include
import app.views


urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^products$', app.views.products, name='products'),
    url(r'^your_choice$', app.views.your_choice, name='your_choice'),


]
