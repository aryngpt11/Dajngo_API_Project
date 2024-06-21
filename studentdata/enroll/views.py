from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import StudentRegistration  
from enroll.models import User
# Create your views here.
def addstud(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            #or
            #fm.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
def updstud(request, id):
    pi = User.objects.get(pk=id)  # Get the user object once outside the if-else block
    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')