from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.tag_name

class Post(models.Model):
    title = models.CharField(max_length=500)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=500, blank=True)
    tags = models.ManyToManyField(Tag)
    total_upvote = models.IntegerField(default=0)
    total_downvote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

