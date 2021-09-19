from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Laptop

# Create your views here.

class laptopListView(ListView):
    model=Laptop

class laptopCreateView(CreateView):
    model=Laptop
    fields='__all__'
    success_url='/App1/list/'


class laptopUpdateView(UpdateView):
    model=Laptop
    fields='__all__'
    success_url='/App1/list/'

class laptopDeleteView(DeleteView):
    model=Laptop
    success_url='/App1/list/'