from django.http import HttpResponse
from django.shortcuts import render
from .forms import CosmoForm,CosmoTrainerdataForm,CosmoTrainerdata
from random import randint
from trainer.models import *
from trainer.forms import *
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from app1 import forms
from .models import *
from app2.models import *
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

def index1(request):
    return render(request,"index1.html")
def cosmologin(request):
    return render(request,"cosmonauts/cosmologin.html")


def trainerresult(request):
    trainerobj=CosmoTrainerdata.objects.get(id=request.GET['id'])
    return render(request,"trainers/trainerresult.html",{"t_obj":trainerobj})
def cosmohome(request):
    return render(request,"loggedin.html",{})


def cosmoregistration(request):
    if request.method == "POST":
        form=CosmoForm(request.POST)
        status=request.POST.get('status')
        print(status)

        if form.is_valid():
                form.save()
        else:
            print("Cosmo User form not valied")
        return HttpResponse("successfully registered")
    else:
        form=CosmoForm()
    return render(request,"cosmonauts/cosmoregistration.html",{'form':form})

def trainerlogin(request):
    return render(request,"trainers/trainerlogin.html")
def trainerregister(request):
    if request.method == "POST":
        form1=CosmoTrainerdataForm(request.POST)
        name=request.POST.get('name')
        print("name=",name)
        authkey=request.POST.get('authkey')
        print(authkey)
        status=request.POST.get('status')
        print(status)
        if form1.is_valid():
            form1.save()
        else:
            print("form not valied")
        return HttpResponse(" Trainer successfully registered")
    else:
        form1=CosmoTrainerdataForm()
    return render(request,"trainers/trainerregister.html",{'form':form1})
def student_res_details(s_obj,stu_res_obj):
    dict = {}

    if not stu_res_obj:
        for x in s_obj:
            print(x)
            dict[x.id] = {'stu_id': x.id, 'stu_name': x.name,'mail':x.mail}
            print(dict[x])
    else:
        for x in s_obj:
            for y in stu_res_obj:
                if x.id == y.cosmonaut.id:
                    dict[x.id]={'stu_id':x.id,'stu_name':x.name,'res1':y.result1,'res2':y.result2,'res3':y.avg,'mail':x.mail,'available':'yes'}
                else:
                    try:
                        if dict[x.id]:
                            pass
                        else:
                            dict[x.id] = {'stu_id': x.id, 'stu_name': x.name,'mail':x.mail}
                    except:
                        dict[x.id] = {'stu_id': x.id, 'stu_name': x.name,'mail':x.mail}
    return dict
def cosmonautdetails(request):
    t_id = request.GET['id']
    t_obj = CosmoTrainerdata.objects.get(id=t_id)
    s_obj = CosmoUser.objects.all()
    return render(request, 'trainers/cosmonautdetails.html', {'s_obj': s_obj, 't_obj': t_obj})
    # return render(request,"cosmonautdetails.html",{"qs":qs,'trainer':''})
def cosmonautresults(request):
    t_id = request.GET['id']
    t_obj = CosmoTrainerdata.objects.get(id=t_id)
    s_obj = CosmoUser.objects.all()
    stu_res_obj = Cosmoresults.objects.filter(trainer=t_obj)
    print(stu_res_obj)
    dict1 = student_res_details(s_obj, stu_res_obj)
    return render(request, 'cosmonautresults.html', {'s_obj': s_obj, 't_obj': t_obj, 'res': dict1})
    # qs1=CosmoUser.objects.all()
    # return render(request,"cosmonautresults.html",{"qs1":qs1})
def adminindex(request):
    return render(request,"admins/adminindex.html")
def adminsignin(request):
    return render(request,"admins/adminsignin.html",{})
def adminloginentered(request):
    uname=request.POST.get('uid')
    pwd=request.POST.get('pwd')
    if uname == 'admin' and pwd == 'admin':
        return render(request,"admins/adminindex.html")
    else:
        return render(request,"admins/adminsignin.html",{"message":"Invalied credentials"})
def adminindex(request):
    return render(request,"admins/adminindex.html")
def viewadmincosmonautdata(request):
    qs=CosmoUser.objects.all()
    return render(request,"admins/viewadmincosmonautdata.html",{"qs":qs})
def activatecosmonauts(request):
    if request.method =='GET':
        pid=request.GET.get('pid')
        status='Activated'
        print("pid=",pid,"status",status)
        CosmoUser.objects.filter(id=pid).update(status=status)
        qs=CosmoUser.objects.all()
        return render(request,"admins/viewadmincosmonautdata.html",{"qs":qs})
