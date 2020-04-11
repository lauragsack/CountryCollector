from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Country, City, RiverCruise
from .forms import CountryForm, CityForm
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
    cruises_country_doesnt_have = RiverCruise.objects.exclude(id__in = country.cruises.all().values_list('id'))
    city_form = CityForm()
    return render(request, 'countries/detail.html', { 
        'country': country,
        'city_form': city_form,
        'cruises': cruises_country_doesnt_have
        })

def add_city(request, country_id):
    form = CityForm(request.POST)
    if form.is_valid():
        new_city = form.save(commit=False)
        new_city.country_id = country_id
        new_city.save()
    return redirect('detail', country_id=country_id)

def assoc_cruise(request, country_id, cruise_id):
    Country.objects.get(id=country_id).cruises.add(cruise_id)
    return redirect('detail', country_id=country_id)

def new_country(request):
  if request.method == 'POST':
    form = CountryForm(request.POST)
    if form.is_valid():
      country = form.save()
      return redirect('detail', country.id)
  else:
    form = CountryForm()
    context = { 'form': form }
  return render(request, 'countries/country_form.html', context)

def countries_update(request, country_id):
  # Select the cat that we're updating from the DB
  country = Country.objects.get(id=country_id)

  # If the request is a POST
  if request.method == "POST":
    form = CountryForm(request.POST, instance=country)
    if form.is_valid():
      country = form.save()
      return redirect('detail', country.id)
  # If not a POST, create the form
  else: 
    form = CountryForm(instance=country)
  # Render the form by sending the context to our existing template
  return render(request, 'countries/country_form.html', { 'form': form })

def countries_delete(request, country_id):
  Country.objects.get(id=country_id).delete()
  return redirect('index')



class CruiseList(ListView):
    model = RiverCruise

class CruiseDetail(DetailView):
    model = RiverCruise

class CruiseCreate(CreateView):
    model = RiverCruise
    fields = '__all__'

class CruiseUpdate(UpdateView):
    model = RiverCruise
    fields = ['name', 'type']

class CruiseDelete(DeleteView):
    model = RiverCruise
    success_url = '/cruises/'