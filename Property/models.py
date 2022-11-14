from django.db import models
from django.contrib.auth.models import User

from index.models import user_profile

class property(models.Model):
    property_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    p_dp=models.ImageField(upload_to="Property_dp",default="Media/home.png")
    area=models.IntegerField(max_length=5)
    room=models.IntegerField(max_length=2)
    city=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    about_property=models.CharField(max_length=100)
    type=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    price=models.IntegerField(blank=True,default=0)

class property_image(models.Model):
    property_id=models.ForeignKey(property,on_delete=models.CASCADE)
    property_img=models.ImageField(upload_to="property_img")
    def __str__(self):
        return "image of object"+str(self.property_id)

class Card(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    property_id=models.ForeignKey(property,on_delete=models.CASCADE)
    is_fav=models.BooleanField(default=False)
    is_book=models.BooleanField(default=False)

