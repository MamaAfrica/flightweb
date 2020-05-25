
from django.urls import path, re_path

from . import views
# app_name='products'
urlpatterns = [
    path('', views.flightIndex, name='flightIndex'),
    path('payment/', views.flightPayment, name='flightPayment'),

]
