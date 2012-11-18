# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyProfile'
        db.create_table('my_profile_myprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aggregate_hotness', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('my_profile', ['MyProfile'])

        # Adding model 'Photo'
        db.create_table('my_profile_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['my_profile.MyProfile'])),
            ('hotness', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('my_profile', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'MyProfile'
        db.delete_table('my_profile_myprofile')

        # Deleting model 'Photo'
        db.delete_table('my_profile_photo')


    models = {
        'my_profile.myprofile': {
            'Meta': {'object_name': 'MyProfile'},
            'aggregate_hotness': ('django.db.models.fields.FloatField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'my_profile.photo': {
            'Meta': {'object_name': 'Photo'},
            'hotness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['my_profile.MyProfile']"})
        }
    }

    complete_apps = ['my_profile']