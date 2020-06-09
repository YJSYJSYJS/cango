from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # path('', RedirectView.as_view(url='/day/')),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]
