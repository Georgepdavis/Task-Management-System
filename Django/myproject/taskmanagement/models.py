from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.

class User(AbstractUser):
    firstname=models.CharField(max_length=20,null=True)
    profile_pic=models.ImageField(upload_to='images/',null=True, blank=True)


class Task(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    members=models.ManyToManyField(User,related_name="tasks")
    created_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_date=models.DateField(default=timezone.now)
    status=models.CharField(max_length=20,default='pending')


class Comments(models.Model):
    comment=models.CharField(max_length=30,null=True,blank=True)
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    created_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_date=models.DateField(default=timezone.now)
