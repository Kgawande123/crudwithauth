from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def suview(reqest):
    form = UserCreationForm()
    if reqest.method == "POST":
        form = UserCreationForm(reqest.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/shv/")

    return render(reqest,"authapp/signup.html",{"form":form})


def liview(reqest):
    if reqest.method == "POST":
        u = reqest.POST.get("un")
        p= reqest.POST.get("p")
        user = authenticate(username=u,password=p)
        print(user)
        if user!=None:
            login(reqest,user)
            return redirect("/a1/shv/")


    return render(reqest,"authapp/login.html",{})

def loview(reqest):
    logout(reqest)
    return redirect("/a2/liv/")
