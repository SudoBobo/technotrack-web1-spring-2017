from django.conf import settings
from django.db import models


class Comment(models.Model):

    post = models.ForeignKey('posts.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)