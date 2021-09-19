from django.urls import path
from .import views

urlpatterns = [
    path('img/',views.imgView,name='img'),
    path('show/',views.showImgView ,name='show')


]
