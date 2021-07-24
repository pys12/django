from django.db import models
from django.urls import reverse

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

class Owner(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Adoption(models.Model):
  cat = models.ForeignKey(Cat,on_delete=models.CASCADE, default=1,related_name='cats')
  owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='owners')
  



  