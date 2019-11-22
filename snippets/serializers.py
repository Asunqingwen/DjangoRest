# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 0022 14:27
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: serializers.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
		owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')
