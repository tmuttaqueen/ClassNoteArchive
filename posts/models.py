from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    description = models.TextField()

