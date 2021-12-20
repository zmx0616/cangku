from django.db import models
from datetime import datetime

#员工账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    #员工账号
    pwd = models.CharField(max_length=50)    #员工密码
    roles= models.ManyToManyField(to="Role")
    def toDict(self):
        return {'id': self.id, 'username': self.username, 'pwd': self.pwd,}

    def __str__(self): return self.username
    class Meta:
        db_table = "user"  # 更改表名


class Role(models.Model):
    title=models.CharField(max_length=50)
    permission= models.ManyToManyField(to="Permission")

    def __str__(self): return self.title
    class Meta:
        db_table = "role"  # 更改表名


class Permission(models.Model):
    title=models.CharField(max_length=50)
    url= models.CharField(max_length=50)

    def __str__(self):return self.title
    class Meta:
        db_table = " permission"  # 更改表名


class Waitui(models.Model):
    username = models.CharField(max_length=50)
    datetime1 = models.DateTimeField(default=datetime.now)
    ridername = models.CharField(max_length=100)
    riderphone = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    detailes = models.CharField(max_length=150)
    onboarding = models.CharField(max_length=50)
    onboardtime = models.CharField(max_length=50)
    threedays = models.CharField(max_length=50)
    threeonjob = models.CharField(max_length=50)
    sevendays = models.CharField(max_length=50)
    sevenonjob = models.CharField(max_length=50)
    fifitydays = models.CharField(max_length=50)
    fifityonjob = models.CharField(max_length=50)
    class Meta:
        db_table = "waitui"  # 更改表名