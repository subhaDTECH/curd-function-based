from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import User
from django.contrib import messages

# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            unm=fm.cleaned_data['name']
            uem=fm.cleaned_data['email']
            unpass=fm.cleaned_data['password']
            uwork=fm.cleaned_data['work']
            user=User(name=unm,email=uem,password=unpass,work=uwork)
            messages.success(request,"Registation successfyl!!!")
            user.save()
            fm=StudentForm()
            
    else:
        fm=StudentForm()
    Data=User.objects.all()
    return render(request,"student/addshow.html",{"form":fm,"data":Data})



def update_user(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Update data")
            
    else:
        pi=User.objects.get(pk=id)
        fm=StudentForm(instance=pi)
    return render(request,'student/update.html',{"form":fm})

def delete_user(requset,id):
    if requset.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.success(requset,"data deleted successfully!")
        return HttpResponseRedirect('/addshow/')
        
       
