from django.shortcuts import render
from .models import cats
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  # return HttpResponse('<h1>About the CatCollector</h1>')
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html', { 'cats': cats })