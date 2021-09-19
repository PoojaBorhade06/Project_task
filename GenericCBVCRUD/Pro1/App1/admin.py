from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','lap_name','company','batchno','ram','rom','weight','processor']

admin.site.register(Laptop,LaptopAdmin)