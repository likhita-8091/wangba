from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=16, verbose_name='姓名', unique=True)
    account = models.CharField(max_length=64, verbose_name="账号")
    note = models.CharField(max_length=64, verbose_name="备注")
    phone = models.CharField(max_length=11, verbose_name="联系电话")
    sex = models.CharField(max_length=2, verbose_name="性别")
    u_age = models.IntegerField(verbose_name="出生年月")
    # 分超级管理员、网管、会员3种
    role = models.CharField(max_length=16, verbose_name="角色", choices=((1, '超级管理员'), (2, '网管'), (3, '会员')))
    password = models.CharField(max_length=16, verbose_name="密码")

    def __str__(self):
        return self.name
