# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Project(models.Model):
    _project_unix_name = models.CharField(max_length=14, blank=False, unique=True)
    project_name = models.CharField(max_length=14, blank=False, unique=True)
    members = models.ManyToManyField(User)
    project_description = models.TextField()
    
    
    def save(self, *args, **kwargs):
        if not self._project_unix_name and self.project_name:
            self.project_unix_name = self.format_to_unix_name(self.project_name)
        super(Project, self).save(*args, **kwargs)
    
    @property
    def project_unix_name(self):
        return self._project_unix_name
    
    @project_unix_name.setter
    def project_unix_name(self, value):
        if value:
            self._project_unix_name = self.format_to_unix_name(value)
            
    def format_to_unix_name(self, value):
        value = value.lower().replace('ä', 'a').replace('å', 'a').replace('ö', 'o').replace(' ', '_')
        return value