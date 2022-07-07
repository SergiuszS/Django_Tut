import email
from django.db import models

# Create your models here.

class TestUsers(models.Model):
    username = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    occupation = models.CharField(max_length=128, default='default')