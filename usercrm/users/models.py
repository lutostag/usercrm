from django.db import models
from .validators import validate_address, validate_phone


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(validators=[validate_phone], max_length=15,
                                    blank=True)
    address = models.CharField(validators=[validate_address], max_length=255,
                               blank=True)

    def __str__(self):
        return '%s, %s: (%s) @ %s' % (self.last_name, self.first_name,
                                      self.phone_number, self.address)

    class Meta:
        unique_together = (('first_name', 'last_name', 'phone_number'),)
