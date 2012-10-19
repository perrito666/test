from django.db import models


class Devotional(models.Model):
    "title month day body"
    title = models.CharField(max_length="75")
    month = models.IntegerField()
    day = models.IntegerField()
    body = models.TextField()
