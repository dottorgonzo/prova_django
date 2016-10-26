# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlacePicture'
        db.create_table(u'montecatini_ccn_placepicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ts_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ts_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['montecatini_ccn.Place'])),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'montecatini_ccn', ['PlacePicture'])


    def backwards(self, orm):
        # Deleting model 'PlacePicture'
        db.delete_table(u'montecatini_ccn_placepicture')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'montecatini_ccn.placepicture': {
            'Meta': {'ordering': "('ts_add',)", 'object_name': 'PlacePicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['montecatini_ccn.Place']"}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_ccn.placetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PlaceTranslation', 'db_table': "u'montecatini_ccn_place_translation'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_ccn.Place']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_ccn']