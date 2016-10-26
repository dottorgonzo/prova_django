# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsTranslation'
        db.create_table(u'montecatini_news_news_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtitle1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtitle2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['montecatini_news.News'])),
        ))
        db.send_create_signal(u'montecatini_news', ['NewsTranslation'])

        # Adding unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.create_unique(u'montecatini_news_news_translation', ['language_code', 'master_id'])

        # Adding model 'News'
        db.create_table(u'montecatini_news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'montecatini_news', ['News'])


    def backwards(self, orm):
        # Removing unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.delete_unique(u'montecatini_news_news_translation', ['language_code', 'master_id'])

        # Deleting model 'NewsTranslation'
        db.delete_table(u'montecatini_news_news_translation')

        # Deleting model 'News'
        db.delete_table(u'montecatini_news_news')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'montecatini_news.news': {
            'Meta': {'ordering': "('order',)", 'object_name': 'News'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_news.newstranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsTranslation', 'db_table': "u'montecatini_news_news_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_news.News']"}),
            'subtitle1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtitle2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_news']