# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PointOfInterestTranslation'
        db.create_table(u'montecatini_metro_pointofinterest_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['montecatini_metro.PointOfInterest'])),
        ))
        db.send_create_signal(u'montecatini_metro', ['PointOfInterestTranslation'])

        # Adding unique constraint on 'PointOfInterestTranslation', fields ['language_code', 'master']
        db.create_unique(u'montecatini_metro_pointofinterest_translation', ['language_code', 'master_id'])

        # Adding model 'PointOfInterest'
        db.create_table(u'montecatini_metro_pointofinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poi_content', null=True, to=orm['cms.Placeholder'])),
            ('subcontent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poi_subcontent', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal(u'montecatini_metro', ['PointOfInterest'])


    def backwards(self, orm):
        # Removing unique constraint on 'PointOfInterestTranslation', fields ['language_code', 'master']
        db.delete_unique(u'montecatini_metro_pointofinterest_translation', ['language_code', 'master_id'])

        # Deleting model 'PointOfInterestTranslation'
        db.delete_table(u'montecatini_metro_pointofinterest_translation')

        # Deleting model 'PointOfInterest'
        db.delete_table(u'montecatini_metro_pointofinterest')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'montecatini_metro.pointofinterest': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PointOfInterest'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poi_content'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'subcontent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poi_subcontent'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_metro.pointofinteresttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PointOfInterestTranslation', 'db_table': "u'montecatini_metro_pointofinterest_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_metro.PointOfInterest']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_metro']