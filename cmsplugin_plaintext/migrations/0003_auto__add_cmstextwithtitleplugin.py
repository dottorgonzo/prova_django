# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CMSTextWithTitlePlugin'
        db.create_table(u'cmsplugin_cmstextwithtitleplugin', (
            (u'text_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['djangocms_text_ckeditor.Text'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cmsplugin_plaintext', ['CMSTextWithTitlePlugin'])


    def backwards(self, orm):
        # Deleting model 'CMSTextWithTitlePlugin'
        db.delete_table(u'cmsplugin_cmstextwithtitleplugin')


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
        u'cmsplugin_plaintext.cmscharfieldplugin': {
            'Meta': {'object_name': 'CMSCharFieldPlugin', 'db_table': "u'cmsplugin_cmscharfieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cmsplugin_plaintext.cmsemailfieldplugin': {
            'Meta': {'object_name': 'CMSEmailFieldPlugin', 'db_table': "u'cmsplugin_cmsemailfieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cmsplugin_plaintext.cmsgeopositionfieldplugin': {
            'Meta': {'object_name': 'CMSGeoPositionFieldPlugin', 'db_table': "u'cmsplugin_cmsgeopositionfieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'cmsplugin_plaintext.cmsphonefieldplugin': {
            'Meta': {'object_name': 'CMSPhoneFieldPlugin', 'db_table': "u'cmsplugin_cmsphonefieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cmsplugin_plaintext.cmstextfieldplugin': {
            'Meta': {'object_name': 'CMSTextFieldPlugin', 'db_table': "u'cmsplugin_cmstextfieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cmsplugin_plaintext.cmstextwithtitleplugin': {
            'Meta': {'object_name': 'CMSTextWithTitlePlugin', 'db_table': "u'cmsplugin_cmstextwithtitleplugin'", '_ormbases': [u'djangocms_text_ckeditor.Text']},
            u'text_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['djangocms_text_ckeditor.Text']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsplugin_plaintext.cmsurlfieldplugin': {
            'Meta': {'object_name': 'CMSURLFieldPlugin', 'db_table': "u'cmsplugin_cmsurlfieldplugin'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'djangocms_text_ckeditor.text': {
            'Meta': {'object_name': 'Text', 'db_table': "u'cmsplugin_text'", '_ormbases': ['cms.CMSPlugin']},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['cmsplugin_plaintext']