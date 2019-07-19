import pymysql
from django.http import HttpResponse
from django.shortcuts import render, redirect

from polls import models

db = pymysql.connect("localhost", "root", "root", "python");
cursor = db.cursor()

def insert():
    sql = """INSERT INTO `user` (`id`,`name`, `age`) VALUES 
    (1,'test1', 1), 
    (2,'test2', 2), 
    (3,'test3', 3), 
    (4,'test4', 4), 
    (5,'test5', 5), 
    (6,'test6', 6);"""
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


def delete(id):
    sql = "delete from user where id='%s'" % (id)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def update(id):
    # sql = "update user set age=100 where id='%s'" % (id)
    sql ="update user set age='{0}' where id ='{1}'".format(id*10,id)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def select():
    cursor.execute("select * from user")
    results = cursor.fetchall()
    return results;



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def list(request):
    ret = models.User.objects.all().order_by("id")
    return render(request, "list.html",{"list":ret})

def delete(request):
    id = request.GET.get("id")
    print(id)
    ret = models.User.objects.get(id=id);
    ret.delete()
    # return redirect("/polls/list")
    return list(request);