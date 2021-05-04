from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
    user_type_choices = [('User', 'User'), ('Privileged User', 'Privileged User')]
    user_type = models.CharField(choices=user_type_choices, max_length=20, default='User')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_year = models.DateField()
    passing_year = models.DateField()
    degree_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    present_address = models.CharField(max_length=500)
    permanent_address = models.CharField(max_length=500)
    rating = models.FloatField()
