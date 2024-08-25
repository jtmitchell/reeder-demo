from django.conf.urls.defaults import include, patterns, url
from rssfeeds.api import RssArticleResource, RssFeedResource

urlpatterns = patterns(
    "",
    url(r"^$", "rssfeeds.views.home", name="home"),
    url(r"^put/(?P<feed_id>\d+)/(?P<article_url>.+)/$", "rssfeeds.views.put", name="feed_put"),
    url(r"^get/(?P<feed_id>\d+)/$", "rssfeeds.views.get", name="feed_get"),
    url(r"^delete/(?P<feed_id>\d+)/$", "rssfeeds.views.delete", name="feed_delete"),
    url(r"api/feeds/", include(RssFeedResource.urls())),
    url(r"api/articles/", include(RssArticleResource.urls())),
)
