from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver 
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError

class Company(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    _www = models.CharField(max_length=60, blank=False)
    admin = models.ForeignKey(User, blank=True, null=True)
    public = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
    def clean(self):
        if '.' not in self.www:
            raise ValidationError("www address must contain dot (.)")
    
    @property
    def www(self):
        return self._www
    
    @www.setter
    def www(self, value):
        if not value.startswith("https://") or not value.startswith("https://"):
            self._www = "http://%s" % value
        else:
            self._www = value
    