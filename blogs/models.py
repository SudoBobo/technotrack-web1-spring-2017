from django.conf import settings
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)

    def __str__(self):
        return 'Блог #{id}: {title}'.format(id=self.id, title=self.title)
        
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)


