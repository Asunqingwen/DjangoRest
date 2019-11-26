# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 0025 15:01
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: serializers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from rest_framework import serializers

from blog.models import *


class BlogSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.name')  # 只读

	class Meta:
		exclude = []
		model = Blog
		fields = ('id', 'title', 'body', 'owner')


# 用于注册的时候返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		exclude = []  # 序列化中排除的字段
		model = User
		field = ('id', 'username', 'name')  # 显示指定某个model中需要序列化的字段


class UserSerializer(serializers.ModelSerializer):
	blog_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

	class Meta:
		exclude = []
		model = User
		field = ('id', 'username', 'blog_set')
