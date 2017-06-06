"""Emelin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^service/$', views.service_category, name='service_category'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^discount/$', views.discount, name='discount'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<alias>[\d\w\-]+)/$', views.article),
    url(r'^price/$', views.price, name='price'),
    url(r'^service/(?P<alias>[a-zA-Z\-0-9]+)/', views.service, name='service'),
]
