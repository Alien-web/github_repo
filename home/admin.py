from django.contrib import admin
from .models import Destination
from accounts.models import Booking
# Register your models here.
admin.site.register(Destination)
admin.site.register(Booking)