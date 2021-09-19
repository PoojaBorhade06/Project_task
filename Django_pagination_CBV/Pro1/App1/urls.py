
from django.urls import path
from .views import ContactListView,addView
urlpatterns = [
    path('show/',ContactListView.as_view()),
    path('create/',addView.as_view())
]
