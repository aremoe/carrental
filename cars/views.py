from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/all_cars.html', {'cars': cars})

def available_cars(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars/available_cars.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_cars')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Додати автомобіль'})

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Редагувати автомобіль'})