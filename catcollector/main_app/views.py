from django.shortcuts import render
from .models import Cat

from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  # return HttpResponse('<h1>About the CatCollector</h1>')
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })