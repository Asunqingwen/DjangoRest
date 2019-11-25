from django.contrib.auth.models import User
from rest_framework import permissions, renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

# 类视图集
class SnippetViewSet(viewsets.ModelViewSet):
	"""
	此视图自动提供‘list’，‘create’，‘retrieve’，‘update’和‘destroy’操作
	我们额外提供一个‘highlight’操作
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
	                      IsOwnerOrReadOnly,)

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	此视图自动提供‘list’和‘detail’操作
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

