from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class jobPost(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
