from django.db import models

# Create your models here.
class state(models.Model):
    Name= models.CharField(max_length=50,null =True,blank=True)
    Image=models.ImageField(upload_to='state_images/',null=True,blank=True)

