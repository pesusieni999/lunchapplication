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


"""
class Restaurant(models.Model):
    name = models.CharField(max_length=256)


class Diets(models.Model):
    abbreviation = models.CharField(max_length=8)
    long_name = models.CharField(max_length=128)


class Meal(models.Model):
    name = models.CharField(max_length=64)


class Food(models.Model):
    name = models.CharField(max_length=64)  # Chili con carne
    diets = models.ForeignKey(Diets, related_name='food', on_delete=models.SET_NULL, null=True)
"""
