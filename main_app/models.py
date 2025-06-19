from django.db import models
from django.urls import reverse
# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)

class Cat(models.Model):
  name = models.CharField(max_length=100) # Text Box
  breed = models.CharField(max_length=100) # Text Box
  description = models.TextField(max_length=250) # Text Area
  age = models.IntegerField() # Int Field
  image = models.ImageField(upload_to='main_app/static/uploads', default="")

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})
  
  def __str__(self):
    return f"{self.name}"
  

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.cat} {self.get_meal_display()} on {self.date}"

