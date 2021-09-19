from django import forms
from .models import StudentContact

class StudentContactForm(forms.ModelForm):
    class Meta:
        model=StudentContact
        fields='__all__'

