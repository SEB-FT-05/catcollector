from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.

class CatCreate(CreateView):
  model = Cat
  # fields = '__all__'
  fields = ['name', 'breed', 'description', 'age', 'image']
  # success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

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
  # return HttpResponse('<h1> Cat Collector </h1>')
    return render(request, 'home.html')


def about(request):
  # return HttpResponse('<h1>About the Cat Collector </h1>')
  return render(request, 'about.html')

def cats_index(request):
  # SELECT * FROM 'main_app_cat';
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats})

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', 
                {'cat': cat, 
                'feeding_form': feeding_form
                })
