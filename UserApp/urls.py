from django.urls import path
from UserApp import views

urlpatterns = [
    path('', views.homeview, name='homeView'),
]