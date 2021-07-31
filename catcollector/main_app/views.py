from django.shortcuts import render,redirect
from .models import Cat,Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .forms import FeedingForm

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name','breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

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
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form,
    'toys': toys_cat_doesnt_have
  })

def add_feeding(request, cat_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
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