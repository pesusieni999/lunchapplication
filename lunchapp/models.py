from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    author = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1024, null=True)
    topic = models.ForeignKey(to=Topic, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
