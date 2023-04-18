from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festivals_index, name='festivals_index'),

    path('myfestivals/', views.my_festivals_index, name='my_festivals_index'),

]
