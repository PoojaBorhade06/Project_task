from django.shortcuts import render,redirect
from django.contrib import messages
from .populate import *
from django.core.paginator import Paginator

# Create your views here.
def homeView(request):
    template_name='App1/base.html'
    context={}
    return render (request, template_name, context)


def addView(request):
    if request.method=='POST':
        n = request.POST.get('data')
        np = int(n)
        for i in range(np):
            rn = randint(1, 500)
            name = faker.name()
            marks = randint(1, 100)
            stu_record = Studentdata.objects.get_or_create(rn=rn, name=name, marks=marks)
        messages.success(request, 'Data Created Successfullyy...!!!!')
        return redirect('show')
    template_name='App1/add.html'
    return render (request,template_name)


def showView(request):
    st=Studentdata.objects.all()
    paginator = Paginator(st, 10)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'App1/show.html'
    context={'page_obj':page_obj}
    return render(request,template_name,context)

