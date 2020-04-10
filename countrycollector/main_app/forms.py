from django import forms
from .models import Country, City

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'visited', 'language', 'continent']

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ['name', 'visited', 'what_to_eat']