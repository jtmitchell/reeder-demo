# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RssFeed'
        db.create_table(u'rssfeeds_rssfeed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(default='', unique=True, max_length=200, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal(u'rssfeeds', ['RssFeed'])

        # Adding model 'RssArticle'
        db.create_table(u'rssfeeds_rssarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rssfeeds.RssFeed'])),
            ('url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, db_index=True)),
            ('snippet', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True)),
            ('is_read', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal(u'rssfeeds', ['RssArticle'])

        # Adding unique constraint on 'RssArticle', fields ['feed', 'url']
        db.create_unique(u'rssfeeds_rssarticle', ['feed_id', 'url'])


    def backwards(self, orm):
        # Removing unique constraint on 'RssArticle', fields ['feed', 'url']
        db.delete_unique(u'rssfeeds_rssarticle', ['feed_id', 'url'])

        # Deleting model 'RssFeed'
        db.delete_table(u'rssfeeds_rssfeed')

        # Deleting model 'RssArticle'
        db.delete_table(u'rssfeeds_rssarticle')


    models = {
        u'rssfeeds.rssarticle': {
            'Meta': {'unique_together': "(['feed', 'url'],)", 'object_name': 'RssArticle'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rssfeeds.RssFeed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'snippet': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'db_index': 'True'})
        },
        u'rssfeeds.rssfeed': {
            'Meta': {'object_name': 'RssFeed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['rssfeeds']