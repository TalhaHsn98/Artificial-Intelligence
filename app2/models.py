from django.db import models


from app1.models  import *

class Cosmoresults(models.Model):
    cosmonaut=models.ForeignKey(CosmoUser,on_delete=models.CASCADE,blank=True,null=True)
    trainer=models.ForeignKey(CosmoTrainerdata,on_delete=models.CASCADE,blank=True,null=True)
    result=models.DecimalField(max_digits=10,decimal_places=2)

class CosmoFinalReport(models.Model):
    cosmonaut=models.ForeignKey(CosmoUser,on_delete=models.CASCADE,blank=True,null=True)
    avg=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

class CosmoFinalReports(models.Model):
    cosmonaut=models.ForeignKey(CosmoUser,on_delete=models.CASCADE,blank=True,null=True)
    avg=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)

class Cosmospaceresults(models.Model):
    cosmonaut=models.ForeignKey(CosmoUser,on_delete=models.CASCADE,blank=True,null=True)
    trainer=models.ForeignKey(CosmoTrainerdata,on_delete=models.CASCADE,blank=True,null=True)
    result=models.DecimalField(max_digits=10,decimal_places=2)

