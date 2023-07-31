from django.core.exceptions import ValidationError


def validate_first_name(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

