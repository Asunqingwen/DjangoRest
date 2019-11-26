"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
# 概要视图
from rest_framework.schemas import get_schema_view

# from snippets import views
from blog import views

# 创建路由器，并注册我们的视图
router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'blogs', views.BlogViewSet)

schema_view = get_schema_view(title='Pastebin API')

# API URL现在由路由器自动确定
# 包含可浏览的API登录URL
urlpatterns = [
	# 自定义视图
	re_path(r'^', include(router.urls)),
	# rest_framwork登录页
	# re_path(r'^', include('rest_framework.urls')),
	# 概要视图
	# re_path(r'^schema/$', schema_view),
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^register', views.UserRegisterAPIView.as_view()),
	re_path(r'^login', views.UserLoginAPIView.as_view()),
]
