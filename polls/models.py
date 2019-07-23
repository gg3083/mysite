from datetime import timezone, datetime

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#
#     class Meta:
#         db_table = 'user'
    #
    # def __init__(self,id,name,age):
    #     self.name = name
    #     self.id = id
    #     self.age = age