def viewadmintrainerdata(request):
    qs=CosmoTrainerdata.objects.all()
    return render(request,"admins/viewadmintrainerdata.html",{"qs":qs})


def activatetrainers(request):
    if request.method == 'GET':
        pid=request.GET.get('pid')
        print(pid)
        status='Activated'
        print("pid=",pid ,"status",status)
        CosmoTrainerdata.objects.filter(id=pid).update(status=status)
        qs=CosmoTrainerdata.objects.all()
        return render(request,"admins/viewadmintrainerdata.html",{"qs":qs})
def logout(request):
    return render(request,"index1.html")
def finalreport(request):
    trainer=CosmoTrainerdata.objects.all()

    dict={}
    for x in trainer:

        tstures=Cosmoresults.objects.filter(trainer=x)
        if tstures:
            for y in tstures:

                try:
                    if dict[y.cosmonaut.name]:
                        dict[y.cosmonaut.name].update({y.trainer.name:y.avg})
                    else:
                        dict[y.cosmonaut.name]= {y.trainer.name:y.avg,'id':y.cosmonaut.id}
                except:

                    dict[y.cosmonaut.name] = {y.trainer.name: y.avg,'id':y.cosmonaut.id}
        else:
            for y in CosmoUser.objects.all():
                if dict[y.name] :
                    dict[y.name].update({x.name: 'NA'})
                else:
                    dict[y.name].update({x.name: 'NA'})
        reports=CosmoFinalReports.objects.all()

        if len(reports)!=0:
            data=reports
        else:
            data='NA'
    return  render(request,'admins/finalreport.html',{'res':dict,'trainers':CosmoTrainerdata.objects.all(),'final':data})
def activate(request):
    id=request.GET['id']
    t_obj=CosmoTrainerdata.objects.all()
    count=0
    l1=[]
    while count<len(t_obj):
        inc=count
        try:

            res1=request.POST['res'+str(inc)]
            l1.append(res1)
            count = count + 1
        except:
            res1 = request.POST['res' + str(inc+1)]
            l1.append(res1)
            count = count + 2

    l2=[]
    for x in l1:
        l2.append(int(float(x)))


    res=sum(l2)/len(l2)
    id=request.GET['id']
    obj=CosmoUser.objects.get(id=id)
    try:
        obj1=CosmoFinalReports.objects.get(cosmonaut=obj)
        # print('hello')
        CosmoFinalReports.objects.filter(id=obj1.id).update(avg=res)
    except:
        CosmoFinalReports(cosmonaut=obj,avg=res).save()
    trainer = CosmoTrainerdata.objects.all()

    dict = {}
    for x in trainer:

        tstures = Cosmoresults.objects.filter(trainer=x)
        if tstures:
            for y in tstures:

                try:
                    if dict[y.cosmonaut.name]:
                        dict[y.cosmonaut.name].update({y.trainer.name: y.avg})
                    else:
                        dict[y.cosmonaut.name] = {y.trainer.name: y.avg, 'id': y.cosmonaut.id}
                except:

                    dict[y.cosmonaut.name] = {y.trainer.name: y.avg, 'id': y.cosmonaut.id}
        else:
            for y in CosmoUser.objects.all():
                if dict[y.name]:
                    dict[y.name].update({x.name: 'NA'})
                else:
                    dict[y.name].update({x.name: 'NA'})
        reports = CosmoFinalReports.objects.all()

        if len(reports) != 0:
            data = reports
        else:
            data = 'NA'
    return render(request, 'admins/finalreport.html', {'res': dict, 'trainers': CosmoTrainerdata.objects.all(), 'final': data})



def savestudentres(request):
    trainername=CosmoTrainerdata.objects.get(id=request.session['id'])
    cosmo_name=CosmoUser.objects.get(id=2)
    result=request.POST['score']
    Cosmoresults(trainer=trainername,cosmonaut=cosmo_name,result=result).save()
    stu_res_obj=Cosmoresults.objects.filter(trainer=t_obj)
    dict=student_res_details(s_obj,stu_res_obj)

    return render(request,'cosmonautresults.html',{'s_obj':s_obj,'t_obj':t_obj,'res':dict})
