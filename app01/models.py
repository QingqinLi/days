from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=32)
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    role = models.ForeignKey('Role')