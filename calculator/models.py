from django.db import models
from django.urls import reverse

# Create your models here.


class Search(models.Model):
    zip = models.CharField(max_length=5)
    snow_days_this_year = models.PositiveIntegerField(default=0)

    PUBLIC = 'PU'
    URBAN_PUBLIC = 'UP'
    RURAL_PUBLIC = 'RP'
    PRIVATE = 'PR'
    BOARDING = 'BO'

    SCHOOLTYPE_CHOICES = [
        (PUBLIC, 'Public'),
        (URBAN_PUBLIC, 'Urban Public'),
        (RURAL_PUBLIC, 'Rural Public'),
        (PRIVATE, 'Private'),
        (BOARDING, 'Boarding'),
    ]

    school_type = models.CharField(
        max_length=2,
        choices=SCHOOLTYPE_CHOICES,
        default=PUBLIC,
    )
