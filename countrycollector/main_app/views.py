from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Country, City, RiverCruise
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

def add_city(request, country_id):
    form = CityForm(request.POST)
    if form.is_valid():
        new_city = form.save(commit=False)
        new_city.country_id = country_id
        new_city.save()
    return redirect('detail', country_id=country_id)



class CruiseList(ListView):
    model = RiverCruise

class CruiseDetail(DetailView):
    model = RiverCruise

class CruiseCreate(CreateView):
    model = RiverCruise
    fields = '__all__'

class CruiseUpdate(UpdateView):
    model = RiverCruise
    fiels = ['name', 'type']

class CruiseDelete(DeleteView):
    model = RiverCruise
    success_url = '/cruises/'