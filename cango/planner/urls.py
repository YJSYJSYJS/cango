from django.urls import path
from . import views


urlpatterns = [
    path('', views.day, name='day'),
    path('todo/', views.todo, name='todo'),
    path('month/', views.view_month, name='month'),
    path('week/', views.view_week, name='week'),
    path('day/', views.day, name='day'),
    path('year/', views.year, name='year'),
    path('enroll/', views.enroll, name='enroll'),
]
