from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join
from settings import MEDIA_ROOT

class Board(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=60)
    column_start = models.BooleanField()
    column_end = models.BooleanField()
    workflow_free = models.BooleanField()
    workflow_next = models.ForeignKey(Status)
    board = models.ForeignKey(Board)
    
    def __unicode__(self):
        return self.title

class Column(models.Model):
    title = models.CharField(max_length=60)
    status = models.ForeignKey(Status)
    
    def __unicode__(self):
        return self.title

class Priority(models.Model):
    title = models.CharField(max_length=60)
    board = models.ForeignKey(Board)
    
    def __unicode__(self):
        return self.title

class TicketStatus(models.Model):
    title = models.CharField(max_length=60)
    board = models.ForeignKey(Board)
    
    def __unicode__(self):
        return self.title

class Ticket(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000)
    creator = models.ForeignKey(User, blank=True, null=True)
    board = models.ForeignKey(Board)
    column = models.ForeignKey(Column)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey(Priority)
    status = models.ForeignKey(TicketStatus)
    open = models.BooleanField()
    
    def __unicode__(self):
        return self.title
    
    

class Comment(models.Model):
    comment = models.TextField(max_length=10000)
    creator = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket)
    
    def __unicode__(self):
        return self.comment
    
