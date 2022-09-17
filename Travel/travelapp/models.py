from django.db import models

# Create your models here.
class demoapp_place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class people(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='people')
    desc=models .TextField()

def __str__(self):
    return self.name