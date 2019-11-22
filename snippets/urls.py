# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 0022 15:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: urls.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
	re_path(r'^snippets/$', views.SnippetList.as_view()),
	re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

	re_path(r'^users/$', views.UserList.as_view()),
	re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
