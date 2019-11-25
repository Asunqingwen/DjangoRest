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


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	# 实体之间使用超链接
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'snippets')
