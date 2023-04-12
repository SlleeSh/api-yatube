from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('text', 'pub_date', 'author', 'image', 'group')
        model = Post
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'post', 'text', 'created')
        model = Comment
