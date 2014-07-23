from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()
    critic_rating = models.SmallIntegerField()
    poster = models.URLField()
    mpaa_rating = models.CharField(max_length=10)
    runtime = models.PositiveSmallIntegerField()
    audience_score = models.SmallIntegerField()
    synopsis = models.TextField(null=True)

    def __unicode__(self):
        return self.title


class Favorite(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField()
    identifier = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title
