from django.db import models
from django.utils import timezone

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
