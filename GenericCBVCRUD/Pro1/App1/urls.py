from django.urls import path
from.views import laptopListView,laptopCreateView,laptopUpdateView,laptopDeleteView

urlpatterns=[
    path('list/',laptopListView.as_view()),
    path('create/', laptopCreateView.as_view()),
    path('update/<int:pk>/', laptopUpdateView.as_view()),
    path('delete/<int:pk>/', laptopDeleteView.as_view())

]