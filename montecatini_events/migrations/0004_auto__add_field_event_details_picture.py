# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.details_picture'
        db.add_column(u'montecatini_events_event', 'details_picture',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.details_picture'
        db.delete_column(u'montecatini_events_event', 'details_picture')


    models = {
        u'montecatini_events.event': {
            'Meta': {'ordering': "('-ts_add',)", 'object_name': 'Event'},
            'details_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ts_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ts_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'montecatini_events.eventtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventTranslation', 'db_table': "u'montecatini_events_event_translation'"},
            'content': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['montecatini_events.Event']"}),
            'subtitle1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtitle2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['montecatini_events']