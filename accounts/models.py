from django.db import models

# Create your models here.
class Booking(models.Model):
    user_id=models.IntegerField()
    dest_id=models.IntegerField()
