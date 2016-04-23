from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Maybe Quote and Review should extend the same base class

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Book(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    year = models.PositiveIntegerField()

class Quote(models.Model):
    book = models.ForeignKey('Book')
    text = models.TextField()
    username = models.ForeignKey(AUTH_USER_MODEL)
    datetime_added = models.DateTimeField(auto_now_add=True)
    upvote = models.PositiveIntegerField()


class Review(models.Model):
    book = models.ForeignKey('Book')
    text = models.TextField()
    username = models.ForeignKey(AUTH_USER_MODEL)
    datetime_added = models.DateTimeField(auto_now_add=True)
    upvote = models.PositiveIntegerField()

