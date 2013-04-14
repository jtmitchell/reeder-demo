# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reeder.views.home', name='home'),
    url(r'^put/(?P<feed_id>\d+)/(?P<article_url>.+)/$', 'reeder.views.put', name='feed_put'),
    url(r'^get/(?P<feed_id>\d+)/$', 'reeder.views.get', name='feed_get'),
    url(r'^delete/(?P<feed_id>\d+)/$', 'reeder.views.delete', name='feed_delete'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
