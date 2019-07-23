import pymysql
from django.db import models


db = pymysql.connect("localhost", "root", "root", "python");
cursor = db.cursor()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    class Meta:
        db_table = 'user'

