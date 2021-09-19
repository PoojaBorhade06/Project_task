
from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.homeView,name='home'),
    path('add/',views.addView,name='add'),
    path('show/',views.showView,name='show')
]
