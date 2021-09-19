from django.shortcuts import render,redirect
from .models import StudentContact
from .forms import StudentContactForm
from django.core.paginator import Paginator


# Create your views here.
def homeView(request):
    template_name='App1/base.html'
    context={}
    return render (request, template_name, context)


def addcontactView(request):
    form=StudentContactForm()
    if request.method=='POST':
        form=StudentContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='App1/add.html'
    context={'form':form}
    return render (request,template_name,context)


def showcontactView(request):
    ctn=StudentContact.objects.all()
    paginator = Paginator(ctn, 4)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'App1/show.html'
    context={'page_obj':page_obj}
    return render(request,template_name,context)













