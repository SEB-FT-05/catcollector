from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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

  # Exclude those toys ids which exists in cat_toys join table with the current cat id.
  # Remaining toys ids will be returned to toys_cat_doesnt_have.
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

  return render(request, 'cats/detail.html', 
                {'cat': cat, 
                'feeding_form': feeding_form,
                'toys': toys_cat_doesnt_have
                })

def add_feeding(request, cat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)


class ToyList(ListView):
  model = Toy 

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy 
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'


def assoc_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id = cat_id)

def unassoc_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.remove(toy_id)
  return redirect('detail', cat_id = cat_id)