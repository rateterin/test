from django.db import models
from django.utils.crypto import get_random_string


class Links(models.Model):
    link = models.CharField(max_length=60)
    short = models.CharField(
        max_length=12,
        default=get_random_string(12, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'),
        unique=True)
    active = models.BooleanField(default=False)
