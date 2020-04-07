from django.shortcuts import render
from django.http import HttpResponse

class Country:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

countries = [
  Country('Lolo', 'tabby', 'foul little demon', 3),
  Country('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Country('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def countries_index(request):
    return render(request, 'countries/index.html', { 'countries': countries })