def updatestudentres(request):
    t_id=request.POST['tid']
    s_id=request.POST['sid']
    res1=request.POST['res1']
    res2=request.POST['res2']
    avg=request.POST['res3']
    t_obj=CosmoTrainerdata.objects.get(id=t_id)
    stu_obj=CosmoUser.objects.get(id=s_id)
    s_obj=CosmoUser.objects.all()
    Cosmoresults.objects.filter(cosmonaut=stu_obj,trainer=t_obj).update(result1=res1,result2=res2,avg=avg)
    stu_res_obj=Cosmoresults.objects.filter(trainer=t_obj)
    dict=student_res_details(s_obj,stu_res_obj)

    return render(request,'cosmonautresults.html',{'s_obj':s_obj,'t_obj':t_obj,'res':dict})

def getavailbaleexams(request):
    examtitle = createexam.objects.all()
    return render(request,'cosmonauts/availbaleexampes.html',{'objects':examtitle})
def trainingprocess(request):
    title=request.GET.get('title')
    try:
        exam_obj=createexam.objects.get(title=title)
        date=datetime.today()
        print(date)
        date1=date.strftime('%Y-%m-%d %H:%M:%S')
        date2=exam_obj.date.strftime('%Y-%m-%d %H:%M:%S')
        print(exam_obj.date.day)
        if exam_obj.date.day < date.day:
            return render(request, "trainingprocess.html", {"exam_info": 'no', "exam_obj": exam_obj, 'datetime': 'empty'})
        elif date1 >= date2:
            return render(request,"trainingprocess.html",{"exam_info":'yes',"exam_obj":exam_obj})
        else:
            return render(request,"trainingprocess.html",{"exam_info":'no',"exam_obj":exam_obj,'datetime':date2})
    except:
        return render(request, "trainingprocess.html", {"exam_info":'not yet'})


def techinicalresult(request):
    if request.method=='POST':
        t_obj=CosmoTrainerdata.objects.get(id=request.POST['tid'])
        c_obj=CosmoUser.objects.get(id=request.session['id'])
        print(c_obj)


        title=request.POST.get('title')
        ans1=request.POST.get('q1')
        ans2=request.POST.get('q2')
        ans3=request.POST.get('q3')
        ans4=request.POST.get('q4')
        ans5=request.POST.get('q5')
        try:
            if examdata.objects.get(cosmonaut=c_obj):
                return HttpResponse("you have already done exam,not allowed morethan once")
        except:
            examdata1=examdata(title=title,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5,trainer=t_obj,cosmonaut=c_obj)
            examdata1.save()
            return HttpResponse("exam completed")
def cosmonautresults1(request):
    try:
        id = request.session['trainer']
        print('Trainer ID ',id)
        if id==2:
            if spaceexamdata.objects.filter(trainer=CosmoTrainerdata.objects.get(id=2)):
                message1=spaceexamdata.objects.filter(trainer=CosmoTrainerdata.objects.get(id=2))
                print(message1)
                res = Cosmospaceresults.objects.all()
                return render(request,"trainers/spaceexamdisplay.html",{"message1":message1,'cosmospc_res':res})
        else:
            message = examdata.objects.filter(trainer=CosmoTrainerdata.objects.get(id=request.session['trainer']))
            print(message)
            res = Cosmoresults.objects.all()
            return render(request, "trainers/techinicalresult.html", {"message": message, 'cosmo_res': res})

    except:
       pass
    return render(request,'trainers/trainerresult.html',{})

def createexam1(request):
    form=Createxamform()
    if request.method == 'POST':
        form1=Createxamform(request.POST)
        if form1.is_valid():

            form1.save()
            obj = createexam.objects.latest('id')

            obj.trainername=CosmoTrainerdata.objects.get(id=request.session['trainer'])
            obj.save()
        else:
            print("form not valied")
    return render(request,"trainers/createexam.html",{"form":form})
def saveres1(request):
    id=request.GET.get('id')
    score=request.POST.get('score'+str(id))
    print(score)
    tider='t_name'+str(id)
    print(tider)
    cid=request.POST.get('t_name'+str(id))
    tid=request.session['trainer']
    cosmo_obj=CosmoUser.objects.get(id=cid)
    trainer_obj=CosmoTrainerdata.objects.get(id=tid)
    try:
        cos=Cosmoresults.objects.get(cosmonaut=cosmo_obj)
        print(cos)
        if cos:
            Cosmoresults.objects.filter(id=cos.id).update(result=score,cosmonaut=cosmo_obj,trainer=trainer_obj)
    except:
        Cosmoresults(result=score,cosmonaut=cosmo_obj,trainer=trainer_obj).save()
    message = examdata.objects.filter(trainer=trainer_obj)
    res=Cosmoresults.objects.all()
    return render(request,"trainers/techinicalresult.html",{"message":message,'cosmo_res':res})
