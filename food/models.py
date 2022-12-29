from distutils.command.upload import upload
from email.mime import image
from turtle import update
from django.db import models
from django.contrib.auth.models import User

class Cuisine(models.Model):
    catagory = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.catagory
    
class Food(models.Model):
    catagory = models.ForeignKey(Cuisine,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    describtion = models.TextField()
    secondary_describtion = models.TextField(default=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food_images/')
        
    def __str__(self):
        return self.name
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order_details=models.CharField(max_length=500)
    total_price=models.FloatField()
    is_ready=models.BooleanField(default=False)
    is_delivered=models.BooleanField(default=False)
    crated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
            
