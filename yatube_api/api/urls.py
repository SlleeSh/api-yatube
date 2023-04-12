from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'group', GroupViewSet)
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('api-token-auth', views.obtain_auth_token),
    path('', include(router.urls))
]
