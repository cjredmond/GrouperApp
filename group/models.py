from django.db import models
from django.template.defaultfilters import slugify

class Entity(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=60)
    code = models.CharField(max_length=12,unique=True)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Entity, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
