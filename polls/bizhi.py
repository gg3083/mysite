import os
import random
from datetime import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


def list(request):
    fileList = os.listdir("D:\work-idea\mysite\static")
    for file in fileList:
        print(type(file))
        print(file)
    return render(request,"index.html",{"files":fileList})

def addPage(request):
    return render(request,"add.html")



def add(request):
    for fname in  request.FILES.getlist('files'):
        if fname:
            no =  random.uniform(1, 999999);
            new_fname = r'static/'+ str(no) + fname.name
            filename = FileSystemStorage().save(new_fname, fname)

    return redirect("/polls/index")