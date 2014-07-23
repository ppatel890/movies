from django.contrib import admin
from tomatoes.models import Movie, Favorite

# Register your models here.

admin.site.register(Movie)
admin.site.register(Favorite)

