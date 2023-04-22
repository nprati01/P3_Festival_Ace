from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festivals_index, name='index'),
    path('festivals/<int:festival_id>/', views.festivals_detail, name='detail'),
    path('add_festival/<int:festival_id>/', views.add_festival, name='add_festival'),
    path('myfestivals/', views.my_festivals_index, name='my_festivals_index'),
    path('myfestivals/<int:festival_id>/', views.my_festivals_detail, name='my_festivals_detail'),
    path('remove_festival/<int:festival_id>/', views.remove_festival, name='remove_festival'),
    path('myfestivals/<int:festival_id>/create_task/<int:my_festival>/', views.create_task, name='create_task'),
    path('myfestivals/<int:festival_id>/update/<int:pk>', views.TaskUpdate.as_view(), name='update_task'),
    path('myfestivals/<int:festival_id>/delete/<int:pk>', views.TaskDelete.as_view(), name='delete_task'),
    path('myfestivals/<int:festival_id>/create_suitcase/<int:my_festival>/', views.create_suitcase, name='create_suitcase'),
    path('myfestivals/<int:festival_id>/update_suitecase/<int:pk>', views.SuitcaseUpdate.as_view(), name='update_suitcase'),
    path('myfestivals/<int:festival_id>/delete_suitcase/<int:pk>', views.SuitcaseDelete.as_view(), name='delete_suitcase'),

]
