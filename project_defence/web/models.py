from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_first_name


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2), validate_first_name]
    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
        validators=[MinLengthValidator(1), validate_first_name]
    )
    email = models.EmailField(
        max_length=40,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[MinLengthValidator(8)]
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )
