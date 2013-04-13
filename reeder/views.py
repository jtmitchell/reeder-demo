# -*- coding: utf-8 -*-
from django.shortcuts import render
import json

from models import RssFeed, RssArticle

import logging
log = logging.getLogger(__name__)

def home(request):
    context = {}
    conext['feeds'] = RssFeed.objects.all()
    return (request,'reeder/home.html',context)

def put(request, feed_id, article_url):
    status = {'success': True, 'feed': '', 'article': ''}

    try:
        feed, new_feed = RssFeed.objects.get_or_create(pk=feed_id)
        status['feed'] = 'created' if new_feed else 'updated'
    
        article, new_article = RssArticle.objects.get_or_create(url=article_url, feed=feed)
        status['article'] = 'created' if new_article else 'updated'
    except Exception, e:
        status['success'] = False
        status['error'] = e
        
    return json.dumps(status)
    
def get(request, feed_id):
    return_value = []

    feed = RssFeed.objects.get(pk=feed_id)
    if feed:
        for article in RssArticle.objects.filter(feed=feed):
            return_value.append(article)
            
    return json.dumps(return_value)

def delete(request, feed_id):
    status = {'success': False}
    if RssFeed.objects.get(pk=feed_id).delete():
        status['success'] = True
    return json.dumps(status)

