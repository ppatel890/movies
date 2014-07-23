# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Movie.audience_score'
        db.alter_column(u'tomatoes_movie', 'audience_score', self.gf('django.db.models.fields.SmallIntegerField')())

    def backwards(self, orm):

        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # Changing field 'Movie.audience_score'
        db.alter_column(u'tomatoes_movie', 'audience_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.SmallIntegerField', [], {}),
            'critic_rating': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tomatoes']