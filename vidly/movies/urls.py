# crete varable: objects that map url endpoints or view functions
# we use path function from django

from django.urls import path
from . import views
# import views -- this is not a good way of importing views module 
# doesn't work in django - but works in pure python world
# if import like that there is a proble - this urls.py is dependent on views module in path module
# so we should use relative import statement 

# example url endpoints
# movies/
# movies/1/details

# use relative urls
# url config

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),           # empty string in first arg is root of the app
    path('<int:movie_id>', views.detail, name='detail')
]