from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.

def hview(request):
    return render(request,"app1/home.html",{})


@login_required(login_url="/a2/liv/")
def stuview(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/shv/")

    return render(request,"app1/student.html",{"form":form})


@login_required(login_url="/a2/liv/")
def shview(request):
    obj = Student.objects.all()
    print(obj)
    return render(request,"app1/show.html",{"obj":obj})


def uview(request,pk):
    obj = Student.objects.get(sid=pk)
    form = StudentForm(instance=obj)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/shv/")

    return render(request,"app1/student.html",{"form":form})


def dview(request,k):
    obj = Student.objects.get(sid=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/shv/")

    return render(request,"app1/sucess.html",{"obj":obj})