from django.db import models
from .validators import validate_address, validate_phone


class Phone(models.Model):
    number = models.CharField(validators=[validate_phone], max_length=15,
                              unique=True, blank=True)

    def __str__(self):
        return self.number


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_numbers = models.ManyToManyField(
        Phone, null=True, blank=True, default=None,
        related_name='users')
    address = models.CharField(validators=[validate_address], max_length=255,
                               blank=True)

    def __str__(self):
        return '%s, %s: (%s) @ %s' % (
                self.last_name,
                self.first_name,
                ', '.join([str(number) for number in self.phone_numbers.all()]),
                self.address)
