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

    def is_authenticated(self):
        return True if self.request.META.get('HTTP_AUTHORIZATION') == '1234' else False

    def list(self):
        return RssFeed.objects.all()

    def detail(self, pk):
        return RssFeed.objects.get(id=pk)

    def create(self):
        return RssFeed.objects.create(
            url=self.data['url'],
            name=self.data['name'],
        )

    def update(self, pk):
        try:
            feed = RssFeed.objects.get(id=pk)
        except RssFeed.DoesNotExist:
            feed = RssFeed()

        feed.name = self.data['name']
        feed.url = self.data['url']
        feed.save()
        return feed

    def delete(self, pk):
        RssFeed.objects.get(id=pk).delete()


class RssArticleResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'url': 'url',
        'feed': 'feed.name',
        'snippet': 'snippet',
        'is_read': 'is_read',
        'lastmodified': 'lastmodified',
    })

    def is_authenticated(self):
        return True if self.request.META.get('HTTP_AUTHORIZATION') == '1234' else False

    def list(self):
        return RssArticle.objects.all()

    def detail(self, pk):
        return RssArticle.objects.get(id=pk)

    def create(self):
        return RssArticle.objects.create(
            url=self.data['url'],
            feed=RssFeed.objects.get(name=self.data['feed']),
            snippet=self.data['snippet'],
            is_read=self.data['is_read'],
        )

    def update(self, pk):
        try:
            article = RssArticle.objects.get(id=pk)
        except RssArticle.DoesNotExist:
            article = RssArticle()

        article.url = self.data['url']
        article.feed = RssFeed.objects.get(name=self.data['name'])
        article.snippet = self.data['snippet']
        article.is_read = self.data['is_read']
        article.save()
        return article

    def delete(self, pk):
        RssArticle.objects.get(id=pk).delete()
