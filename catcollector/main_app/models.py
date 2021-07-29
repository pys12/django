from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Owner(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Adoption(models.Model):
  cat = models.ForeignKey(Cat,on_delete=models.CASCADE, default=1,related_name='cats')
  owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='owners')
  
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  # Create a cat_id FK
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']


  