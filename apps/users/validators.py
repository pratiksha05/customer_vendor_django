from django.core.validators import RegexValidator

YEARREGEX = RegexValidator(
    r'^\+?1?\d{4,4}$', 'Only numbers are allowed.'
)
PHONEREGEX = RegexValidator(
    regex=r'^\+?1?\d{9,13}$',
    message="Phone number must be entered in the format: '+9199999999'. Up to 12 digits allowed."
)
CHARREGEX = RegexValidator(
    r'^[a-zA-Z ]+$', 'Only Alphabets are allowed.'
)