from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='course', null=True)

    title = models.CharField(max_length=200, null=False)#과목명
    image = models.ImageField(upload_to='course/', null=False)#과목사진

    classnumber = models.CharField(max_length=200, null=False)#학수번호

    created_at = models.DateField(auto_now_add=True, null=True)
