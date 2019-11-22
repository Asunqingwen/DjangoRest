from django.contrib.auth.models import User
from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

# 类视图
class SnippetList(generics.ListCreateAPIView):
	"""
	列出所有的code snippet，或创建一个新的snippet。
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	获取，更新或删除一个code snippet
	"""

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
	                      IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
