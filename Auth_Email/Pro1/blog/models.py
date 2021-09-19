from django.db import models

# Create your models here.
class Post(models.Model):
    # udata = models.FileField(upload_to='media/')
    udata = models.ImageField(upload_to='media/')

