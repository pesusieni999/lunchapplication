from rest_framework import serializers
from django.contrib.auth.models import User
from lunchapp.models import Comment, Topic


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'topic')


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Topic
        fields = ('id', 'author', 'name', 'text')


class UserSerializer(serializers.ModelSerializer):
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=Topic.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'topics', 'comments')
