from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    pw = models.CharField(max_length=200, default='1234')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    content = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    tag = models.ForeignKey('Tag', null=True, blank=True, on_delete=models.CASCADE)
    thumbnail = models.FileField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title