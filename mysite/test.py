import pymysql

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

    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        # print(type(row[1])) #打印变量类型 <class 'str'>

        print("id=%s,name=%s,age=%s" % \
              (id,name, age))


if __name__ == '__main__':
    for i in range(1,5):
        update(i)

    # insert()
    select()

