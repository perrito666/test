import HTMLParser
from django.db import models
from django.utils.html import strip_tags


class Devotional(models.Model):
    "title month day body"
    title = models.CharField(max_length="75")
    month = models.IntegerField()
    day = models.IntegerField()
    body = models.TextField()

    def __unicode__(self):
        return "(%d/%d) %s" % (self.month, self.day, self.title)

    class Meta:
        unique_together = ("month", "day")

    def get_body(self):
        return HTMLParser.HTMLParser().unescape(self.body)

    def get_wordcount(self):
        escaped = HTMLParser.HTMLParser().unescape(self.body)
        escaped = strip_tags(escaped).split(" ")
        return len(escaped)
