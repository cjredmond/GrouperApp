from django.db import models
from group.models import Entity
from django.utils import timezone

class Alert(models.Model):
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    expiration_time = models.DateTimeField()

    @property
    def is_expired(self):
        if self.expiration_time < timezone.now():
            return True
