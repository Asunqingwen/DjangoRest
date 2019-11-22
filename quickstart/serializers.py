# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 0022 13:28
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: serializers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

# 序列化程序
from django.contrib.auth.models import User, Group
from rest_framework import serializers

#使用超链接关系
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		modle = Group
		fields = ('url', 'name')
