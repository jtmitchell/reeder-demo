from django.urls import path

from rssfeeds import views

from .api import api

urlpatterns = [
    path("", views.home, name="feeds_home"),
    path("put/<int:feed_id>/<str:article_url>/", views.put, name="feed_put"),
    path("get/<int:feed_id>/", views.get, name="feed_get"),
    path("delete/<int:feed_id>/", views.delete, name="feed_delete"),
    path("api/feeds/", api.urls),
]
