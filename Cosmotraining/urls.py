"""Cosmotraining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app1.views import index1,cosmologin,trainerresult,cosmohome,cosmoregistration,trainerlogin,trainerregister,cosmonautdetails,cosmonautresults,adminindex,adminsignin,adminloginentered,adminindex,viewadmincosmonautdata,activatecosmonauts,viewadmintrainerdata,activatetrainers,logout,finalreport,activate,savestudentres,updatestudentres,getavailbaleexams,trainingprocess,techinicalresult,cosmonautresults1,createexam1,saveres1,finalreport1,spacecraftexam,spacecraftresult,saveres2,spacereport1,sendoffer
from app2.views import cosmologincheck
from trainer.views import trainerlogincheck

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home/',index1,name="index1"),
    #url('', index1, name="index1"),
    url(r'^cosmologin/',cosmologin,name="cosmologin"),
    url(r'^cosmologincheck/',cosmologincheck,name="cosmologincheck"),
    url(r'^cosmoregistration/',cosmoregistration,name="cosmoregistration"),
    url(r'^trainerlogin/',trainerlogin,name="trainerlogin"),
    url(r'^trainerregister/',trainerregister,name='trainerregister'),
    url(r'^trainerresult/',trainerresult,name='trainerresult'),
    url(r'^cosmonautdetails/',cosmonautdetails,name='cosmonautdetails'),
    url(r'^cosmonautresults/',cosmonautresults,name='cosmonautresults'),
    url(r'^cosmohome/',cosmohome,name='cosmohome'),
    url(r'^adminsignin/',adminsignin,name='adminsignin'),
    url(r'^adminloginentered/',adminloginentered,name='adminloginentered'),
    url(r'^adminindex/',adminindex,name='adminindex'),
    url(r'^viewadmincosmonautdata/',viewadmincosmonautdata,name='viewadmincosmonautdata'),
    url(r'^activatecosmonauts/',activatecosmonauts,name='activatecosmonauts'),
    url(r'^trainerlogincheck/',trainerlogincheck,name='trainerlogincheck'),
    url(r'^viewadmintrainerdata/',viewadmintrainerdata,name='viewadmintrainerdata'),
    url(r'^activatetrainers/',activatetrainers,name='activatetrainers'),
    url(r'^logout/',logout,name='logout'),
    url(r'trainingprocess/',trainingprocess,name='trainingprocess'),
    url('saveres/', savestudentres, name='savestures'),
    url('updateres/', updatestudentres, name='updatestures'),
    url('finalreport/', finalreport, name='finalreport'),
    url('activate/', activate, name='activate'),
    url(r'techinicalresult/',techinicalresult,name='techinicalresult'),
    url(r'cosmonautresults1/',cosmonautresults1,name='cosmonautresults1'),
    url(r'createexam/',createexam1,name='createexam'),
    url(r'saveres1/',saveres1,name='saveres1'),
    url(r'finalreport1',finalreport1,name='finalreport1'),
    url(r'spacecraftexam',spacecraftexam,name='spacecraftexam'),
    url(r'^getavailbaleexams/',getavailbaleexams,name='getavailbaleexams'),
    url(r'^spacecraftresult/',spacecraftresult,name='spacecraftresult'),
    url(r'saveres2/',saveres2,name='saveres1'),
    url(r'^spacereport1/',spacereport1,name='spacereport1'),
    url(r'^sendoffer/',sendoffer,name='sendoffer'),


]
