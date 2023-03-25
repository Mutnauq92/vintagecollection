from django.db import models
from django.conf import settings

# Create your models here.
class Car(models.Model):
    "Creates a car model"
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    car_pic = models.ImageField("%s" % "Image")
    engine_size = models.CharField("%s" % "Engine Size", max_length=200)
    engine_configuration = models.CharField("%s" % "Engine Configuration", max_length=20)
    horsepower = models.CharField("%s" % "Horse Power", max_length=20)
    torque = models.CharField("%s" % "Torque", max_length=20)
    transmission = models.CharField("%s" % "Transmission", max_length=50)
    production_year = models.DateField("%s" % "Year")

    def __str__(self):
        return self.model
    
class CarGallery(models.Model):
    "Links car gallery to car model"
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_pics = models.ImageField("%s" % "Image")
    path_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.path_name