# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 0025 15:19
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: permissions.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.session.get('user_id') is not None

	def has_object_permission(self, request, view, blog):
		# Read permissions are allowed to any request,
		# so we'll always allow GET,HEAD or OPTIONS requests
		if request.method in permissions.SAFE_METHODS:
			return True
		return blog.owner.id == request.session.get('user_id')
