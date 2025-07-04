from django.db import models
from django.core.validators import MinLengthValidator

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    fuel_consumption = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(9)])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.car}'