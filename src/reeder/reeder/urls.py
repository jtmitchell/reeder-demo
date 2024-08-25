from django.contrib import admin
from django.urls import include, path

urlpatterns = [path(r"^admin/", include(admin.site.urls)), path("feeds/", include("rssfeeds.urls"))]
