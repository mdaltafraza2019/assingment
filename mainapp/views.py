from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import*
# Create your views here.
def home(r):
    return render(r,'home.html')

def add(r):
    form=StudentForm(r.POST or None ,r.FILES or None)
    if(r.method=="POST"):
        if form.is_valid():
            form.save()
            return redirect(detail)

    return render(r,"add.html",{"form":form})
def edit(r,id):
    data={}
    student=Student.objects.get(id=id)
    form=StudentForm(r.POST or None ,r.FILES or None,instance=student)
    if(r.method=="POST"):
        if data.form.is_valid():
            data.form.save()
            return redirect(detail)

    return render(r,"edit.html",{'form':form})
def detail(r):
    data=Student.objects.all()
    return render(r,'detail.html',{'user':data})

def deletefun(r,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect(detail)