from rest_framework import generics, mixins
from rest_framework import permissions
from django.contrib.auth.models import User
from lunchapp.models import Topic, Comment
from lunchapi.serializers import TopicSerializer, CommentSerializer, UserSerializer
from lunchapi.permissions import IsOwnerOrReadOnly


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class TopicList(generics.ListCreateAPIView):
    """
    List all topics or create a new topic.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a topic instance.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a new comment.
    """
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Comment.objects.filter(topic__pk=topic_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Comment.objects.filter(topic__pk=topic_id)


class UserList(generics.ListAPIView):
    """
    List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    """
    List user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
