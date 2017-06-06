# coding=utf-8
from models import Article, Discount


def registry(request):
    all_news = Article.objects.filter()
    latest_article = map(lambda obj: {
        "name": obj.name,
        "text": obj.short_text,
        "url": "%s" % obj.get_url(),
    }, all_news.order_by("-date")[:5])
    all_news_count = all_news.count()
    all_discount = Discount.objects.filter()
    latest_discount = map(lambda obj: {
        "text": obj.description,
    }, all_discount[:5])
    all_discount_count = all_discount.count()
    return {
        "logo": "/static/images/logo.png",
        "caption": u"Студия лазерной косметологии",
        "latest_article": latest_article,
        "latest_discount": latest_discount,
        "all_news_count": all_news_count,
        "all_discount_count": all_discount_count,
    }
