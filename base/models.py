from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book( models.Model ):
    name = models.CharField( max_length=50, null=False )
    author = models.CharField( max_length=50, null=False )
    genre = models.CharField( max_length=20, null=True )
    publish_year = models.IntegerField(max_length=4, null=True )
    def __str__(self):
        return self.name

