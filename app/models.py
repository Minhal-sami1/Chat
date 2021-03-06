import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from .encrypt import decrypt
# Create your models here.


class User(AbstractUser):
    seperation = models.CharField(unique=True, default=uuid.uuid1, editable=False, max_length=100)
    pass

class Message(models.Model):
    text = models.TextField(max_length=50000)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagefrom")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messageto")
    time = models.TimeField(auto_now=True)
    def __str__(self):
        return f"Message: {decrypt(self.text)}, from: {self.user_from}, to: {self.user_to}"
