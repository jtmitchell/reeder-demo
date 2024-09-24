from django.db import models


class RssFeed(models.Model):
    url = models.URLField(unique=True, db_index=True, default="")
    name = models.CharField(blank=True, default="", max_length=100)
    lastmodified = models.DateTimeField(editable=False, auto_now=True, db_index=True)

    def __str__(self):
        if self.name:
            return f"{self.name}"
        elif self.url:
            return f"RssFeed {self.url}"
        else:
            return f"RssFeed {self.pk}"


class RssArticle(models.Model):
    feed = models.ForeignKey(RssFeed, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, db_index=True, default="")
    snippet = models.CharField(max_length=500, default="", blank=True)
    is_read = models.BooleanField(default=True)
    lastmodified = models.DateTimeField(editable=False, auto_now=True, db_index=True)

    def __str__(self):
        if self.url:
            return f"{self.feed} {self.url} {self.snippet[:10]}"
        else:
            return f"RssArticle {self.pk}"

    class Meta:
        unique_together = ["feed", "url"]
