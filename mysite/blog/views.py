# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.template import RequestContext
from models import *
from django.views.decorators.csrf import *
import re
import datetime

# Create your views here.
def index(request):
       articlelist = Article.objects.all()
       return render_to_response('index.html',{'artlist':articlelist})

def check(request,ArticleId):
       try:
           article = Article.objects.filter(artid = ArticleId)
       except:
           return render_to_response('404.html')
       else:
           flags = article[0].flag.all()
           commentlist = article[0].com.all()
           commentlist = commentlist.order_by("date")
           return render_to_response('article.html',{'article':article[0],
                                                     'flag':flags,
                                                     'commentlist':commentlist})


def flagcheck(request,FlagId):
       try:
           flag = Flags.objects.filter(flid = FlagId) 
       except:   
           return render_to_response('404.html')
       else:
           articlelist = flag[0].flag_article.all().order_by("date")
           return render_to_response('index.html',{'artlist':articlelist})    
      

def about(request):
          return render_to_response('about.html')

@csrf_protect
@csrf_exempt
def reply(request,ArticleId):
                    newcomment = Comment()
                    newcomment.commentname = request.POST["name"]
                    newcomment.commenttext = request.POST["message"]
                    newcomment.article = Article.objects.filter(artid = ArticleId)[0]
                    newcomment.save()
                    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def page_not_found(request):
          return render_to_response('404.html')

