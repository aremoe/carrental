from django.urls import path
from .models import Car
from . import views

urlpatterns = [
    path('', views.all_cars, name='all_cars'),
    path('rent/', views.rent_car, name='rent_car'),
    path('available/', views.available_cars, name='available_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    path('favorites/add/<int:car_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:car_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
