from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Provider','NameOfProduct','Price','Quantity','Amount',' Stock']

