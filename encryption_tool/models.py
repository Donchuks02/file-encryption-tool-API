from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  bio = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.user.username}'s profile"


class EncryptedFile(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  file = models.FileField(upload_to='uploads/')
  encrypted_file = models.FileField(upload_to='encrypted_files/', blank=True, null=True)
  encrypted_method = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

