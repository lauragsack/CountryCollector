from django.shortcuts import render
from .models import Country
from .forms import CityForm
# Create your views here.
def home(request):
  return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

def countries_index(request):
    countries = Country.objects.all()
    return render(request, 'countries/index.html', { 'countries': countries })

def countries_detail(request, country_id):
    country = Country.objects.get(id = country_id)
    city_form = CityForm()
    return render(request, 'countries/detail.html', { 
        'country': country,
        'city_form': city_form
        })