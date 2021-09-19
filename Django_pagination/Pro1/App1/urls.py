from .import views
from django.urls import path

urlpatterns = [
    path('home/', views.homeView,name='home'),
    path('add/', views.addcontactView,name='add'),
    path('show/', views.showcontactView,name='show'),
]