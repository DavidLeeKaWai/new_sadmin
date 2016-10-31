#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-08-30 by liufeily@163.com

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render

@login_required
def Home(request):
   return render(request,'home.html')

def About(request):
   return render(request,'about.html')
