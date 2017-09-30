# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Flags(models.Model):
       name = models.CharField(max_length=8,unique = True)
       flid = models.IntegerField()
       def __unicode__(self):
             return self.name

class Article(models.Model):
       name = models.CharField(max_length = 30)
       date = models.DateTimeField()
       flag = models.ManyToManyField(Flags,related_name = "flag_article")
       art = models.TextField()
       jianjie = models.TextField()
       artid = models.IntegerField(unique = True) 
       jpg = models.ImageField(upload_to = 'statics/images')
       def __unicode__(self):
             return self.name

class Comment(models.Model):
       article = models.ForeignKey(Article,related_name='com')
       date = models.DateTimeField(auto_now=True)
       commenttext = models.TextField()
       commentname = models.CharField(max_length = 8)
       def __unicode__(self):
             return self.commentname