from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    template_name='InventoryManagement/base.html'
    context={}
    return render(request,template_name,context)

@login_required(login_url='login')
def add(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='InventoryManagement/add.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def show(request):
    template_name = 'InventoryManagement/show.html'
    po=Product.objects.all()
    context = {'po': po}
    return render(request, template_name, context)

def update(request,idf):
    p=Product.objects.get(id=idf)
    form=ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'InventoryManagement/add.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete(request,idf):
    p = Product.objects.get(id=idf)
    p.delete()
    return redirect('show')