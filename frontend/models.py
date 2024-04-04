from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class state(models.Model):
    Name= models.CharField(max_length=50,null =True,blank=True)
    Image=models.ImageField(upload_to='state_images',null=True,blank=True)
    def __str__(self):
        return self.Name
    
class destination(models.Model):
    State = models.ForeignKey(state,on_delete=models.CASCADE,null=True,blank=True)
    Image = models.ImageField(upload_to='destination_images',null=True,blank=True)
    Name = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.Name
    
class Package(models.Model):
    destination = models.ForeignKey(destination,on_delete=models.CASCADE,null=True,blank=True)
    spot = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    duration = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to='package_images',null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.spot
    
class Hotel(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE,null=True,blank=True)
    hotel_name = models.CharField(max_length=50,null=True,blank=True)
    hotel_image = models.ImageField(upload_to='hotel_image',null=True,blank=True)
    hotel_description = models.CharField(max_length=500,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.hotel_name
    
class User_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    package = models.ForeignKey(Package,on_delete=models.CASCADE,null=True,blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True,blank=True)
    U_Name = models.CharField(max_length=50,null=True,blank=True)
    U_State = models.CharField(max_length=50,null=True,blank=True)
    U_Street = models.CharField(max_length=50,null=True,blank=True)
    U_Town = models.CharField(max_length = 50,null =True,blank= True)
    U_Phone = models.CharField(max_length=50,null=True,blank=True)
    U_Email = models.EmailField(max_length=50,null=True,blank=True)

class Feedback(models.Model):
    Name= models.CharField(max_length=50,null=True,blank=True)
    email= models.EmailField(max_length=50,null=True,blank=True)
    feedback = models.CharField(max_length=500,null=True,blank=True)