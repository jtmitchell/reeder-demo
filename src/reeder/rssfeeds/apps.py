"""
App configuration for RSS Feeds.
"""

from django.apps import AppConfig


class RssFeedsConfig(AppConfig):
    """
    App configuration for RSS Feeds.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "rssfeeds"
    verbose_name = "RSS Feeds"
