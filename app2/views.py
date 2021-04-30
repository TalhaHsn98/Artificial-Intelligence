from django.shortcuts import render,HttpResponse
from app1.models import CosmoUser
from django.contrib import messages
import datetime



# Create your views here.
def cosmologincheck(request):
    if  request.method == "POST":
        print("hello post method")
        name = request.POST.get('loginid')
        pswd = request.POST.get('password')
        try:
            check = CosmoUser.objects.get(name=name, passwd=pswd)
            print(check)
            request.session['name'] = check.name
            request.session['id'] = check.id
            print(check.name)
            request.session['mail'] = check.mail
            print(check.mail)
            request.session['passwd'] = check.passwd
            print(check.passwd)
            print("getting session details")
            status = check.status
            print("session status created ",status)
            if status == "Activated":
               return render(request,'loggedin.html',{"s_obj":check})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request,'cosmologin.html',{"message": "invalied login"})

            return render(request,'loggedin.html')
        except Exception as e:
            print('Exception is ',str(e))
    return render(request,'cosmonauts/cosmologin.html',{"message" : "user under waiting state or invalied data "})
