from django.db import models
from app1.models import *
from app2.models import *
class createexam(models.Model):
    trainername=models.ForeignKey(CosmoTrainerdata,blank=True,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField()
    title=models.CharField(max_length=40,unique=True)
    subjectname=models.CharField(max_length=40,blank=True,null=True)
    typeofexam=models.CharField(max_length=40,blank=True,null=True)


class examdata(models.Model):
    cosmonaut=models.ForeignKey(CosmoUser,blank=True,null=True,on_delete=models.CASCADE)
    trainer=models.ForeignKey(CosmoTrainerdata,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=40,blank=True,null=True)
    answer1=models.CharField(max_length=1000)
    answer2=models.CharField(max_length=1000)
    answer3=models.CharField(max_length=1000)
    answer4=models.CharField(max_length=1000)
    answer5=models.CharField(max_length=1000)

class spaceexamdata(models.Model):
    cosmonaut = models.ForeignKey(CosmoUser, blank=True, null=True, on_delete=models.CASCADE)
    trainer = models.ForeignKey(CosmoTrainerdata, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True, null=True)
    answer1 = models.CharField(max_length=1000)
    answer2 = models.CharField(max_length=1000)
    answer3 = models.CharField(max_length=1000)
    answer4 = models.CharField(max_length=1000)
    answer5 = models.CharField(max_length=1000)
    answer6 = models.CharField(max_length=1000)
    answer7 = models.CharField(max_length=1000)
    answer8 = models.CharField(max_length=1000)
    answer9 = models.CharField(max_length=1000)
    answer10= models.CharField(max_length=1000)

