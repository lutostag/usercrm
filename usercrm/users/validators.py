from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from postal.expand import expand_address
from postal.parser import parse_address


REQUIRED_ADDRESS_FIELDS = set([
    'city',
    'road',
    'postcode',
])


def validate_address(address):
    default_expansion = expand_address(address)[0]
    if len(default_expansion) > 255:
        raise ValidationError(
            'Address is too long, please limit to 255 characters')
    parsed = {item[1]: item[0] for item in parse_address(default_expansion)}
    known_keys = parsed.keys()
    if len(REQUIRED_ADDRESS_FIELDS - known_keys) > 0:
        raise ValidationError('Address does not have valid entries for: ' +
                              ', '.join(REQUIRED_ADDRESS_FIELDS - known_keys))


# phone number recommendation -- https://stackoverflow.com/a/19131360
validate_phone = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. "
            "Up to 15 digits allowed.")
