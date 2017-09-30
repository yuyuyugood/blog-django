from django.db import models

class Flags(models.Model):
       name = models.CharField(unique = True)
       articlecount = models.IntegerField()

class Article(models.Model):
       name = models.CharField(max_length = 30)
       date = models.DateTimeField()
       time = models.TimeField()
       author = models.CharField(max_length = 8)
       flag = models.ManyToManyField(Flags)
       readcount = models.IntegerField()
       art = models.TextField()
       image = models.ImageField()

class comment(models.Model):
       article = models.ForeignKey(Article)
       comment_content = models.TextField()
       date = models.DateTimeField()
       commenttext = models.TextField()
       commentname = models.CharField(max_length = 8)

