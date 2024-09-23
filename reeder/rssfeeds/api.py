from ninja import NinjaAPI, Schema

from .auth import ApiCookieKey, ApiHeaderKey
from .models import RssArticle, RssFeed

api = NinjaAPI(auth=[ApiHeaderKey(), ApiCookieKey()])


class FeedSchema(Schema):
    id: int | None = None
    name: str = ""
    url: str = ""
    lastmodified: str = ""


class ArticleSchema(Schema):
    id: int | None = None
    feed: str = ""
    url: str = ""
    snippet: str = ""
    is_read: bool = False
    lastmodified: str = ""


@api.get("")
def feed_list(request) -> list[RssFeed]:
    return RssFeed.objects.all()


@api.get("/{pk}")
def feed_detail(request, pk: int) -> RssFeed | None:
    return RssFeed.objects.filter(id=pk).first()


@api.post("")
def feed_create(request, data: FeedSchema) -> RssFeed:
    return RssFeed.objects.create(
        url=data["url"],
        name=data["name"],
    )


@api.put("/{pk}")
def feed_update(request, pk: int, data: FeedSchema) -> RssFeed:
    feed, created = RssFeed.objects.get_or_create(
        id=pk,
        defaults=dict(name=data["name"], url=data["url"]),
    )
    if not created:
        feed.name = data["name"]
        feed.url = data["url"]
        feed.save()
    return feed


@api.delete("/{pk}")
def feed_delete(request, pk: int) -> None:
    RssFeed.objects.filter(id=pk).delete()


@api.get("/{feed_id}/article")
def article_list(request, feed_id: int) -> list[RssArticle]:
    return RssArticle.objects.filter(feed_id=feed_id)


@api.get("/{feed_id}/article/{pk}")
def article_detail(request, feed_id: int, pk: int) -> RssArticle:
    return RssArticle.objects.filter(feed_id=feed_id, pk=pk).first()


@api.post("/{feed_id}/article")
def article_create(request, feed_id: int, data: ArticleSchema) -> RssArticle | None:
    feed = RssFeed.objects.filter(pk=feed_id).first()
    if not feed:
        return None
    return RssArticle.objects.create(
        feed=feed,
        url=data["url"],
        snippet=data["snippet"],
        is_read=data["is_read"],
    )


@api.put("/{feed_id}/article/{pk}")
def article_update(request, feed_id: int, pk: int, data: ArticleSchema) -> RssArticle | None:
    feed = RssFeed.objects.filter(pk=feed_id).first()
    if not feed:
        return None

    article, created = RssArticle.objects.get_or_create(
        id=pk,
        feed=feed,
        defaults=dict(url=data["url"], snippet=data["snippet"], is_read=data["is_read"]),
    )

    if not created:
        article.url = data["url"]
        article.snippet = data["snippet"]
        article.is_read = data["is_read"]
        article.save()
    return article


@api.delete("/{feed_id}/article/{pk}")
def article_delete(request, feed_id: int, pk: int) -> None:
    RssArticle.objects.filter(feed_id=feed_id, id=pk).delete()
