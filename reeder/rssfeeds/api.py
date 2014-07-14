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

    """
    @api {get} /api/feeds/ List of feeds
    @apiVersion 0.0.2
    @apiName ListFeeds
    @apiGroup Feeds
    
    @apiSuccess {Feed[]} objects List of feeds
    @apiSuccess {Url} objects.url URL for the RSS feed
    @apiSuccess {String} objects.name Name of the feed
    @apiSuccess {Number} objects.id ID for the feed
    @apiSuccess {DateTime} objects.lastmodified Date and time of the last modification to the feed.
    """
    def list(self):
        return RssFeed.objects.all()

    """
    @api {get} /api/feeds/:id Feed detail
    @apiVersion 0.0.2
    @apiName GetFeed
    @apiGroup Feeds
    
    @apiSuccess {Url} url URL for the RSS feed
    @apiSuccess {String} name Name of the feed
    @apiSuccess {Number} id ID for the feed
    @apiSuccess {DateTime} lastmodified Date and time of the last modification to the feed.
    """
    def detail(self, pk):
        return RssFeed.objects.get(id=pk)

    """
    @api {post} /api/feeds/ Create new Feed
    @apiVersion 0.0.2
    @apiName PostFeed
    @apiGroup Feeds
    
    @apiParam {Url} url URL for the RSS feed
    @apiParam {String} name Name of the feed
    @apiParam {Number} id ID for the feed
    """
    def create(self):
        return RssFeed.objects.create(
            url=self.data['url'],
            name=self.data['name'],
        )

    """
    @api {put} /api/feeds/:id Update an existing Feed
    @apiVersion 0.0.2
    @apiName UpdateFeed
    @apiGroup Feeds
    
    @apiParam {Number} id ID for the feed
    @apiParam {Url} url URL for the RSS feed
    @apiParam {String} name Name of the feed

    @apiSuccess {Url} url URL for the RSS feed
    @apiSuccess {String} name Name of the feed
    @apiSuccess {Number} id ID for the feed
    @apiSuccess {DateTime} lastmodified Date and time of the last modification to the feed.
    """
    def update(self, pk):
        try:
            feed = RssFeed.objects.get(id=pk)
        except RssFeed.DoesNotExist:
            feed = RssFeed()

        feed.name = self.data['name']
        feed.url = self.data['url']
        feed.save()
        return feed

    """
    @api {delete} /api/feeds/:id Feed detail
    @apiVersion 0.0.2
    @apiName DeleteFeed
    @apiGroup Feeds

    @apiParam {Number} id ID for the feed
    """
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
