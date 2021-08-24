from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    favorite_bacon = models.TextField(null=True, default='')
    longest = models.IntegerField(default='0')
    def __str__(self):
        return str(self.user)