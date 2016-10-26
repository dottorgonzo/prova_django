# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'NewsTranslation.content'
        db.alter_column(u'montecatini_news_news_translation', 'content', self.gf('ckeditor.fields.RichTextField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'NewsTranslation.content'
        raise RuntimeError("Cannot reverse this migration. 'NewsTranslation.content' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'NewsTranslation.content'
        db.alter_column(u'montecatini_news_news_translation', 'content', self.gf('ckeditor.fields.RichTextField')())

    models = {
        u'montecatini_news.news': {
            'Meta': {'ordering': "('-ts_add',)", 'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_news.newstranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsTranslation', 'db_table': "u'montecatini_news_news_translation'"},
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_news.News']"}),
            'subtitle1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtitle2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_news']