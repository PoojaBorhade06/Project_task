from django.db import models

# Create your models here.
class Laptop(models.Model):
    lap_name=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    batchno=models.IntegerField()
    ram=models.IntegerField()
    rom=models.IntegerField()
    weight=models.FloatField()
    processor=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.company}'