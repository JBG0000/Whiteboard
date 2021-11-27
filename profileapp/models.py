from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  #id

    name = models.CharField(max_length=20, unique=True, null=True)  #이름
    image = models.ImageField(upload_to='profile/', null=True)  #사진
    studentid = models.CharField(max_length=20, unique=True, null=True) #학번
    department = models.CharField(max_length=100, null=True)  #학과

    PERSON_STATUS = [('0', '학부생'), ('1', '교수')]  #학생, 교수
    personnel = models.CharField(max_length=5, choices=PERSON_STATUS, default='0')