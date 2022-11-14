from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    mo_nu=models.IntegerField(max_length=10)
    email=models.CharField(max_length=30)
    password=models.IntegerField(max_length=15)
    city=models.CharField(max_length=25)
    about=models.CharField(max_length=100)
    dp=models.ImageField(default='Media/default.png',upload_to="user_dp")
    

