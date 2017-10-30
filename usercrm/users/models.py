from django.db import models
from .validators import validate_address, validate_phone


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_nunber = models.CharField(validators=[validate_phone], max_length=15,
                                    blank=True)
    address = models.CharField(validators=[validate_address], max_length=255,
                               blank=True)
