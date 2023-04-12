from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from posts.models import Post, Group
import api.serializers as sers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = sers.PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = sers.GroupSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Получение, создание, изменение и удаление комментариев."""
    serializer_class = sers.CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Возвращаем все комментарии к посту."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Вызов сериализатора для создания
        и сохранения комментария к посту."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
