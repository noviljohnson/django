from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):   # defines main page of an app
    
    movies = Movie.objects.all()
    # # select * from movies_movie
    output = ', '.join([m.title for m in movies])
    # Movie.objects.filter(release_year=2000)
    # # select * from movies_movie where ....
    # Movie.objects.get(id=1)

    return HttpResponse(output)
    # return HttpResponse("Hello world")

