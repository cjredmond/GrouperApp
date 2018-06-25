from django.db import models
from django.contrib.auth.models import AbstractUser
from group.models import Entity
from alerts.models import Alert

USER_LEVELS = [('s', 'super'), ('l', 'leader'), ('m', 'member')]

class User(AbstractUser):
    level = models.CharField(max_length=1,choices=USER_LEVELS)

    class Meta(object):
        unique_together = ('email',)

    def __str__(self):
        return self.username

    @property
    def get_alerts(self):
        ls = []
        for rel in self.userentityrelation_set.all():
            for alert in rel.entity.alert_set.all():
                if alert.is_expired == False:
                    ls.append(alert)
        return ls

    def get_events(self):
        ls = []
        for rel in self.userentityrelation_set.all():
            for event in rel.entity.event_set.all():
                ls.append(event)
        return ls

RELATION_TYPES = [('l', 'leader'), ('m', 'member')]

class UserEntityRelation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE)
    relation_type = models.CharField(max_length=1,choices=RELATION_TYPES,default='m')

    def __str__(self):
        return self.user.username + " " + self.entity.name
    # @property
    # def search_alerts(self):
    #     return [alert for alert in self.entity.alert_set.all()]
