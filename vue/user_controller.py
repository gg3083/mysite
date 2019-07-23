from django.shortcuts import redirect, render
import pandas as pdx
from vue.models import User


def index(request):
    return render(request,"vue/index.html")

def list(request):
    userList = User.objects.all().order_by("-id")
    datas = []
    for user in userList:
        userMap = {}
        userMap['id'] = user.id
        userMap['name'] = user.name
        userMap['age'] = user.age
        datas.append(userMap)
        print(userMap)

    return datas

def get(request):
    id = request.GET["id"]
    user = User.objects.filter(id=id).get()
    print(user)
    return user

def delete(request):
    id = request.GET["id"]
    User.objects.filter(id=id).delete()
    return redirect('/index/')

def update(request):
    id = request.GET["id"]
    if id:
        name = request.GET["name"]
        age = request.GET["age"]
        user = User.objects.filter(id=id).get()
        user.age = age
        user.name = name
        user.save()
        return redirect('/index/')
