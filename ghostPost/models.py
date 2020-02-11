from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    CHOICES = (
        (1, 'Boast'),
        (0, 'Roast')
        )
    title = models.CharField(max_length=50)
    boast_or_roast = models.BooleanField(default=True, choices=CHOICES)
    upordown = models.IntegerField(default=0)
    content = models.TextField()
    total = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
