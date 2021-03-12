from django.db import models

# Create your models here.
class Destination(models.Model):
    dest_name =models.CharField(max_length=100)
    desc =models.CharField(max_length=200)
    img= models.ImageField(upload_to="pics",default="image/bali.jpg")
    price =models.IntegerField()
    offer =models.BooleanField(default=False)