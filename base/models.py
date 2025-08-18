from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    scheduled_date=models.DateField(null=True,blank=True)
    description=models.TextField(max_length=200,null=True,blank=True)
    status=models.CharField(max_length=10,null=True,blank=True,default='pending')
    completed_date=models.DateField(null=True,blank=True)
    default=models.BooleanField(null=True,blank=True)
    priority_level=models.SmallIntegerField(null=True,blank=True)
    urgency_level=models.SmallIntegerField(null=True,blank=True)
  