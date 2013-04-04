# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reeder.views.home', name='home'),
    url(r'^create/$', 'reeder.views.create', name='create'),
    url(r'^read/(?P<site_id>)/$', 'reeder.views.read', name='read'),
    url(r'^update/(?P<site_id>)/$', 'reeder.views.update', name='update'),
    url(r'^delete/(?P<site_id>)/$', 'reeder.views.delete', name='delete'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
