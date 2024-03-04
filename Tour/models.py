from django.db import models

# Create your models here.
class PackagesDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="image", null=True, blank=True)