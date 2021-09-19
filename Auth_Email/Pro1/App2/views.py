from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import UserForm
from django.core.mail import send_mail

# Create your views here.
def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        e=request.POST.get('email')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            send_mail(
                'Thanku for login',
                'This is my message,it worked',
                '15poojab@gmail.com',
                [e],
                fail_silently=False,
            )
            return redirect('aboutus')
        else:
            messages.error(request,'Invalid credentials!!')
    template_name='App2/login.html'
    context={}
    return render(request,template_name,context)

def registerView(request):
    form=UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            e = request.POST.get('email')
            send_mail(
                'Thanku for register',
                'This is my message,it worked',
                '15poojab@gmail.com',
                [e],
                fail_silently=False,
            )

            return redirect('login')
    template_name = 'App2/register.html'
    context = {'form':form}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')

def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'password sucessfully changed')
            return redirect('aboutus')
        else:
            messages.success(request,'Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'App2/change_password.html', {
        'form': form
    })




