from django.contrib import admin
from .models import Operator, DroneShot, Booking, Location, Customer

# Register your models here.

admin.site.register(Operator)
admin.site.register(DroneShot)
admin.site.register(Booking)
admin.site.register(Location)
admin.site.register(Customer)
