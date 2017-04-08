from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog')

    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1024)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Пост #{id}: {title}'.format(id=self.id, title=self.title)


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey(Post, related_name='likes')

    def __str__(self):
        return 'Лайк #{id}: от "{author}" к посту "{post}"'.format(id=self.id, author=self.author, post=self.post)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
