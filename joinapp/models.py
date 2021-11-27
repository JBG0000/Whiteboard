from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from courseapp.models import Course


class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='join')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='join')

    class Meta:
        unique_together = ('user', 'course')
