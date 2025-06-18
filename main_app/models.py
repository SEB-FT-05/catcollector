from django.db import models

# Create your models here.

class Cat(models.Model):
  name = models.CharField(max_length=100) # Text Box
  breed = models.CharField(max_length=100) # Text Box
  description = models.TextField(max_length=250) # Text Area
  age = models.IntegerField() # Int Field
  image = models.ImageField(upload_to='main_app/static/uploads', default="")

