from django.db import models

# Create your models here.
class People(models.Model):
    #变量类型
    #null=True 数据库中暂时没有这个数据也没有关系
    #blank=true 名字都不填写也可以
    name = models.CharField(null=True,blank=True,max_length=200)
    job = models.CharField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.name

class Ariticle(models.Model):
    headline =  models.CharField(null=True,blank=True,max_length=500)
    content =  models.TextField(null=True,blank=True)
    #变量利用元组的形式
    TAG_CHOICES = {
        ('tech','Tech'),
        ('life','Life'),
    }
    # 设置文章的分类,choices 提供下拉选项的字段
    tag = models.CharField(null=True,blank=True,max_length=5,choices=TAG_CHOICES)


    def __str__(self):
        return self.headline


