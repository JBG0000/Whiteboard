from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='course', null=True)

    title = models.CharField(max_length=200, null=False)#제목이 꼭 있도록 null=False
    image = models.ImageField(upload_to='course/', null=False)

    content = models.TextField(null=False)#내용도 꼭 있도록 null=False

    created_at = models.DateField(auto_now_add=True, null=True)
