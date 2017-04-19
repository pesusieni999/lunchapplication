from django.db import models
from django.contrib.auth.models import User


__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class Topic(models.Model):
    """
    Model for topics. Topics are discussions to which comments can be added.
    """
    author = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    """
    Model for comments. Comments belong to a topic.
    """
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1024, null=True)
    topic = models.ForeignKey(to=Topic, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
