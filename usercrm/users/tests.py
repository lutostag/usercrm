from django.test import TestCase
from .validators import validate_address, validate_phone
from django.core.exceptions import ValidationError


class ValidateAddressTest(TestCase):
    def test_validate(self):
        good_address = '1510 S. Heatherwilde Blvd, Austin, TX 78660'
        bad_address = '1510 S. Heatherwilde Blvd'
        self.assertEquals(validate_address(good_address), None)
        self.assertRaises(ValidationError, validate_address, bad_address)


class ValidatePhoneTest(TestCase):
    def test_validate(self):
        good_number = '8323901881'
        bad_numbers = [
            'Not a number',
            '81234123413513412341234',
        ]
        self.assertEquals(validate_phone(good_number), None)
        for bad_number in bad_numbers:
            self.assertRaises(ValidationError, validate_phone, bad_number)
