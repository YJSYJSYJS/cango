from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_main, name='guide_main')
]
