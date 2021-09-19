from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def imgView(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=PostForm()
    template_name = 'blog/blog.html'
    context = {'form':form }
    return render(request, template_name, context)

def showImgView(request):
    po = Post.objects.all()
    print(po[0])
    print(type(po[0]),'\n',dir(po[0]))
    # print('type of po[0].udata.url=',type(po[0].udata.url))
    # print('value of po[0].udata.url=',po[0].udata.url)
    template_name='blog/showimg.html'
    context={'po':po}
    return render(request,template_name,context)
