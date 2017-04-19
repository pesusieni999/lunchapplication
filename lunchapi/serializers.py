from rest_framework import serializers
from django.contrib.auth.models import User
from lunchapp.models import Comment, Topic


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for reading/writing Comment models.
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'topic')


class TopicSerializer(serializers.ModelSerializer):
    """
    Serializer for reading/writing Topic models.
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Topic
        fields = ('id', 'author', 'name', 'text')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for reading/writing User models.
    """
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=Topic.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'topics', 'comments')
