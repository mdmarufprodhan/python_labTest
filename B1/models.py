from django.db import models

# Create your models here.
from django.db.models import CharField


class Country(models.Model):
   name = models.CharField(max_length=100, default="")
   country_ID = models.IntegerField(default=0)
   area = models.CharField(max_length=500, default="")
   GDP = models.CharField(max_length=500, default="")
   urban = models.CharField(max_length=500, default="")


   def __str__(self):
       return self.name



