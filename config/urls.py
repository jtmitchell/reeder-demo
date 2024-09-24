from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="feeds_home")),
    path("auth/", include("allauth.urls")),
    path("feeds/", include("reeder.rssfeeds.urls")),
    path("admin/", admin.site.urls),
]
