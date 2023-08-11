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
    image = models.ImageField(default='avatar.jpg')
    username = models.CharField(
        max_length=16,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)]
    )

    def __str__(self):
        return self.first_name


class AddGames(models.Model):
    game_name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    image = models.URLField(
        blank=True,
        null=True
    )
    producer = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)]
    )
    description = models.TextField(
        blank=False,
        null=False
    )


class GiftCards(models.Model):
    your_name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    amount = models.FloatField(
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )


class AddExpert(models.Model):
    # CHECK_CHOICES = [
    #     "Gamer",
    #     "I <3 Games!",
    #     "Full Time",
    # ]
    name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    games_done = models.IntegerField(
        blank=True,
        null=True,
    )
    check_me = models.TextChoices("Gamer", "Full Time")

    description = models.TextField(
        blank=False,
        null=False
    )
    image = models.URLField(
        blank=True,
        null=True,
        default='static/images/avatar.jpg'
    )


class AddKeys(models.Model):
    name = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    price = models.FloatField(
        blank=False,
        null=False,
    )
    image = models.URLField(
        blank=True,
        null=True,
        default='static/images/avatar.jpg'
    )


class ProfileAdmin(models.Model):
    username = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2), validate_first_name]
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
