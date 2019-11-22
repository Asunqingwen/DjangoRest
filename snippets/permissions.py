# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 0022 17:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: permissions.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	自定义权限只允许对象的所有者编辑它
	"""

	def has_object_permission(self, request, view, obj):
		# 读取权限允许任何请求
		# 所以总是允许GET,HEAD或OPTIONS请求
		if request.method in permissions.SAFE_METHODS:
			return True

		# 只有该snippet的所有者才允许写权限
		return obj.owner == request.user
