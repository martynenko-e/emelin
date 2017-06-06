# coding=utf-8
from __future__ import unicode_literals
from transliterate import translit
from django.db import models
import re
# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.alias = re.sub("[^a-zA-Z]", "-", translit(u'%s' % self.name, 'ru', reversed=True)).lower()
        super(Gender, self).save(*args, **kwargs)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/service_category', null=True, blank=True)
    show_on_main = models.BooleanField(default=False)

    def get_image(self):
        if self.image:
            return "/%s" % self.image.url
        else:
            return ""

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_url(self):
        if self.alias:
            return "/service/%s/" % self.alias
        else:
            return "/service/%s/" % self.id

    class Meta:
        verbose_name = u'Категория услуги'
        verbose_name_plural = u'Категории услуг'

    def save(self, *args, **kwargs):
        self.alias = re.sub("[^a-zA-Z]", "-", translit(u'%s' % self.name, 'ru', reversed=True)).lower()
        if self.description:
            self.short_text = self.description[:100]
        super(ServiceCategory, self).save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    gender = models.ForeignKey(Gender, related_name='services', null=True, blank=True)
    category = models.ForeignKey(ServiceCategory, related_name="services", null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_price(self):
        if self.price:
            return "%s грн." % self.price
        else:
            return ""

    def get_time(self):
        if self.time:
            return "%s мин." % self.time
        else:
            return ""

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'

    def save(self, *args, **kwargs):
        self.alias = re.sub("[^a-zA-Z]", "-", translit(u'%s' % self.name, 'ru', reversed=True)).lower()
        super(Service, self).save(*args, **kwargs)


class Info(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    second_phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    logo = models.ImageField(upload_to='static/logo', null=True, blank=True)

    class Meta:
        verbose_name = u'Информация'
        verbose_name_plural = u'Информация'


class Article(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/article', null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_url(self):
        return "/articles/%s/%s/" % (self.publish_date.strftime('%Y/%m/%d'), self.alias),

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    def save(self, *args, **kwargs):
        self.alias = re.sub("[^a-zA-Z]", "-", translit(u'%s' % self.name, 'ru', reversed=True)).lower()
        if self.description:
            self.short_text = self.description[:100]
        super(Article, self).save(*args, **kwargs)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='static/gallery', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    show_on_slide = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Картинка'
        verbose_name_plural = u'Картинки'


class Discount(models.Model):
    service_category = models.ForeignKey(ServiceCategory, related_name='discounts', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    image = models.ForeignKey(Gallery, null=True, blank=True)

    class Meta:
        verbose_name = u'Акция'
        verbose_name_plural = u'Акции'

    def __str__(self):
        return self.image.name

    def __unicode__(self):
        return self.image.name


class SocialNetwork(models.Model):
    pass


class Day(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return self.name


class OpeningHours(models.Model):
    contact = models.ForeignKey("Info", related_name="working_hours")
    weekday_from = models.ForeignKey("Day", related_name="weekday_from")
    weekday_to = models.ForeignKey("Day", related_name="weekday_to")
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)

    def get_display(self):
        return "%s - %s | %02d:%02d - %02d:%02d" % (self.weekday_from.short_name,
                                               self.weekday_to.short_name,
                                               self.from_hour.hour,
                                               self.from_hour.minute,
                                               self.to_hour.hour,
                                               self.to_hour.minute)

    class Meta:
        verbose_name = u'Время работы'
        verbose_name_plural = u'Время работы'


class SpecialDays(models.Model):
    holiday_date = models.DateField()
    closed = models.BooleanField(default=True)
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)



