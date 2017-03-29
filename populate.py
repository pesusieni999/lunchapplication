#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to populate database for testing purposes.

This file is part of the system implementation done by Ville Myllynen for Tampere
University of Technology course MAT-81000 Ohjelmallinen sisällönhallinta 2017.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lunchapplication.settings')
django.setup()

from django.contrib.auth.models import User
from lunchapp.models import Topic, Comment

__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Lunch-Rest-API"
__credits__ = ["Ville Myllynen"]
__license__ = "Apache v2.0"
__version__ = "1.0.0"
__maintainer__ = "Ville Myllynen"
__email__ = "na"
__status__ = "Production"


def populate():
    """
    Populate the database with information defined in this function.
    :return: Nothing.
    """

    # Create superuser.
    super_users_created = 0
    super_users_updated = 0
    s_user, created = add_super_user('nimba', '1234')
    if created:
        super_users_created += 1
    else:
        super_users_updated += 1

    # Create topics.
    topics_created = 0
    topics_updated = 0
    topic_1, created = add_topic("New topic 1", s_user)
    if created:
        topics_created += 1
    else:
        topics_updated += 1

    # Create comments.
    comments_created = 0
    comments_updated = 0
    _, created = add_comment(topic_1, "New comment 1 to topic 1.", s_user)
    if created:
        comments_created += 1
    else:
        comments_updated += 1

    # Print populate results.
    print("New super users created: ", super_users_created)
    print("Old super users updated: ", super_users_updated)
    print("New topics created: ", topics_created)
    print("Old topics updated: ", topics_updated)
    print("New comments created: ", comments_created)
    print("Old comments updated: ", comments_updated)


def add_super_user(name, password):
    """
    Add or get super user. Matching name is considered same.
    :param name: Name of the user.
    :param password: New password.
    :return: Created/Updated user object, Boolean (true if user created).
    """
    created = False
    try:
        u = User.objects.get(username=name)
    except User.DoesNotExist:
        created = True
        u = User(username=name)
    u.set_password(password)
    u.save()
    return u, created


def add_topic(topic, author):
    """
    Add or get topic. Mathing topic text and author is considered same.
    :param topic: Topic text for the topic object.
    :param author: Author object of the topic.
    :return: Created/Updated topic object, Boolean (true if topic created).
    """
    created = False
    try:
        t = Topic.objects.get(name=topic, author=author)
    except Topic.DoesNotExist:
        created = True
        t = Topic(name=topic, author=author)
        t.save()
    return t, created


def add_comment(topic, comment, author):
    """
    Add or get comment. Matching comment text, topic and author objects are considered same.
    :param topic: Topic object to which comment belongs to.
    :param comment: Comment text for the comment object.
    :param author: Author object who created the comment.
    :return: Created/Updated comment object. Boolean (true if comment created).
    """
    created = False
    try:
        c = Comment.objects.get(topic=topic, text=comment, author=author)
    except Comment.DoesNotExist:
        created = True
        c = Comment(topic=topic, text=comment, author=author)
        c.save()
    return c, created


if __name__ == '__main__':
    print('Starting test data population.')
    populate()
    print('Test data population completed.')
