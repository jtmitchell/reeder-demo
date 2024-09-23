from django.urls import include, path

from reeder.rssfeeds import api, views

urlpatterns = [
    path("", views.home, name="home"),
    path("put/<int:feed_id>/<str:article_url>/", views.put, name="feed_put"),
    path("get/<int:feed_id>/", views.get, name="feed_get"),
    path("delete/<int:feed_id>/", views.delete, name="feed_delete"),
    path("api/feeds/", include(api.RssFeedResource.urls())),
    path("api/articles/", include(api.RssArticleResource.urls())),
]
