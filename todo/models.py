from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    @property
    def role(self):
        return "admin" if self.is_superuser else "employee"


class Task(models.Model):
    PRIORITY_CHOICES = (('low', 'Low'), ('medium', 'Medium'), ('high', 'High'),)

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.priority} | {self.author}"