from django.contrib import admin
from .models import User, UserEntityRelation
# Register your models here.
admin.site.register([User, UserEntityRelation])
