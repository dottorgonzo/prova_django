# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubContentTranslation'
        db.create_table(u'montecatini_metro_subcontent_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['montecatini_metro.SubContent'])),
        ))
        db.send_create_signal(u'montecatini_metro', ['SubContentTranslation'])

        # Adding unique constraint on 'SubContentTranslation', fields ['language_code', 'master']
        db.create_unique(u'montecatini_metro_subcontent_translation', ['language_code', 'master_id'])

        # Adding model 'SubContent'
        db.create_table(u'montecatini_metro_subcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('poi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['montecatini_metro.PointOfInterest'])),
            ('ordering', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'montecatini_metro', ['SubContent'])

        # Deleting field 'PointOfInterest.subcontent'
        db.delete_column(u'montecatini_metro_pointofinterest', 'subcontent_id')

        # Adding field 'PointOfInterestTranslation.mp3'
        db.add_column(u'montecatini_metro_pointofinterest_translation', 'mp3',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'SubContentTranslation', fields ['language_code', 'master']
        db.delete_unique(u'montecatini_metro_subcontent_translation', ['language_code', 'master_id'])

        # Deleting model 'SubContentTranslation'
        db.delete_table(u'montecatini_metro_subcontent_translation')

        # Deleting model 'SubContent'
        db.delete_table(u'montecatini_metro_subcontent')

        # Adding field 'PointOfInterest.subcontent'
        db.add_column(u'montecatini_metro_pointofinterest', 'subcontent',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='poi_subcontent', null=True, to=orm['cms.Placeholder']),
                      keep_default=False)

        # Deleting field 'PointOfInterestTranslation.mp3'
        db.delete_column(u'montecatini_metro_pointofinterest_translation', 'mp3')


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
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_metro.pointofinteresttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PointOfInterestTranslation', 'db_table': "u'montecatini_metro_pointofinterest_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_metro.PointOfInterest']"}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'montecatini_metro.subcontent': {
            'Meta': {'object_name': 'SubContent'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'poi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['montecatini_metro.PointOfInterest']"}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_metro.subcontenttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SubContentTranslation', 'db_table': "u'montecatini_metro_subcontent_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_metro.SubContent']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_metro']