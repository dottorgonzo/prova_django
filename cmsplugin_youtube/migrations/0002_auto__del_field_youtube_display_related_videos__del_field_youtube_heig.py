# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'YouTube.display_related_videos'
        db.delete_column('cmsplugin_youtube', 'display_related_videos')

        # Deleting field 'YouTube.height'
        db.delete_column('cmsplugin_youtube', 'height')

        # Deleting field 'YouTube.border'
        db.delete_column('cmsplugin_youtube', 'border')

        # Deleting field 'YouTube.allow_fullscreen'
        db.delete_column('cmsplugin_youtube', 'allow_fullscreen')

        # Deleting field 'YouTube.high_quality'
        db.delete_column('cmsplugin_youtube', 'high_quality')

        # Deleting field 'YouTube.width'
        db.delete_column('cmsplugin_youtube', 'width')

        # Deleting field 'YouTube.loop'
        db.delete_column('cmsplugin_youtube', 'loop')

        # Deleting field 'YouTube.autoplay'
        db.delete_column('cmsplugin_youtube', 'autoplay')


    def backwards(self, orm):
        # Adding field 'YouTube.display_related_videos'
        db.add_column('cmsplugin_youtube', 'display_related_videos',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'YouTube.height'
        db.add_column('cmsplugin_youtube', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=344),
                      keep_default=False)

        # Adding field 'YouTube.border'
        db.add_column('cmsplugin_youtube', 'border',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'YouTube.allow_fullscreen'
        db.add_column('cmsplugin_youtube', 'allow_fullscreen',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'YouTube.high_quality'
        db.add_column('cmsplugin_youtube', 'high_quality',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'YouTube.width'
        db.add_column('cmsplugin_youtube', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=425),
                      keep_default=False)

        # Adding field 'YouTube.loop'
        db.add_column('cmsplugin_youtube', 'loop',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'YouTube.autoplay'
        db.add_column('cmsplugin_youtube', 'autoplay',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_youtube.youtube': {
            'Meta': {'object_name': 'YouTube', 'db_table': "u'cmsplugin_youtube'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['cmsplugin_youtube']