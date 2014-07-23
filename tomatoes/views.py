import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie, Favorite


def home(request):
    return render(request, 'tomatoes_base.html')


@csrf_exempt
def new_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score'],
            synopsis=data['synopsis']

        )

        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score,
            'synopsis': new_movie.synopsis
        }

        return HttpResponse(json.dumps(movie_info), content_type='application/json')



# Creates a record of favorited movie in database, returns a javascript object
@csrf_exempt
def new_movie_template(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critic_rating=data['critic_rating'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score'],
            synopsis=data['synopsis']
        )

        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score,
            'synopsis': new_movie.synopsis
        }

        return render_to_response('movie_template.html', movie_info)

# Sends the list of favorite movies to server, uses template to build the favorites page
@csrf_exempt
def favorites(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = {'movies': movies}
        return render_to_response('favorites.html', data)

# Deletes the selected movie, sends favorite movie list back
@csrf_exempt
def delete_favorite(request):
    if request.method == 'POST':
        movie_title = json.loads(request.body)
        movie = Movie.objects.get(title=movie_title).delete()
        movies = Movie.objects.all()
        data = {'movies': movies}

        return render_to_response('favorites.html', data)


def tinder(request):
    return render(request, 'tinder.html')


def new_favorite(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_favorite = Favorite.objects.create(
            title=data['title'],
            poster=data['poster'],
            identifier=data['identifier']
        )
