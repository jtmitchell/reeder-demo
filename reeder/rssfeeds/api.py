# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import RssFeed, RssArticle


class RssFeedResource(DjangoResource):
    """
    @apiDefineSuccessStructure Feed
    @apiSuccess {Number} id ID for the feed
    @apiSuccess {Url} url URL for the RSS feed
    @apiSuccess {String} name Name of the feed
    @apiSuccess {DateTime} lastmodified Date and time of the last modification to the feed.
    """
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

    @apiParam {Number} id ID for the feed

    @apiSuccessStructure Feed
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

    @apiSuccessStructure Feed
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

    @apiSuccessStructure Feed
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
    @api {delete} /api/feeds/:id Delete an existing Feed
    @apiVersion 0.0.2
    @apiName DeleteFeed
    @apiGroup Feeds

    @apiParam {Number} id ID for the feed

    @apiSuccess (Success 204) empty No data returned
    """
    def delete(self, pk):
        RssFeed.objects.get(id=pk).delete()


class RssArticleResource(DjangoResource):
    """
    @apiDefineSuccessStructure Article
    @apiSuccess {Number} id ID for the article
    @apiSuccess {Url} url URL for the article
    @apiSuccess {String} feed Name of the feed
    @apiSuccess {String} snippet Short extract or summary of the article
    @apiSuccess {Boolean} is_read Has the article been marked as read?
    @apiSuccess {DateTime} lastmodified Date and time of the last modification
    
    """
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

    """
    @api {get} /api/articles/ List of articles
    @apiVersion 0.0.2
    @apiName ListArticles
    @apiGroup Articles
    
    @apiSuccess {Articles[]} objects List of articles
    @apiSuccess {Number} objects.id ID for the article
    @apiSuccess {Url} objects.url URL for the article
    @apiSuccess {String} objects.feed Name of the feed
    @apiSuccess {String} objects.snippet Short extract or summary of the article
    @apiSuccess {Boolean} objects.is_read Has the article been marked as read?
    @apiSuccess {DateTime} objects.lastmodified Date and time of the last modification
    """
    def list(self):
        return RssArticle.objects.all()

    """
    @api {get} /api/articles/:id Article detail
    @apiVersion 0.0.2
    @apiName GetArticle
    @apiGroup Articles

    @apiParam {Number} id ID for the article

    @apiSuccessStructure Article
    """
    def detail(self, pk):
        return RssArticle.objects.get(id=pk)

    """
    @api {post} /api/articles/ Create a new article
    @apiVersion 0.0.2
    @apiName PostArticle
    @apiGroup Articles

    @apiParam {Url} url URL for the article
    @apiParam {String} feed Name of the feed
    @apiParam {String} snippet Short extract or summary of the article
    @apiParam {Boolean} is_read Has the article been marked as read?

    @apiSuccessStructure Article
    """
    def create(self):
        return RssArticle.objects.create(
            url=self.data['url'],
            feed=RssFeed.objects.get(name=self.data['feed']),
            snippet=self.data['snippet'],
            is_read=self.data['is_read'],
        )

    """
    @api {put} /api/articles/:id Update an existing article
    @apiVersion 0.0.2
    @apiName UpdateArticle
    @apiGroup Articles

    @apiParam {Number} id ID for the article

    @apiParam {Url} url URL for the article
    @apiParam {String} feed Name of the feed
    @apiParam {String} snippet Short extract or summary of the article
    @apiParam {Boolean} is_read Has the article been marked as read?

    @apiSuccessStructure Article
    """
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

    """
    @api {delete} /api/articles/:id Delete an existing article
    @apiVersion 0.0.2
    @apiName DeleteArticle
    @apiGroup Articles

    @apiParam {Number} id ID for the article

    @apiSuccess (Success 204) empty No data returned
    """
    def delete(self, pk):
        RssArticle.objects.get(id=pk).delete()
