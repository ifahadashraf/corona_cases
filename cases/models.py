from django.db import models
from django.utils import timezone


class Case(models.Model):
    name = models.CharField(max_length=255, null=False)
    nic = models.CharField(max_length=13, null=False)
    age = models.IntegerField(null=False)
    city = models.CharField(max_length=128, null=False)
    address = models.TextField(null=False)
    travel_history = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
