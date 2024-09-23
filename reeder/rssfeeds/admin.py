from django.contrib import admin

from .models import RssArticle, RssFeed

admin.site.register(RssFeed)
admin.site.register(RssArticle)
