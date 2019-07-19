import re

import bs4
import pymysql
from django.http import HttpResponse
import requests
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
    # ret = models.User.objects.all().order_by("id")
    datas = requestPage()
    return render(request, "list.html",{"list":datas})

def requestPage():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    url = "https://s.weibo.com/top/summary?cate=realtimehot&sudaref=www.baidu.com&display=0&retcode=6102";
    weiboUrl = "https://s.weibo.com/";
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    # response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
    response = requests.get(url, headers=headers)

    content = response.text
    soup = bs4.BeautifulSoup(content, "html.parser")
    list = []
    datas = []
    for data in soup.find_all('tbody'):
        for td in data.find_all('td'):
            if (str(td).startswith("<td class=\"td-02\">")):
                list.append(td)


    for l in list:
        a = l.find("a")
        span = l.find("span")
        dd = re.compile(r'<[^>]+>', re.S).sub('', str(span))
        dd2 = re.compile(r'<[^>]+>', re.S).sub('', str(a))
        dicts = {}
        dicts["title"] = dd2
        dicts["url"] = weiboUrl + str(a.get('href'))
        dicts["index"] = dd
        datas.append(dicts)

    print(datas)
    return datas

def delete(request):
    id = request.GET.get("id")
    print(id)
    ret = models.User.objects.get(id=id);
    ret.delete()
    # return redirect("/polls/list")
    return list(request)