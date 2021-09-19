from django.contrib import admin
from .models import Studentdata

# Register your models here.
class StudentdataAdmin(admin.ModelAdmin):
    list_display = ['id','rn','name','marks']

admin.site.register(Studentdata,StudentdataAdmin)