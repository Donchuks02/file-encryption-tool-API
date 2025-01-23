from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  bio = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.user.username}'s profile"

