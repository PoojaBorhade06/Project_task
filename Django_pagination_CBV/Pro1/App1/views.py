from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import StudentContact

class ContactListView(ListView):
    paginate_by = 2
    model = StudentContact

class addView(CreateView):
    model=StudentContact
    fields='__all__'
    success_url = '/App1/show'