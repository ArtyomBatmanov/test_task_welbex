from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, related_name='pick_up_location', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(Location, related_name='delivery_location', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
    description = models.CharField(max_length=1024, default='')


class Car(models.Model):
    car_number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lifting_capacity = models.PositiveIntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
