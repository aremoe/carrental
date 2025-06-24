from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Car

def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/all_cars.html', {'cars': cars})

def available_cars(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars/available_cars.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})
