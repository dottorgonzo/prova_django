# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoryTranslation'
        db.create_table(u'montecatini_ccn_category_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['montecatini_ccn.Category'])),
        ))
        db.send_create_signal(u'montecatini_ccn', ['CategoryTranslation'])

        # Adding unique constraint on 'CategoryTranslation', fields ['language_code', 'master']
        db.create_unique(u'montecatini_ccn_category_translation', ['language_code', 'master_id'])

        # Adding model 'Category'
        db.create_table(u'montecatini_ccn_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('root', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'montecatini_ccn', ['Category'])


    def backwards(self, orm):
        # Removing unique constraint on 'CategoryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'montecatini_ccn_category_translation', ['language_code', 'master_id'])

        # Deleting model 'CategoryTranslation'
        db.delete_table(u'montecatini_ccn_category_translation')

        # Deleting model 'Category'
        db.delete_table(u'montecatini_ccn_category')


    models = {
        u'montecatini_ccn.category': {
            'Meta': {'ordering': "('root',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'root': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_ccn.categorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CategoryTranslation', 'db_table': "u'montecatini_ccn_category_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_ccn.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_ccn']