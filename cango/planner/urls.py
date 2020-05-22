from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='main'),
    path('month/', views.view_month, name='month'),
    path('week/', views.view_week, name='week'),
    # path('', views.post_list, name='post_list'),
    path('day/', views.day, name='day'),
    path('year/', views.year, name='year')
]
