from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tomatoes.views.home', name='home'),
    url(r'^new_movie/$', 'tomatoes.views.new_movie', name='new_movie'),
    url(r'^new_movie_template/$', 'tomatoes.views.new_movie_template', name='new_movie_template'),
    url(r'^favorites/$', 'tomatoes.views.favorites', name='favorites'),
    url(r'^delete_favorite/$', 'tomatoes.views.delete_favorite', name='delete_favorite'),

    url(r'^tinder/$', 'tomatoes.views.tinder', name='tinder'),
    url(r'^new_favorite/$', 'tomatoes.views.new_favorite', name='new_favorite'),

)
