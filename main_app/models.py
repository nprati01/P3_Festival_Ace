from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Festival(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    date = models.DateField('festival date')
    duration = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
            return self.name
