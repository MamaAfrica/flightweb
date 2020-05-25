from django.urls import path

from . import views

# app_name='search'
urlpatterns = [
    path('', views.flightResult, name='flightResult'),
# path('result/', views.flightResult, name='flightResult'),
    ]

