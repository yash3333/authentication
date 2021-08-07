from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    id =  models.AutoField(primary_key=True)
    age = models.IntegerField()
    companyname = models.CharField(max_length=50)
