# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import RssFeed, RssArticle


class RssFeedResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'url': 'url',
        'name': 'name',
        'lastmodified': 'lastmodified',
    })

    def list(self):
        return RssFeed.objects.all()

    def detail(self, pk):
        return RssFeed.objects.get(id=pk)


class RssArticleResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'url': 'url',
        'feed': 'feed.name',
        'snippet': 'snippet',
        'is_read': 'is_read',
        'lastmodified': 'lastmodified',
    })

    def list(self):
        return RssArticle.objects.all()

    def detail(self, pk):
        return RssArticle.objects.get(id=pk)
