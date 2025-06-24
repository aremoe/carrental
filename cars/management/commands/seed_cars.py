from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):
    help = "Заповнення бази початковими автомобілями"

    def handle(self, *args, **kwargs):
        Car.objects.all().delete()
        cars = [
            {"brand": "Toyota", "model": "Camry", "year": 2020, "price_per_day": 50, "available": True, "fuel_consumption": 7.2, "color": "Чорний"},
            {"brand": "Tesla", "model": "Model 3", "year": 2022, "price_per_day": 80, "available": False, "fuel_consumption": 0, "color": "Білий"},
            {"brand": "BMW", "model": "X5", "year": 2021, "price_per_day": 100, "available": True, "fuel_consumption": 9.5, "color": "Сірий"},
        ]
        for car_data in cars:
            Car.objects.create(**car_data)
        self.stdout.write(self.style.SUCCESS("Дані додано"))
