from django.db import models

# Create your models here.

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from django.contrib.auth.admin import UserAdmin

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    avatar = models.ImageField(upload_to="avatar/%Y", null=True, default="", verbose_name="个人头像")
    nickname = models.CharField(max_length=50, default="", null=True, verbose_name="用户昵称")

    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name



class Category(models.Model):
    name = models.CharField('博客分类',max_length = 100)
    is_visble=models.IntegerField(verbose_name="是否可见")
    
    class Meta:
       verbose_name = '博客分类'
       verbose_name_plural = verbose_name
	
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    blog_name=models.CharField(max_length = 255,db_comment="名称")
    blog_text=models.TextField(max_length = 255,db_comment="内容")
    category_id=models.TextField(max_length = 255,db_comment="Categoryid")
    
    class Meta:
       verbose_name = '博客分类'
       verbose_name_plural = verbose_name
	
    def __str__(self):
        return self.name




# admin.site.register(User)


# class classroom(models.Model):
#     classroom_id = models.CharField(max_length=50, unique=True, verbose_name='教室编号')
#     classroom_name = models.CharField(max_length=50, unique=True, verbose_name='教室名称')
#     classroom_capacity = models.IntegerField(verbose_name='教室容量')
#     classroom_location = models.CharField(max_length=50, verbose_name='教室位置')
#     classroom_type = models.CharField(max_length=50, verbose_name='教室类型')

#     class Meta:
#         db_table = 'classroom'
#         verbose_name = '教室'
#         verbose_name_plural = verbose_name




