from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=40)
    desciption = models.CharField(max_length=200)
    location = models.CharField(max_length=60)
    code = models.CharField(max_length=12,unique=True)
    

    def __str__(self):
        return self.name
