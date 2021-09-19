from django.urls import path
from .import views

urlpatterns=[
    path('h/',views.home,name='h'),
    path('add/',views.add,name='add'),
    path('show/',views.show,name='show'),
    path('up/<int:idf>/',views.update,name='up'),
    path('de/<int:idf>/',views.delete,name='de'),

]

