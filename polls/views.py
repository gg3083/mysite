import re
import time
import bs4
import pymysql
from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect

from polls import models


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def list(request):
    # ret = models.User.objects.all().order_by("id")
    datas = requestPage()
    return render(request, "list.html",{"list":datas})

def requestPage():
    now = time.time()
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

    print(now)
    print( time.time() - now)
    return datas

