from django import forms
from .models import Studentdata

class StudentdataForm(forms.ModelForm):
    class Meta:
        model=Studentdata
        fields='__all__'