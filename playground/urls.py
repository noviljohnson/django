from django.urls import path
from . import views

# urlconfig
urlpatterns = [     # django looks for this variable
    path('hello/', views.say_hello)          # set this to an url patters objects, use path() 
]