def finalreport1(request):
    result=Cosmoresults.objects.all()
    return render(request,"admins/finalreport1.html",{"message":result})
def spacecraftexam(request):
    cos_obj=CosmoUser.objects.get(id=request.GET['id'])
    print(cos_obj)
    exam_obj=examdata.objects.get(cosmonaut=cos_obj)
    print(exam_obj)
    spc_obj = createexam.objects.get(title='spacecraftexam')

    if exam_obj:
        res_obj=Cosmoresults.objects.get(cosmonaut=cos_obj)
        if res_obj.result>=75:
            return render(request,"spacecraftexam.html",{"spc_obj":spc_obj})
        else:
            return HttpResponse("your not shortlisted for 2nd round")
    else:
        return HttpResponse("1st you have to attempt techinical exam round:") 

def spacecraftresult(request):
    if request.method=='POST':
        t_obj=CosmoTrainerdata.objects.get(id=request.POST['tid'])
        c_obj=CosmoUser.objects.get(id=request.session['id'])


        title=request.POST.get('title')
        ans1=request.POST.get('q1')
        ans2=request.POST.get('q2')
        ans3=request.POST.get('q3')
        ans4=request.POST.get('q4')
        ans5=request.POST.get('q5')
        ans6=request.POST.get('q6')
        ans7=request.POST.get('q7')
        ans8=request.POST.get('q8')
        ans9=request.POST.get('q9')
        ans10=request.POST.get('q10')
        examdata1=spaceexamdata(title=title,answer1=ans1,answer2=ans2,answer3=ans3,answer4=ans4,answer5=ans5,answer6=ans6,answer7=ans7,answer8=ans8,answer9=ans9,answer10=ans10,trainer=t_obj,cosmonaut=c_obj)
        examdata1.save()
        return HttpResponse("exam completed")

def saveres2(request):
    id=request.GET.get('id')
    score=request.POST.get('score'+str(id))
    tider='t_name'+str(id)
    print(tider)
    cid=request.POST.get('t_name'+str(id))
    print(cid)
    tid=request.session['trainer']
    cosmo_obj=CosmoUser.objects.get(id=cid)
    trainer_obj=CosmoTrainerdata.objects.get(id=tid)
    try:
        cos=Cosmospaceresults.objects.get(cosmonaut=cosmo_obj)
        print(cos)
        if cos:
            Cosmospaceresults.objects.filter(id=cos.id).update(result=score,cosmonaut=cosmo_obj,trainer=trainer_obj)
    except:
        Cosmospaceresults(result=score,cosmonaut=cosmo_obj,trainer=trainer_obj).save()
    message = spaceexamdata.objects.filter(trainer=trainer_obj)
    res=Cosmospaceresults.objects.all()
    return render(request,"trainers/spaceexamdisplay.html",{"message1":message,'cosmospc_res':res})
def spacereport1(request):
    result1=Cosmospaceresults.objects.all()
    return render(request,"admins/spaceexamfinalreport.html",{"message":result1})


def sendoffer(request):

    if request.method=='GET':
        id = request.GET.get('id')
        check = CosmoUser.objects.get(id=id);
        username = check.name
        email = check.mail
        today = date.today()
        print('User Name ',username,' User Email ',email)
        subject = 'Your Offer from Company Soyuz Spacecraft'
        message = ' Hi '+username+', ' \
                  '\n Thank you for taking the time to speak with us. ' \
                  'We’ve all enjoying meeting you and appreciate your ' \
                  'Space Examinations and Cosmonaut . ' \
                  'We would like to formally offer you the position of cosmonaut pilot at soyuz spacecraft. ' \
                  'This would include a $102500 annual salary, 2600 health care, and 32 days of paid vacation per year. ' \
                  'We also include any retirement, signing bonus,  or other benefits here. ' \
                  'We’re hoping to have you start by '+str(today)+'. ' \
                  'Please feel free to email or call me directly if you have any questions about the offer. ' \
                  'We are so excited to have you join us! \n Best, [Alex Hales]  '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

    result1 = Cosmospaceresults.objects.all()
    return render(request, "admins/spaceexamfinalreport.html", {"message": result1})


































