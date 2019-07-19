import pymysql
#告诉Django，用pymysql代替MySQLdb（MySQLdb不支持中py3）
pymysql.install_as_MySQLdb()