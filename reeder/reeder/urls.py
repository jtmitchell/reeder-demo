# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from rssfeeds.api import RssFeedResource, RssArticleResource


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rssfeeds.views.home', name='home'),
    url(r'^put/(?P<feed_id>\d+)/(?P<article_url>.+)/$', 'rssfeeds.views.put', name='feed_put'),
    url(r'^get/(?P<feed_id>\d+)/$', 'rssfeeds.views.get', name='feed_get'),
    url(r'^delete/(?P<feed_id>\d+)/$', 'rssfeeds.views.delete', name='feed_delete'),

    url(r'api/feeds/', include(RssFeedResource.urls())),
    url(r'api/articles/', include(RssArticleResource.urls())),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
