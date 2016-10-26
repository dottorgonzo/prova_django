# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Picture'
        db.create_table(u'montecatini_metro_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('poi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['montecatini_metro.PointOfInterest'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ordering', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'montecatini_metro', ['Picture'])

        # Adding field 'PointOfInterestTranslation.youtube_id'
        db.add_column(u'montecatini_metro_pointofinterest_translation', 'youtube_id',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table(u'montecatini_metro_picture')

        # Deleting field 'PointOfInterestTranslation.youtube_id'
        db.delete_column(u'montecatini_metro_pointofinterest_translation', 'youtube_id')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'montecatini_metro.picture': {
            'Meta': {'ordering': "('poi', 'ordering')", 'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'poi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['montecatini_metro.PointOfInterest']"}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['montecatini_metro']