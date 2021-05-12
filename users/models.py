from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, blank=True)
    def __str__(self): 
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    user_type_choices = [('User', 'User'), ('Privileged User', 'Privileged User')]
    user_type = models.CharField(choices=user_type_choices, max_length=20, default='User')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    admission_year = models.DateField(blank=True)
    passing_year = models.DateField(blank=True)
    degree_name = models.CharField(max_length=100, blank=True)
    department_name = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, blank=True)
    present_address = models.CharField(max_length=500, blank=True)
    permanent_address = models.CharField(max_length=500, blank=True)
    rating = models.FloatField(blank=True)
