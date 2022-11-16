from django.db import models
from django.utils import timezone

# the django.db has all functionalities to work with dbs
# the module 'models' has class models has lot of functionalities for storing a model obj in db
# retreiving, filtering  and etc...

# Create your models here.

# we are inherting our Genre class from the base model clss in django
# so django will take care ot storing the Genre obj in db

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)     # creating a relationship bw movie&genre
    date_created = models.DateField(default=timezone.now)  # we want default date time to be calculated at runtime
    # so we should pass the reference to the now function instead of calling that function
    # if we call the now() function the datetime will be hard coded 