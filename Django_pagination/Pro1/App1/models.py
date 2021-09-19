from django.db import models

# Create your models here.

class StudentContact(models.Model):
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    mblno=models.BigIntegerField()
    