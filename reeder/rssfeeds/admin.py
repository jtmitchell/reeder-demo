# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import RssFeed, RssArticle

admin.site.register(RssFeed)
admin.site.register(RssArticle)
