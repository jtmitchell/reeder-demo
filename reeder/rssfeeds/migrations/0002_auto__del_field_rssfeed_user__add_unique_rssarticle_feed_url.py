# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RssFeed.user'
        db.delete_column('reeder_rssfeed', 'user_id')

        # Adding unique constraint on 'RssArticle', fields ['feed', 'url']
        db.create_unique('reeder_rssarticle', ['feed_id', 'url'])


    def backwards(self, orm):
        # Removing unique constraint on 'RssArticle', fields ['feed', 'url']
        db.delete_unique('reeder_rssarticle', ['feed_id', 'url'])

        # Adding field 'RssFeed.user'
        db.add_column('reeder_rssfeed', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']),
                      keep_default=False)


    models = {
        'reeder.rssarticle': {
            'Meta': {'unique_together': "(['feed', 'url'],)", 'object_name': 'RssArticle'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reeder.RssFeed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'snippet': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'db_index': 'True'})
        },
        'reeder.rssfeed': {
            'Meta': {'object_name': 'RssFeed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['reeder']