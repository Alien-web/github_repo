from django.db import models

# Create your models here.
class Booking(models.Model):
    user_id=models.IntegerField()
    dest_id=models.IntegerField()
    def __str__(self):
     return ' '.join([
        self.user_id,
        self.dest_id,
                     ])