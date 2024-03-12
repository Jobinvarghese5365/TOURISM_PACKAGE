from django.db import models

# Create your models here.
class PackagesDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="image", null=True, blank=True)
    def __str__(self):
        return self.Name

class Spot(models.Model):
    Destination = models.ForeignKey(PackagesDb, on_delete=models.CASCADE, null=True, blank=True)
    S_Name = models.CharField(max_length=50, null=True, blank=True)
    S_days = models.CharField(max_length=50,null=True,blank=True)
    S_Description = models.CharField(max_length=500, null=True, blank=True)
    S_Price = models.IntegerField(null=True, blank=True)
    S_Image = models.ImageField(upload_to="image", null=True, blank=True)

    def __str__(self):
        return self.S_Name
