from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Bicycle(models.Model):
    name = models.CharField(max_length=150)
    is_available = models.BooleanField(default=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    booking_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
