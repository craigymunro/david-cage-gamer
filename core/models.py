from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    date = models.DateTimeField('Publication date')
    body = models.TextField(null=True)
    
    def __str__(self):
        return self.title