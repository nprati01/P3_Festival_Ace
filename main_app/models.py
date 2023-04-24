
from django.db import models
from model_utils import Choices
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
        return f"{self.user.username}is user Festivals with Id {self.id}, "

class Task(models.Model):
     title = models.CharField(max_length=250)
     completed = models.BooleanField(default=False)
     due_date = models.DateField()
     festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
     my_festival = models.ForeignKey(MyFestival, on_delete=models.CASCADE)

     def __str__(self):
        return f"Festival Task {self.title} is due by {self.due_date}"

class Suitcase(models.Model):
     STATUS = Choices(
       ('I own this', ('I own this')),
       ('I need to purchase', ('I need to purchase this')),
       ('I will borrow', ('I am borrowing this')),
       )
     item_name = models.CharField(max_length=250)
     quantity = models.CharField(max_length=250)
     status = models.CharField(
          max_length=100,
          choices=STATUS,
          default=STATUS['I own this']

   )
     festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
     my_festival = models.ForeignKey(MyFestival, on_delete=models.CASCADE)
