from django.db import models
from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings



# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=500)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog'


class regional_sample(models.Model):
    tree = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    class Meta:
        db_table = 'regional_sample'


class forset(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    tree_species = models.CharField(max_length=100)

    class Meta:
        db_table = 'forset'



class poplar(models.Model):
    place = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    rep = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)

    class Meta:
        db_table = 'poplar'



class video(models.Model):
    video = models.FileField(upload_to='video')
    name = models.CharField(max_length=100)

    # img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name

class lineChart(models.Model):
    image = models.FileField(upload_to='lineChart')
    name = models.CharField(max_length=100)

    # img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'lineChart'

    def __str__(self):
        return self.name

class pieChart(models.Model):
    image = models.FileField(upload_to='lineChart')
    name = models.CharField(max_length=100)

    # img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'pieChart'

    def __str__(self):
        return self.name


class treeTmp(models.Model):
    place = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    rep = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)


    class Meta:
        db_table = 'treeTmp'

class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

# 保存文件
class SaveFile(models.Model):
    name=models.CharField(max_length=1000)
    create_time = models.DateTimeField(u"上传时间")
    file_url = models.FileField(upload_to='SaveExcel',max_length=1000)  # 'SaveExcel'是保存excel的文件夹（即路径）

    class Meta:
        db_table = 'SaveFile'

class rule_table(models.Model):
    file = models.FileField(upload_to='rule_table')
    name = models.CharField(max_length=100)

    # img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'rule_table'

    def __str__(self):
        return self.name

class decisionTree_img(models.Model):
    image = models.FileField(upload_to='decisionTree_img')
    name = models.CharField(max_length=100)

    # img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'decisionTree_img'

    def __str__(self):
        return self.name


class Qx(models.Model):
    fy_tem = models.FloatField(blank=True, null=True)
    qq_tem = models.FloatField(blank=True, null=True)
    lj_tem = models.FloatField(blank=True, null=True)
    dq_tem = models.FloatField(blank=True, null=True)
    hr_tem = models.FloatField(blank=True, null=True)
    nh_tem = models.FloatField(blank=True, null=True)
    gn_tem = models.FloatField(blank=True, null=True)
    fy_hum = models.FloatField(blank=True, null=True)
    qq_hum = models.FloatField(blank=True, null=True)
    lj_hum = models.FloatField(blank=True, null=True)
    dq_hum = models.FloatField(blank=True, null=True)
    hr_hum = models.FloatField(blank=True, null=True)
    nh_hum = models.FloatField(blank=True, null=True)
    gn_hum = models.FloatField(blank=True, null=True)
    fy_sum = models.FloatField(blank=True, null=True)
    qq_sum = models.FloatField(blank=True, null=True)
    lj_sum = models.FloatField(blank=True, null=True)
    dq_sum = models.FloatField(blank=True, null=True)
    hr_sum = models.FloatField(blank=True, null=True)
    nh_sum = models.FloatField(blank=True, null=True)
    gn_sum = models.FloatField(blank=True, null=True)
    fy_rai = models.FloatField(blank=True, null=True)
    qq_rai = models.FloatField(blank=True, null=True)
    lj_rai = models.FloatField(blank=True, null=True)
    dq_rai = models.FloatField(blank=True, null=True)
    hr_rai = models.FloatField(blank=True, null=True)
    nh_rai = models.FloatField(blank=True, null=True)
    gn_rai = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qx'




# 将models在admin中注册，可以修改数据库中的数据
admin.site.register(Blog)
admin.site.register(regional_sample)
admin.site.register(forset)
admin.site.register(poplar)
admin.site.register(video)
