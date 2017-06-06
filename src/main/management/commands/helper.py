# -*- coding: utf-8 -*-
import urllib2
import requests
from django.core.files.base import ContentFile
from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from django.utils.text import slugify


def get_soup_from_url(url, save):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    r = requests.get(url, headers=headers, timeout=30)
    if r.status_code == 200:
        html = r.text
        if save:
            file1 = open("parse.html", "w")
            file1.write(html.encode('utf-8'))
            file1.close()
        return BeautifulSoup(html, 'lxml')

    else:
        print "Can't read url %s, status code %s" % (url, r.status_code)


def download_image(self, url):
    input_file = StringIO(urllib2.urlopen(url).read())
    output_file = StringIO()
    img = Image.open(input_file)
    # if img.mode != "RGB":
    #     img = img.convert("RGB")
    img.save(output_file, "PNG")
    try:
        self.logo.save(slugify(self.name).lower() + ".png", ContentFile(output_file.getvalue()),
                       save=True)
    except Exception as e:
        self.logo.save(self.name.lower() + ".png", ContentFile(output_file.getvalue()), save=True)


def download_image_parse(self, url):
    input_file = StringIO(urllib2.urlopen(url).read())
    output_file = StringIO()
    img = Image.open(input_file)
    # if img.mode != "RGB":
    #     img = img.convert("RGB")
    img.save(output_file, "JPEG")
    try:
        self.image.save(slugify(self.name).lower() + ".jpg", ContentFile(output_file.getvalue()),
                        save=True)
    except Exception as e:
        self.image.save(self.name.lower() + ".jpg", ContentFile(output_file.getvalue()), save=True)