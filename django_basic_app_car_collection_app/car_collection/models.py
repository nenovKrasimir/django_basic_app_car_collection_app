from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(blank=False, max_length=10)
    email = models.EmailField(blank=False)
    age = models.IntegerField(blank=False, validators=[MinValueValidator(18)])
    password = models.CharField(blank=False, max_length=30)
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    profile_picture = models.URLField

    def __str__(self):
        return f"Username: {self.username}"
class Car(models.Model):
    TYPES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )

    type = models.CharField(blank=False, choices=TYPES)
    model = models.CharField(blank=False, max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(blank=False, validators=[
        MinValueValidator(1980, message="Year must be between 1980 and 2049"),
        MaxValueValidator(2049, message="Year must be between 1980 and 2049")
    ])
    image_url = models.URLField(blank=False)
    price = models.FloatField(blank=False, validators=[MinValueValidator(1)])
