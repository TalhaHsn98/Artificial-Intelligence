from django.shortcuts import render
from app1.models import CosmoTrainerdata


def trainerlogincheck(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        try:
            rosco=CosmoTrainerdata.objects.get(name=uname,passwd=pwd)
            request.session['trainer']=rosco.id
            print(rosco.id)
            request.session['rosconame']=rosco.name
            status=rosco.status
            print("status created",status)
            if status == 'Activated':
                return render(request,'trainers/trainerresult.html',{"t_obj":rosco})
            else:
                return render(request,"trainers/trainerlogin.html",{"message":"trainer under waiting list"})
        except Exception as f:
            print("exception is",str(f))
            return render(request,"trainers/trainerlogin.html",{"message":"Invalied credentials"})
    else:
        return render(request,"trainers/trainerlogin.html",{"message":"Invalied credentials"})



