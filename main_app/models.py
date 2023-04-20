from django.db import models
from datetime import date
from django.urls import reverse
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

class MyFestival(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    festivals = models.ManyToManyField(Festival)
    def __str__(self):
        return f"{self.user.username}'s Festivals"

class Tasks(models.Model):
     title = models.CharField(max_length=250)
     completed = models.BooleanField()
     due_date = models.DateField()

     def __str__(self):
        return f"Festival Tasks {self.title}'s "
