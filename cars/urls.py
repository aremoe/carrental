from django.urls import path
from .models import Car
from . import views

urlpatterns = [
    path('', views.all_cars, name='all_cars'),
    path('rent/', views.rent_car, name='rent_car'),
    path('available/', views.available_cars, name='available_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('<int:car_id>/edit/', views.edit_car, name='edit_car'),
]
