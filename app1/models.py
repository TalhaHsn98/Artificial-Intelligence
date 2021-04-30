

from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class CosmoUser(models.Model):
    name=models.CharField(max_length=40)
    uid=models.CharField(max_length=20)
    mail=models.EmailField(unique=True)
    passwd=models.CharField(max_length=40)
    cwpasswd=models.CharField(max_length=40)
    mobileno=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.mail
    class Meta:
        db_table = 'cosmouser'

class CosmoTrainerdata(models.Model):
    name=models.CharField(max_length=40)
    uid=models.CharField(max_length=30)
    mail=models.EmailField()
    passwd=models.CharField(max_length=30)
    qualification=models.CharField(max_length=20)
    mobileno=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    Experience=models.CharField(max_length=40)
    authkey=models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.mail
    class Meta:
        db_table = 'cosmotrainerdata'









