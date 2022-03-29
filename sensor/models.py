import imp
from django.db import models
from django.utils import timezone

# Create your models here.
class View(models.Model):
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)