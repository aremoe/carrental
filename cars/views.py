from django.core.paginator import Paginator
from datetime import timedelta
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RentalForm
from .models import Car, Rental, Favorite
from .forms import CarForm
from django.contrib import messages

def all_cars(request):
    car_list = Car.objects.all()
    paginator = Paginator(car_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cars/all_cars.html', {'page_obj': page_obj})
    
def available_cars(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars/available_cars.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    bookings = car.rentals.all()
    return render(request, 'cars/car_detail.html', {
        'car': car,
        'bookings': bookings
    })

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


def rent_car(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cars/rental_success.html')
    else:
        form = RentalForm()
    return render(request, 'cars/rent_car.html', {'form': form})

def is_car_available(car, start_date, end_date):
    overlapping_rentals = car.rentals.filter(
        start_date__lte=end_date,
        end_date__gte=start_date
    )
    return not overlapping_rentals.exists()

def rent_car(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['car']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if is_car_available(car, start_date, end_date):
                form.save()
                return render(request, 'cars/rental_success.html')
            else:
                messages.error(request, "Авто недоступне на вибрані дати.")
    else:
        form = RentalForm()

    return render(request, 'cars/rent_car.html', {'form': form})

@login_required
def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    Favorite.objects.get_or_create(user=request.user, car=car)
    return redirect('favorites_list')

@login_required
def remove_from_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    Favorite.objects.filter(user=request.user, car=car).delete()
    return redirect('favorites_list')

def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'cars/favorites.html', {'favorites': favorites})