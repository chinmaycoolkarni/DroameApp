from django.db import models
from django.utils import timezone


# Create your models here.

class Operator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    access = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'operator'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    mobileNo = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    aadhaarNo = models.CharField(max_length=12)
    addedBy = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer'


class DroneShot(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30)
    addedBy = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'drone_shot'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    addedBy = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'location'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    location_id = models.IntegerField()
    drone_shot_id = models.IntegerField()
    datetime = models.DateTimeField(null=False, default=timezone.now())
    totalRent = models.IntegerField()
    duration = models.IntegerField()
    addedBy = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'booking'
