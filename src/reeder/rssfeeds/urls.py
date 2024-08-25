from django.urls import include, path

from .api import RssArticleResource, RssFeedResource

urlpatterns = [
    path("", "rssfeeds.views.home", name="home"),
    path("put/<int:feed_id>/<str:article_url>/", "rssfeeds.views.put", name="feed_put"),
    path("get/<int:feed_id>/", "rssfeeds.views.get", name="feed_get"),
    path("delete/<int:feed_id>/", "rssfeeds.views.delete", name="feed_delete"),
    path("api/feeds/", include(RssFeedResource.urls())),
    path("api/articles/", include(RssArticleResource.urls())),
]
