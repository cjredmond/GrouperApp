from django.db import models
from group.models import Entity
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE)
    time = models.DateTimeField()
    description = models.TextField()
    urgent = models.BooleanField(default=False)
    sticky = models.BooleanField(default=False)

    @property
    def is_expired(self):
        if self.time < timezone.now() + timedelta(hours=1):
            return True
