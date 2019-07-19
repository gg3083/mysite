import re

import bs4 as bs4
import pymysql
import requests
import xlwt as xlwt
import xlsxwriter as xw


db = pymysql.connect("localhost", "root", "root", "python");
cursor = db.cursor()


def creat():
    # 创建user表
    cursor.execute("drop table if exists user")
    sql = """CREATE TABLE IF NOT EXISTS `user` ( 
          `id` int(11) NOT NULL AUTO_INCREMENT, 
          `name` varchar(255) NOT NULL, 
          `age` int(11) NOT NULL, 
          PRIMARY KEY (`id`) 
        ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

    cursor.execute(sql)





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




def select():
    cursor.execute("select * from user")

    results = cursor.fetchall()

    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        # print(type(row[1])) #打印变量类型 <class 'str'>

        print("id=%s,name=%s,age=%s" % \
              (id,name, age))

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
    # export(datas)

def export(msg_list):
    workbook = xw.Workbook('Expenses03.xlsx')
    worksheet = workbook.add_worksheet('sheet1')

    worksheet.write(0, 0, "标题")
    worksheet.write(0, 1, "地址")
    worksheet.write(0, 2, "热度")

    for i in range(len(msg_list)):
            row = msg_list[i]
            worksheet.write(i+1, 0, row["title"])
            worksheet.write(i+1, 1, row["url"])
            worksheet.write(i+1, 2, row["index"])
    # 创建操作二进制数据的对象

    # 关闭excel 文件 释放资源
    workbook.close()




if __name__ == '__main__':

    datas =  requestPage()

