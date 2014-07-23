# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Favorite'
        db.create_table(u'tomatoes_favorite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('poster', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tomatoes', ['Favorite'])


    def backwards(self, orm):
        # Deleting model 'Favorite'
        db.delete_table(u'tomatoes_favorite')


    models = {
        u'tomatoes.favorite': {
            'Meta': {'object_name': 'Favorite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.SmallIntegerField', [], {}),
            'critic_rating': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'synopsis': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tomatoes']