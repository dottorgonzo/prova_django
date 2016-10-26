# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'montecatini_ccn_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['montecatini_ccn.Category'])),
            ('premium', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'montecatini_ccn', ['Place'])

        # Adding model 'PlaceTranslation'
        db.create_table(u'montecatini_ccn_place_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['montecatini_ccn.Place'])),
        ))
        db.send_create_signal(u'montecatini_ccn', ['PlaceTranslation'])

        # Adding unique constraint on 'PlaceTranslation', fields ['language_code', 'master']
        db.create_unique(u'montecatini_ccn_place_translation', ['language_code', 'master_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PlaceTranslation', fields ['language_code', 'master']
        db.delete_unique(u'montecatini_ccn_place_translation', ['language_code', 'master_id'])

        # Deleting model 'Place'
        db.delete_table(u'montecatini_ccn_place')

        # Deleting model 'PlaceTranslation'
        db.delete_table(u'montecatini_ccn_place_translation')


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
        },
        u'montecatini_ccn.place': {
            'Meta': {'ordering': "('category__root', 'category')", 'object_name': 'Place'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['montecatini_ccn.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_ccn.placetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PlaceTranslation', 'db_table': "u'montecatini_ccn_place_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_ccn.Place']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_ccn']