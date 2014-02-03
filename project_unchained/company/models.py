from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Company(models.Model):
    name = models.CharField(max_length=60)
    www = models.CharField(max_length=60)
    admin = models.ForeignKey(User, blank=True, null=True)
    public = models.BooleanField()
    
    def __unicode__(self):
        return self.name
