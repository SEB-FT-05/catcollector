from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

# Create your views here.

# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

def home(request):
  return HttpResponse('<h1> Cat Collector </h1>')

def about(request):
  # return HttpResponse('<h1>About the Cat Collector </h1>')
  return render(request, 'about.html')

def cats_index(request):
  # SELECT * FROM 'main_app_cat';
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})
