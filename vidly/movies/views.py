from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

def index(request):   # defines main page of an app
    
    movies = Movie.objects.all()
    # # select * from movies_movie
    # output = ', '.join([m.title for m in movies])
    # Movie.objects.filter(release_year=2000)
    # # select * from movies_movie where ....
    # Movie.objects.get(id=1)


    return render(request, 'movies/index.html',{'movies':movies})
    # return HttpResponse(output)
    # return HttpResponse("Hello world")

# def detail(request, movie_id):
#     try:
#         movie = Movie.objects.get(pk=movie_id)#id=movie_id)
#         return render(request,'movies/detail.html',{'movie':movie})
#         # return HttpResponse(movie_id)
#     except Movie.DoesNotExist:
#         raise Http404()

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/detail.html',{'movie':movie})