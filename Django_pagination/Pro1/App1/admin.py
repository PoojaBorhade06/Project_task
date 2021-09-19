from django.contrib import admin
from .models import StudentContact

# Register your models here.
class StudentContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','mblno']

admin.site.register(StudentContact,StudentContactAdmin)