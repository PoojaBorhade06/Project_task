from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    template_name='App1/base.html'
    context={}
    return render(request,template_name,context)

@login_required(login_url='login')
def aboutus(request):
    template_name='App1/aboutus.html'
    context={}
    return render(request,template_name,context)


@login_required(login_url='login')
def contactus(request):
    template_name='App1/contactus.html'
    context={}
    return render(request,template_name,context)