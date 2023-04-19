from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festivals_index, name='index'),
    path('festivals/<int:festival_id>/', views.festivals_detail, name='detail'),
    path('add_festival/<int:festival_id>/', views.add_festival, name='add_festival'),
    path('myfestivals/', views.my_festivals_index, name='my_festivals_index'),

]
