from django import forms
from .models import Car
from .models import Rental

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'name', 'email', 'phone', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }