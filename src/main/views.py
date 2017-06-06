# coding=utf-8
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from models import *
# Create your views here.

MAIN_PAGE_LIST_COUNT = 4


def index(request):
    title = "Студия лазерной косметологии - Emelin"
    services = map(lambda obj: {
        "name": obj.name,
        "short_text": obj.short_text,
        "url": obj.get_url(),
        "image": obj.image.url,
    }, ServiceCategory.objects.filter(show_on_main=True))

    articles = map(lambda obj: {
        "name": obj.name,
        "short_text": obj.short_text,
        "url": "%s" % obj.get_url(),
    }, Article.objects.filter(publish_date__lt=timezone.now())[:MAIN_PAGE_LIST_COUNT])

    discounts = map(lambda obj: {
        "description": obj.description,
        "image": obj.image.image.url,
    }, Discount.objects.all()[:MAIN_PAGE_LIST_COUNT])

    slider = map(lambda obj: {
        "description": obj.description,
        "image": obj.image.url,
    }, Gallery.objects.filter(show_on_slide=True))

    return render(request, 'index.html', {
        "title": title,
        "services": services,
        "articles": articles,
        "discounts": discounts,
        "slider": slider,
    })


def service_category(request):
    title = "Услуги - Emelin"
    services = map(lambda obj: {
        "image": obj.get_image(),
        "name": obj.name,
        "short_text": obj.short_text,
        "url": obj.get_url(),
    }, ServiceCategory.objects.all())

    return render(request, 'service_categories.html', {
        "title": title,
        "services": services,
        "breadcrumb_title": "Все услуги"
    })


def service(request, alias):
    if alias.isdigit():
        service_category_obj = ServiceCategory.objects.filter(id=alias)
    else:
        service_category_obj = ServiceCategory.objects.filter(alias=alias)

    title = u"%s - Услуга - Emelin" % service_category_obj[0].name
    category_name = service_category_obj[0].name
    description = service_category_obj[0].description
    services = map(lambda service: {
        "name": service.name,
        "time": service.get_time(),
        "price": service.get_price(),
    }, service_category_obj[0].services.all())

    return render(request, 'service.html', {
        "title": title,
        "services": services,
        "description": description,
        "category_name": category_name,
        "image": service_category_obj[0].get_image()
    })


def articles(request):
    title = "Статьи - Emelin"
    article_list = map(lambda article: {
        "name": article.name,
        "short_text": article.short_text,
        "date": article.publish_date.strftime('%Y %B %d'),
        "image": article.get_image(),
        "url": "%s" % article.get_url(),
    }, Article.objects.filter(publish_date__lt=timezone.now()))

    return render(request, 'articles.html', {
        "title": title,
        "articles": article_list,
        "breadcrumb_title": "Статьи"
    })


def article(request, year="2017", month="2", day="9", alias=""):
    title = "Акции - Emelin"
    current_article = Article.objects.filter(publish_date__year=year,
                                             publish_date__day=day,
                                             publish_date__month=month,
                                             alias=alias)
    if len(list(current_article)) > 0:
        current_article = current_article[0]
    else:
        raise Http404()

    description = current_article.description
    new_lines = re.compile(r'[\r\n]\s+')
    description = '<p>' + '</p>\n\n<p>'.join(re.split(new_lines, description)) + '</p>'

    return render(request, 'article.html', {
        "title": title,
        "article_name": current_article.name,
        "article_description": description,
    })


def discount(request):
    title = "Акции - Emelin"
    discount_list = map(lambda obj: {
        "text": obj.description,
        "image": "/%s" % obj.image.image.url,
    }, Discount.objects.all())

    return render(request, 'discount.html', {
        "title": title,
        "discount_list": discount_list,
        "breadcrumb_title": "Акции"
    })


def contact(request):
    title = "Контакты - Emelin"
    info = Info.objects.all()[0]
    phone = info.phone
    address = info.address
    about = info.about
    working_hour = map(lambda data: {
        "day": data.get_display()
    }, info.working_hours.all())

    return render(request, 'contact.html', {
        "title": title,
        "phone": phone,
        "address": address,
        "about": about,
        "working_hour": working_hour,
        "breadcrumb_title": "Контакты"
    })


def price(request):
    title = "Цены - Emelin"

    context = map(lambda obj: {
        "name": obj.name,
        "url": obj.get_url(),
        "services": map(lambda service: {
            "name": service.name,
            "price": service.get_price(),
            "time": service.get_time(),
        }, obj.services.all())
    }, ServiceCategory.objects.filter())

    return render(request, 'price.html', {
        "title": title,
        "context": context,
        "breadcrumb_title": "Цены"
    })



