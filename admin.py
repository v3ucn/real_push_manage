#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from models import *
from django.db.models import F
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
import StringIO
from PIL import *
from django import http
import ImageFile,Image, ImageDraw, ImageFont, md5, random,cStringIO
from django.shortcuts import render_to_response
from my import settings
import datetime,time
import sys,os
import json
import csv





def index(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 1
    date =''
    date1 = ''
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),~Q(xiupian = '1'),~Q(beijing = '1'),Q(review=0),Q(created=request.GET.get("date")),~Q(source = '麦考林') ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),~Q(xiupian = '1'),~Q(beijing = '1'),Q(review=0),~Q(source = '麦考林'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('index.html', locals())


def c10d(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 62
    date =''
    date1 = ''
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(created=request.GET.get("date")),~Q(source = '麦考林') ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),~Q(source = '麦考林'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('c10d.html', locals())


def c11d(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 63
    date =''
    date1 = ''
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=11),Q(created=request.GET.get("date")),~Q(source = '麦考林') ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=11),~Q(source = '麦考林'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('c11d.html', locals())


def zhualog(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 51
    date =''
    date1 = ''
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(created=request.GET.get("date")),~Q(source = '麦考林') ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),~Q(source = '麦考林'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('zhualog.html', locals())


def bianlog(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 53
    date =''
    date1 = ''

    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  storage group by user_id ") 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM user where user_id in (%s) " % cc
    books=User.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      date = request.GET.get("date")
    else:
      date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('bianlog.html', locals())



def tj_ft(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 53
    date =''
    date1 = ''

    cursor = connection.cursor()
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      date = request.GET.get("date")
    else:
      date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('tj_ft.html', locals())


def tj_dr(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 53
    date =''
    date1 = ''

    cursor = connection.cursor()
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      date = request.GET.get("date")
    else:
      date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('tj_dr.html', locals())


def tj_wd(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 53
    date =''
    date1 = ''

    cursor = connection.cursor()
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      date = request.GET.get("date")
    else:
      date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('tj_wd.html', locals())



def job_ft(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = -1
    date =''
    date1 = ''

    cursor = connection.cursor()
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      dd = request.GET.get("date")
    else:
      dd=  "2012-01"
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('job_ft.html', locals())



def job_dr(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = -1
    date =''
    date1 = ''

    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  storage group by user_id ") 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      dd = request.GET.get("date")
    else:
      dd=  "2012-01"
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('job_dr.html', locals())




def job_dan(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = -1
    date =''
    date1 = ''

    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  storage group by user_id ") 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      dd = request.GET.get("date")
    else:
      dd=  "2012-01"
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('job_dan.html', locals())


def job_huifu(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 90
    date =''
    date1 = ''

    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  storage group by user_id ") 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      dd = request.GET.get("date")
    else:
      dd=  "2012-01"
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('job_huifu.html', locals())


def job_wd(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = -1
    date =''
    date1 = ''

    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  storage group by user_id ") 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM editor group by realname "
    books=Editor.objects.raw(sql)
    books = tuple(books)

    if(request.GET.get("date")):
      dd = request.GET.get("date")
    else:
      dd=  "2012-01"
      #date = "%s%s%s" % ('&','date=',str(date2))



    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('job_wd.html', locals())




def excel(request):
 # Create the HttpResponse object with the appropriate CSV header.

 date123=request.GET.get("date")
 cursor = connection.cursor()
 cursor.execute(" SELECT * FROM  items where created = '%s' " % date123 ) 
 rows = cursor.fetchall()


 
 response = HttpResponse(mimetype='text/csv')
 response.write('\xEF\xBB\xBF')
 response['Content-Disposition'] = 'attachment; filename=wodfan.csv'

 writer = csv.writer(response)
 writer.writerow(['单品id', '来源', '标题'])

 for vs in range(len(rows)):
     r2=rows[vs][2]
     r2 = r2.encode('utf8')
     r4=rows[vs][4]
     r4 = r4.encode('utf8')
     writer.writerow([rows[vs][0], r2,r4])

 return response




def shouquan(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 12
    books=Items.objects.filter(  ~Q(item_id = '0'),~Q(xiupian = '1'),~Q(beijing = '1'),Q(review=0),~Q(source = '麦考林') ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('shouquan.html', locals())


def c10(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 60
    books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),~Q(source = '麦考林') ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('c10.html', locals())

def c11(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 61
    books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=11),~Q(source = '麦考林') ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('c11.html', locals())


def shoupei(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 54
    cursor = connection.cursor()
    

    cursor.execute(" SELECT * FROM  recommend where state = 0  order by position asc limit 8 ")
    row1=cursor.fetchall()

    cursor.execute(" SELECT * FROM  recommend where state = 2 order by position asc limit 4   ")
    row2=cursor.fetchall()


    cursor.execute(" SELECT * FROM  recommend where state = 1 order by position asc limit 4   ")
    row3=cursor.fetchall()


    cursor.execute(" SELECT * FROM  recommend where state = 3 order by position asc limit 3   ")
    row4=cursor.fetchall()

    cursor.execute(" SELECT * FROM  recommend_user  order by recommend_user_id limit 0,3   ")
    row5=cursor.fetchall()

    cursor.execute(" SELECT * FROM  recommend_user  order by recommend_user_id limit 3,4   ")
    row6=cursor.fetchall()

  

    


    

    return render_to_response('shoushe.html', locals())


def getdapei(request):
    value=request.GET.get("id")
    cursor = connection.cursor()        
    cursor.execute(" SELECT look_id FROM  collocation where collocation_id = '"+str(value)+"' limit 1 ") 
    row2 = cursor.fetchone()
    if row2 == None:
     return HttpResponse('1234')
    else :
     cid = row2[0]
    #return cid

    try:
     cursor.execute(" SELECT * FROM  looks where look_id = '"+str(cid)+"' limit 1 ") 
     row = cursor.fetchone()
     if row != None:
      imgstr=row[1]
      return HttpResponse(imgstr)
     else:
      return HttpResponse('123')
    except:
     return HttpResponse('123')


def getmabi(request):
    cursor = connection.cursor()
    value = request.GET.get("id")
    try:
         cursor.execute(" SELECT iscollocation,url FROM  figure where position = 0 and fashion_id = '"+str(value)+"' limit 1 ") 
         row = cursor.fetchone()    
    except:
         nimabi = '123'
    if row != None:
	    if(row[0]==1):
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
        nimabi = '123'
    	
    return HttpResponse(nimabi)


def gettouxiang(request):
    cursor = connection.cursor()
    value = request.GET.get("id")
    try:
         cursor.execute(" SELECT url FROM user where user_id = '%s' " % value ) 
         row = cursor.fetchone()    
    except:
         nimabi = '123'
    if row != None:
	 nimabi = '%s%s' % ("http://www.wodfan.com/images/avatar",row[0])
    else:
        nimabi = '123'
    	
    return HttpResponse(nimabi)


def getmabi1(request):
    cursor = connection.cursor()
    value = request.GET.get("id")
    try:
         cursor.execute(" SELECT iscollocation,url FROM  photo where position = 0 and talent_id = '"+str(value)+"' limit 1 ") 
         row = cursor.fetchone()    
    except:
         nimabi = '123'
    if row != None:
	    if(row[0]==1):
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
        nimabi = '123'
    	
    return HttpResponse(nimabi)

def getmabi3(request):
    cursor = connection.cursor()
    value = request.GET.get("id")
    try:
         cursor.execute(" SELECT iscollocation,url FROM  qaImages where position = 0 and qa_id = '"+str(value)+"' limit 1 ") 
         row = cursor.fetchone()    
    except:
         nimabi = '123'
    if row != None:
	    if(row[0]==1):
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      nimabi = "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
        nimabi = '123'
    	
    return HttpResponse(nimabi)


def getmabi2(request):
    value = request.GET.get("id")
    cursor = connection.cursor()
    tablename = 'item_image'
    cursor.execute(" SELECT image_id FROM  "+tablename+" where isdelete = 0 and item_id = '"+str(value)+"'") 
    rows = cursor.fetchall()
    ccff=''
    for key in rows:
     ccff+="%s%s" % (',',key[0])
    cchou=ccff.find(',')
    ccff=ccff[cchou+1:]
    ccff=ccff.strip()
    #return ccff
    row456='123'
    try:
     cursor.execute(" select * from images where position = 0   and  image_id in ("+ccff+") limit 1 ") 
     row456 = cursor.fetchone()
    except:
     try:
      cursor.execute(" select * from images where image_id in ("+ccff+") limit 1 ") 
      row456 = cursor.fetchone()
     except:
      row465='123'
     #row456='123'
    if (row456 != '123') and (row456 != None):
     #imgstr=row456[1]
     imgstr="%s%s" % ("http://ifan.me:8081/images",row456[1])
    else:
     imgstr='123'
    return HttpResponse(imgstr)


def chongshen(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 10
    date =''
    date1 = ''
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(created=request.GET.get("date")),~Q(source = '麦考林') ).order_by("-item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),~Q(source = '麦考林'),Q(created=str(date2)) ).order_by("-item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('chongshen.html', locals())


def chongshenq(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 11
    date =''
    date1 = ''
    if(request.GET.get("danid")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(item_id=request.GET.get("danid")),~Q(source = '麦考林') ).order_by("-item_id")
    else:     
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),~Q(source = '麦考林') ).order_by("-item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('chongshenq.html', locals())


def setyonghu(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 80
    date =''
    date1 = ''
    #if(request.GET.get("danid")):
    # books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(item_id=request.GET.get("danid")),~Q(source = '麦考林') ).order_by("-item_id")
    #else:     
    books=User.objects.filter(  ~Q(user_id = '0'),Q(role=1) ).order_by("-user_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('setyonghu.html', locals())

def yiyonghu(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 81
    date =''
    date1 = ''
    #if(request.GET.get("danid")):
    # books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(item_id=request.GET.get("danid")),~Q(source = '麦考林') ).order_by("-item_id")
    #else:     
    books=RecommendUser.objects.filter(  ~Q(user_id = '0'),Q(ishome=1) ).order_by("-user_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('yiyonghu.html', locals())


def yidan(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 13
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT item_id FROM recommend_item " ) 
     row = cursor.fetchall()
    except:
     row = '123'
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    if(cc):
            if(request.GET.get("danid")):	     
	     sql = "SELECT * FROM items where item_id = '%s' order by item_id desc " % request.GET.get("danid")
	    else:
	     sql = "SELECT * FROM items where item_id in (%s) order by item_id desc " % cc
	    books=Items.objects.raw(sql)
	    books = tuple(books)
	    #books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1),Q(item_id=request.GET.get("danid")),~Q(source = '麦考林') ).order_by("-item_id")
	    after_range_num = 5        #当前页前显示5页
	    befor_range_num = 4       #当前页后显示4页
	    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
	     page = int(request.GET.get("page",1))
	     if page < 1:
	      page = 1
	    except ValueError:
	     page = 1
	    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
	    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
	     books = paginator.page(page)
	    except(EmptyPage,InvalidPage,PageNotAnInteger):
	     books = paginator.page(paginator.num_pages)
	    if page >= after_range_num:
	     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	    else:
	     page_range = paginator.page_range[0:int(page)+befor_range_num]
	    
	    APP=request.META['SERVER_NAME']

    return render_to_response('yidan.html', locals())


def showallimg(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 11
    danid=request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" SELECT image_id FROM  item_image where item_id = %s " % str(danid) ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    sql = "SELECT * FROM images where image_id in (%s) " % cc
    books=Images.objects.raw(sql)
    books = tuple(books)
    #return HttpResponse(len(books))
        

    return render_to_response('showallimg.html', locals())


def setindex(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 5 
    books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=1) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('setindex.html', locals())


def setdapei(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 6
    tt=''
    if(request.GET.get("t")):
     tt="%s%s" % ('&t=',request.GET.get("t"))
     if request.GET.get("t") == 'remen':
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(activity_popular__gt = 0) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'zuixin' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'daren' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(istalent = 1) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'heji' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(isset = 1) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'zipai' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(isself = 1) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'jiepai' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(isstreet = 1) ).order_by("-collocation_id")
     elif request.GET.get("t") == 'mingxing' :
      books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(isstar = 1) ).order_by("-collocation_id")
    else:    
     books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0) ).order_by("-collocation_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('setdapei.html', locals())

def budapei(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 18
    books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),Q(theme = '') ).order_by("collocation_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('budapei.html', locals())


def bufenlei(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 56
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM  fan_theme  ")
    rowxiaofen=cursor.fetchall()

    cursor.execute(" SELECT fan_id FROM  fan_theme ")
    youzi=cursor.fetchall()

    imgstr=youzi
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    
    cursor.execute(" SELECT * FROM  fan where fan_id not in (%s) " % cc )
    wuzi=cursor.fetchall()



    if(request.GET.get("username")):
         
            #return HttpResponse(request.GET.get("username"))
	    try:
             cursor.execute(" SELECT user_id FROM  user where username = '%s'  " % request.GET.get("username") )
             uid=cursor.fetchone()
	    except:
	     return HttpResponse('没有这个用户')
	    
            cursor.execute(" SELECT collocation_id FROM  user_collocation where  isown = 1 and user_id = '%s'  " % uid[0] )
            clists=cursor.fetchall()

	    imgstr1=clists
            cc=''
            for key in imgstr1:
             cc+="%s%s" % (',',key[0])
            cchou=cc.find(',')
            cc=cc[cchou+1:]
	    #return HttpResponse(cc)
	    sql = "SELECT * FROM collocation where isdelete = 0  and collocation_id in (%s) order by collocation_id desc " % cc
	    books=Collocation.objects.raw(sql)
	    books = tuple(books)
            #return HttpResponse(len(books))
	    after_range_num = 5        #当前页前显示5页
	    befor_range_num = 4       #当前页后显示4页
	    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
	     page = int(request.GET.get("page",1))
	     if page < 1:
	      page = 1
	    except ValueError:
	     page = 1
	    paginator = Paginator(books,5000)   # 设置books在每页显示的数量，这里为2
	    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
	     books = paginator.page(page)
	    except(EmptyPage,InvalidPage,PageNotAnInteger):
	     books = paginator.page(paginator.num_pages)
	    if page >= after_range_num:
	     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	    else:
	     page_range = paginator.page_range[0:int(page)+befor_range_num]


	     


    else:
	    books=Collocation.objects.filter(  ~Q(collocation_id = '0'),Q(isdelete = 0),~Q(theme = '') ).order_by("-collocation_id")
	    after_range_num = 5        #当前页前显示5页
	    befor_range_num = 4       #当前页后显示4页
	    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
	     page = int(request.GET.get("page",1))
	     if page < 1:
	      page = 1
	    except ValueError:
	     page = 1
	    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
	    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
	     books = paginator.page(page)
	    except(EmptyPage,InvalidPage,PageNotAnInteger):
	     books = paginator.page(paginator.num_pages)
	    if page >= after_range_num:
	     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	    else:
	     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    

    return render_to_response('bufenlei.html', locals())


def feed(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 17
    books=Fashion.objects.filter(  ~Q(fashion_id = '0'),Q(isdelete = 0) ).order_by("-fashion_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('feed.html', locals())

def ftscore(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 17
    books=Fashion.objects.filter(  ~Q(fashion_id = '0'),Q(isdelete = 0) ).order_by("-fashion_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('ftscore.html', locals())

def wenda(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 70
    books=Qa.objects.filter(  ~Q(qa_id = '0'),Q(isdelete = 0) ).order_by("-qa_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('wenda.html', locals())

def daren(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 71
    books=Talent.objects.filter(  ~Q(talent_id = '0'),Q(isdelete = 0) ).order_by("-talent_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('daren.html', locals())


def drscore(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 71
    books=Talent.objects.filter(  ~Q(talent_id = '0'),Q(isdelete = 0) ).order_by("-talent_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('drscore.html', locals())


def blog(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 15
    books=Blog.objects.filter(  ~Q(blog_id = '0'),Q(isdelete = 0) ).order_by("-blog_id")

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('blog.html', locals())


def yidapei(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 14
    
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT target_id FROM recommend_feed where feed_type = 0 or feed_type = 1 " ) 
     row = cursor.fetchall()
    except:
     row = '123'
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    if(cc):
	    sql = "SELECT * FROM collocation where collocation_id in (%s) order by collocation_id desc " % cc
	    books=Collocation.objects.raw(sql)
	    books = tuple(books)
	    after_range_num = 5        #当前页前显示5页
	    befor_range_num = 4       #当前页后显示4页
	    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
	     page = int(request.GET.get("page",1))
	     if page < 1:
	      page = 1
	    except ValueError:
	     page = 1
	    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
	    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
	     books = paginator.page(page)
	    except(EmptyPage,InvalidPage,PageNotAnInteger):
	     books = paginator.page(paginator.num_pages)
	    if page >= after_range_num:
	     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	    else:
	     page_range = paginator.page_range[0:int(page)+befor_range_num]
	    
	    APP=request.META['SERVER_NAME']

    return render_to_response('yidapei.html', locals())


def yiblog(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 16
    
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT target_id FROM recommend_feed where feed_type = 2 " ) 
     row = cursor.fetchall()
    except:
     row = '123'
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #return HttpResponse(cc)
    if(cc):
	    sql = "SELECT * FROM blog where blog_id in (%s) order by blog_id desc " % cc
	    books=Blog.objects.raw(sql)
	    books = tuple(books)
	    after_range_num = 5        #当前页前显示5页
	    befor_range_num = 4       #当前页后显示4页
	    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
	     page = int(request.GET.get("page",1))
	     if page < 1:
	      page = 1
	    except ValueError:
	     page = 1
	    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
	    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
	     books = paginator.page(page)
	    except(EmptyPage,InvalidPage,PageNotAnInteger):
	     books = paginator.page(paginator.num_pages)
	    if page >= after_range_num:
	     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
	    else:
	     page_range = paginator.page_range[0:int(page)+befor_range_num]
	    
	    APP=request.META['SERVER_NAME']

    return render_to_response('yiblog.html', locals())


def judge(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 4
    books=Items.objects.filter(  ~Q(item_id = '0'),Q(review=7) ).order_by("-item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('judge.html', locals())

def xiupian(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set xiupian = 1,review = 2 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute("commit")
	#sort123=random.randrange(1,999999999)
	#cursor.execute(" update  "+tablename+" set sort = '"+str(sort123)+"' where item_id = '"+str(request.GET['id'])+"' ")
	#cursor.execute("commit") 
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def pass1(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 1 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def del1(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 6 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def dahui(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        #cursor.execute(" update  "+tablename+" set review = 0,beijing=0,xiupian=0 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute(" update  "+tablename+" set review = 2,beijing=0,xiupian=1 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)


def beijing(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set beijing = 1,review = 2 where item_id = '"+str(request.GET['id'])+"' ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def pixiu(request):
    if request.is_ajax():
        #return HttpResponse(str(request.GET['id']))
	fuckcaonima = str(request.GET['id'])
	fuckcaonima = fuckcaonima.split(",")
	#return HttpResponse(str(fuckcaonima[0]))
        cursor = connection.cursor()
        
	#for value in fuckcaonima:
	#    sort123=random.randrange(1,999999999)
	#    cursor.execute(" update  items set sort = '"+str(sort123)+"' where item_id = '"+str(value)+"' ")
	#    cursor.execute("commit")
	    

        tablename = 'items'
        cursor.execute(" update  "+tablename+" set xiupian = 1,review = 2 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def pipass(request):
    if request.is_ajax():
        cursor = connection.cursor()
	fuckcaonima = str(request.GET['id'])
	fuckcaonima = fuckcaonima.split(",")

	#for value in fuckcaonima:
	#    sort123=random.randrange(1,999999999)
	#    cursor.execute(" update  items set sort = '"+str(sort123)+"' where item_id = '"+str(value)+"' ")
	#    cursor.execute("commit")

        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 10 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)


def pipassc10d(request):
    if request.is_ajax():
        cursor = connection.cursor()
	fuckcaonima = str(request.GET['date'])
	
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 11 where created = '%s' " % fuckcaonima )
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)




def pipass1(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 11 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def pipass2(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 10 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)


def pidahui(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        #cursor.execute(" update  "+tablename+" set review = 0,beijing=0,xiupian=0 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute(" update  "+tablename+" set review = 2,beijing=0,xiupian=1 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)


def pidel(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 6 where item_id in( "+str(request.GET['id'])+") ")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)
 
def pibei(request):
    if request.is_ajax():
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set beijing = 1,review = 2 where item_id in ( "+str(request.GET['id'])+")")
	cursor.execute("commit")
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def fenpeix(request):
    if request.is_ajax():
        ids = request.GET['id']
	ids = ids.split(",")
	userid = str(request.GET['userid'])
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 3 where item_id in ( "+str(request.GET['id'])+")")
	cursor.execute("commit")
	for j in ids:
	 sql="insert into admin_job (`userid`,`type`,`date`,`itemid`) values ('%s','%s','%s','%s') " % (int(userid),1,time.time(),int(j))
	 cursor.execute(sql)	
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)

def fenpeib(request):
    if request.is_ajax():
        ids = request.GET['id']
	ids = ids.split(",")
	userid = str(request.GET['userid'])
        cursor = connection.cursor()
        tablename = 'items'
        cursor.execute(" update  "+tablename+" set review = 3 where item_id in ( "+str(request.GET['id'])+")")
	cursor.execute("commit")
	for j in ids:
	 sql="insert into admin_job (`userid`,`type`,`date`,`itemid`) values ('%s','%s','%s','%s') " % (int(userid),2,time.time(),int(j))
	 cursor.execute(sql)	
        message = "ok"
    else:
        message = "通信失败"
    return HttpResponse(message)
 
def x(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
    nav = 2
    userlist = AdminUser.objects.all().exclude(role=1)
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(xiupian = '1'),Q(review = '2'),Q(created=request.GET.get("date")) ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(xiupian = '1'),Q(review = '2'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]   
    APP=request.META['SERVER_NAME']
    return render_to_response('x.html', locals())

def xx(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '2') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
    nav = 1
    #itemids1 = AdminJob.objects.filter(userid=user.id)
    cursor = connection.cursor()
    sql = " select item_id from items  where review = 3 "
    cursor.execute(sql) 
    rs = cursor.fetchall()
    str=''
    for rsc in rs:
       str = str +'%s,' %  rsc[0]
    str = str.rstrip(',')
    if str == '':
     div1=''
     return render_to_response('xx.html', locals())
    sql = " select itemid from admin_job  where type = 1 and userid = %s and itemid in (%s) " % (user.id,str)
    cursor.execute(sql) 
    row = cursor.fetchall()
    str=''
    for rec in row:
       str = str +'%s,' %  rec[0]
    str = str.rstrip(',')
    #books=Items.objects.filter(  ~Q(item_id = '0'),Q(xiupian = '1'),Q(review = '3'),Q(item_id__in=[str]) ).order_by("item_id")
    div1="<input type=\"button\" onclick=\"down();\" value=\"点击下载所有修片任务图片\" \/>"
    if str == '':
     div1=''
     return render_to_response('xx.html', locals())
    sql = "SELECT * FROM items where xiupian = 1 and review = 3 and item_id in (%s) " % str
    books=Items.objects.raw(sql)
    books = tuple(books)
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]   
    APP=request.META['SERVER_NAME']
    return render_to_response('xx.html', locals())

def xb(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '2') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
    nav = 2
    #itemids1 = AdminJob.objects.filter(userid=user.id)
    cursor = connection.cursor()
    sql = " select item_id from items  where review = 3 "
    cursor.execute(sql) 
    rs = cursor.fetchall()
    str=''
    for rsc in rs:
       str = str +'%s,' %  rsc[0]
    str = str.rstrip(',')
    if str == '':
     div1=''
     return render_to_response('xx.html', locals())
    sql = " select itemid from admin_job  where type = 2 and userid = %s and itemid in (%s) " % (user.id,str)
    cursor.execute(sql) 
    row = cursor.fetchall()
    str=''
    for rec in row:
       str = str +'%s,' %  rec[0]
    str = str.rstrip(',')
    #books=Items.objects.filter(  ~Q(item_id = '0'),Q(xiupian = '1'),Q(review = '3'),Q(item_id__in=[str]) ).order_by("item_id")
    div1="<input type=\"button\" onclick=\"down();\" value=\"点击下载所有背景任务图片\" \/>"
    if str == '':
     div1=""
     return render_to_response('xb.html', locals())
    sql = "SELECT * FROM items where beijing = 1 and review = 3 and item_id in (%s) " % str
    books=Items.objects.raw(sql)
    books = tuple(books)
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]   
    APP=request.META['SERVER_NAME']
    return render_to_response('xb.html', locals())

def b(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')

    userlist = AdminUser.objects.all().exclude(role=1)
    nav = 3
    if(request.GET.get("date")):
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(beijing = '1'),Q(review = '2'),Q(created=request.GET.get("date")) ).order_by("item_id")
     date = "%s%s%s" % ('&','date=',request.GET.get("date"))
     date1=request.GET.get("date")
    else:
     date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = "%s%s%s" % ('&','date=',str(date2))
     date1=str(date2)
     books=Items.objects.filter(  ~Q(item_id = '0'),Q(beijing = '1'),Q(review = '2'),Q(created=str(date2)) ).order_by("item_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]   
    APP=request.META['SERVER_NAME']
    return render_to_response('b.html', locals())

def upload3(request):
    url = request.POST.get("url")
    item_id = request.POST.get("item_id")
    cursor = connection.cursor()
    #tablename = 'item_image'
    #cursor.execute(" SELECT * FROM  "+tablename+" where item_id =  "+str(item_id)) 
    #row = cursor.fetchone()
    tablename = 'items'
    cursor.execute(" update  "+tablename+" set xiupian = 0,review=4 where item_id =  '"+str(item_id)+"'")
    cursor.execute("commit")
    f = request.FILES.get('photo', None)
    parser = ImageFile.Parser()  
    for chunk in f.chunks():
     parser.feed(chunk)  
    img = parser.close()
    name = '%s%s' % (settings.STATIC_PATH, url)  ##这里的时保存文件的路径加名字！
    img.save(name)
    return http.HttpResponseRedirect('/x/')


def upload12(request):
    url = request.POST.get("url")
    item_id = request.POST.get("item_id")
    cursor = connection.cursor()
    #tablename = 'item_image'
    #cursor.execute(" SELECT * FROM  "+tablename+" where item_id =  "+str(item_id)) 
    #row = cursor.fetchone()
    tablename = 'items'
    cursor.execute(" update  "+tablename+" set beijing = 0,review=4 where item_id =  '"+str(item_id)+"'")
    cursor.execute("commit")
    f = request.FILES.get('photo', None)
    parser = ImageFile.Parser()  
    for chunk in f.chunks():
     parser.feed(chunk)  
    img = parser.close()
    name = '%s%s' % (settings.STATIC_PATH, url)  ##这里的时保存文件的路径加名字！
    img.save(name)
    return http.HttpResponseRedirect('/b/')


def setindexupdate(request):
    activity_popular = request.POST.get("activity_popular")
    item_id = request.POST.get("item_id")
    cursor = connection.cursor()
    tablename = 'items'
    cursor.execute(" update  "+tablename+" set activity_popular = %s where item_id = %s " % (activity_popular,item_id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/setindex/')

def pictpaixu(request):
    position = request.POST.get("position")
    pict_id = request.POST.get("pict_id")
    mid = request.POST.get("mid")
    cursor = connection.cursor()
    cursor.execute(" update  pictorial set position = '%s' where pictorial_id = '%s' " % (position,pict_id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/pictlist/?mid='+mid)

def setdapeiupdate(request):
    activity_popular = request.POST.get("activity_popular")
    item_id = request.POST.get("collocation_id")
    cursor = connection.cursor()
    tablename = 'collocation'
    cursor.execute(" update  "+tablename+" set activity_popular = %s where collocation_id = %s " % (activity_popular,item_id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/setdapei/')


def test(request):
    list = Items.objects.get(item_id=1)
    return HttpResponse(str(time.strftime('%Y-%m-%d %H : %M : %S',time.localtime(1306206489))))

def login(request):
    return render_to_response('login.html', locals())

def checkcode(request):
    im = Image.new('RGBA',(52,18),(50,50,50,50))
    draw = ImageDraw.Draw(im)
    rands = random.randint(1000,9999)
    rands = random.randint(1000,9999)
    rands = str(rands)
    rands = tuple(rands)
    ziti = "%s%s" % (settings.STATIC_PATH1,'/tahomabd.TTF') 
    draw.text((2,0), rands[0], font=ImageFont.truetype(ziti, random.randrange(12,18)), fill='white')
    draw.text((14,0), rands[1], font=ImageFont.truetype(ziti, random.randrange(12,18)), fill='yellow')
    draw.text((27,0), rands[2], font=ImageFont.truetype(ziti, random.randrange(12,18)), fill='yellow')
    draw.text((40,0), rands[3], font=ImageFont.truetype(ziti, random.randrange(12,18)), fill='white')  
    del draw
    request.session['checkcode'] = rands
    request.session.set_expiry(0)
    buf = cStringIO.StringIO()
    im.save(buf, 'gif')
    return HttpResponse(buf.getvalue(),'image/gif')
    #return HttpResponse(rands[0])

def checklogin(request):
    import hashlib
    
    vac="".join(request.session.get('checkcode'))
    vas=str(request.GET.get("checkcode"))
    if vac <> vas :
     return HttpResponse('验证码错误')
    password = request.GET.get("password")    
    m = hashlib.md5(password)
    m.digest()
    psd = m.hexdigest()
    try:
     list = AdminUser.objects.get(password=psd,username=request.GET.get("username"))
     request.session['checkuser'] = str(list.username)
     request.session['checkrole'] = str(list.role)
     request.session['uid'] = str(list.id)
     request.session.set_expiry(0)
     return HttpResponse(str(list.role))
    except:
     return HttpResponse('用户名或者密码错误')


def RemoveNonNullDirectory (top):
    import os
    """ 
    Remove non-null directory
    """
    while 1:
        if os.path.exists(top):
            if len(os.listdir(top)) == 0:
                os.rmdir (top)
                break
            else:
                for root, dirs, files in os.walk(top, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
        else:
            break


def down(request):
    import zipfile, os,shutil
    user = AdminUser.objects.get(username=request.session.get('checkuser'))
    cursor = connection.cursor()
    sql = " select item_id from items  where review = 3 "
    cursor.execute(sql) 
    rs = cursor.fetchall()
    str=''
    for rsc in rs:
       str = str +'%s,' %  rsc[0]
    str = str.rstrip(',')
    if request.GET.get("cc"):
     if request.GET.get("ccs"):
      if request.GET.get("type") == '1':
       sql = " select item_id from items  where  xiupian = 1 and review = 2 and item_id in (%s)  " %  request.GET.get("ccs")
      else:
       sql = " select item_id from items  where  beijing = 1 and review = 2 and item_id in (%s) " %  request.GET.get("ccs")
     else:
      if request.GET.get("type") == '1':
       sql = " select item_id from items  where  xiupian = 1 and review = 2  " 
      else:
       sql = " select item_id from items  where  beijing = 1 and review = 2 "
    else :
     if request.GET.get("type") == '1':
      sql = " select itemid from admin_job  where userid = %s and type = 1 and itemid in (%s) " % (user.id,str)
     else:
      sql = " select itemid from admin_job  where userid = %s and type = 2 and itemid in (%s) " % (user.id,str)
    cursor.execute(sql) 
    row = cursor.fetchall()
    str=''
    for rec in row:
       str = str +'%s,' %  rec[0]
    str = str.rstrip(',')
    sql = " select image_id from item_image  where isdelete = 0 and item_id in ( %s ) " % str
    cursor.execute(sql) 
    row1 = cursor.fetchall()
    str=''
    for rec1 in row1:
       str = str +'%s,' %  rec1[0]
    str = str.rstrip(',')
    sql = " select * from  images  where  image_id in ( %s ) " % str
    cursor.execute(sql) 
    row2 = cursor.fetchall()
    str=''
    directory= '%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id)
    if os.path.exists(directory) == False:
     os.mkdir(directory)
    else:
     RemoveNonNullDirectory(directory)
     os.mkdir(directory)
    for rec2 in row2:
       #str = str +'%s,' %  rec2[1]
       target="%s%s" % (settings.STATIC_PATH,rec2[1])
       sc = "%s" % (rec2[1])
       sc2 = "%s" % (rec2[0])
       schou = sc.rfind('.')
       scjie = sc[schou:]
       scxin = "%s%s" % (sc2,scjie)
       sc = sc.replace('/','#')
       #xiabiao = sc.rfind('/')
       #xiabiao = xiabiao + 1
       #sc = sc[xiabiao:]
       sc1 = "%s%s%s" % (directory,"/",scxin)
       shutil.copy(target, sc1)
    filename = '%s%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id,".zip")
    testdir = '%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id)
    z = zipfile.ZipFile(filename, 'w',true)
    if os.path.isdir(testdir):
     for d in os.listdir(testdir):
      z.write(testdir+os.sep+d)
    z.close()
    sql="%s%s%s" % ("/zip/zip",user.id,".zip")
    return HttpResponse(sql)


def down2(request):
    import zipfile, os,shutil
    user = AdminUser.objects.get(username=request.session.get('checkuser'))
    cursor = connection.cursor()    
    #return HttpResponse(str)
    if request.GET.get("type") == '1':
     sql = " select item_id from items  where  xiupian = 1 and review = 2 and created = '%s'  " %  request.GET.get("date")
    else:
     sql = " select item_id from items  where  beijing = 1 and review = 2 and created = '%s' " %  request.GET.get("date")    
    cursor.execute(sql) 
    row = cursor.fetchall()
    str=''
    for rec in row:
       str = str +'%s,' %  rec[0]
    str = str.rstrip(',')
    sql = " select image_id from item_image  where item_id in ( %s ) " % str
    cursor.execute(sql) 
    row1 = cursor.fetchall()
    str=''
    for rec1 in row1:
       str = str +'%s,' %  rec1[0]
    str = str.rstrip(',')
    sql = " select * from  images  where image_id in ( %s ) " % str
    cursor.execute(sql) 
    row2 = cursor.fetchall()
    str=''
    directory= '%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id)
    if os.path.exists(directory) == False:
     os.mkdir(directory)
    else:
     RemoveNonNullDirectory(directory)
     os.mkdir(directory)
    for rec2 in row2:
       #str = str +'%s,' %  rec2[1]
       target="%s%s" % (settings.STATIC_PATH,rec2[1])
       sc = "%s" % (rec2[1])
       sc2 = "%s" % (rec2[0])
       schou = sc.rfind('.')
       scjie = sc[schou:]
       scxin = "%s%s" % (sc2,scjie)
       sc = sc.replace('/','#')
       #xiabiao = sc.rfind('/')
       #xiabiao = xiabiao + 1
       #sc = sc[xiabiao:]
       sc1 = "%s%s%s" % (directory,"/",scxin)
       shutil.copy(target, sc1)
    filename = '%s%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id,".zip")
    testdir = '%s%s%s' % (settings.STATIC_PATHZIP, "/zip",user.id)
    z = zipfile.ZipFile(filename, 'w')
    if os.path.isdir(testdir):
     for d in os.listdir(testdir):
      z.write(testdir+os.sep+d)
    z.close()
    sql="%s%s%s" % ("/zip/zip",user.id,".zip")
    return HttpResponse(sql)


def upload(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')

    nav = 7
    url = settings.STATIC_URL
    uuid = request.session.get('uid')
    return render_to_response('upload.html', locals())


def uploadfy(request):
    #if request.FILES:
    # return HttpResponse("123")   
    file_obj = request.FILES.get('Filedata', None)
    #return HttpResponse(file_obj)
    fname=file_obj.name
    fnamehou=fname.rfind('.')
    #fnamehou=fnamehou-1;
    fnamejie=fname[0:fnamehou]
    #return HttpResponse(fnamejie)
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM  images where image_id = '"+str(fnamejie)+"' limit 1 ") 
    row3 = cursor.fetchone()    
    fnamex=row3[1]
    #fnamex=fname.replace('#','/')
    fnamec = fnamex
    xiabiao = fnamex.rfind('/')
    xiabiao = xiabiao + 1
    sc = fnamec[xiabiao:]
    #return HttpResponse(fnamex)
    parser = ImageFile.Parser()  
    for chunk in file_obj.chunks():
     parser.feed(chunk)  
    img = parser.close()
    name = '%s/%s' % (settings.STATIC_PATHNEW, sc)
    #return HttpResponse(name)
    img.save(name)
    try:
     os.system(" chmod -R 777 /home/liuyue/ly.sh ")
     os.system(" chmod -R 777 /home/liuyue/ly.sh ")
     os.system(" sudo /home/liuyue/ly.sh ")
     os.system(" sudo /home/liuyue/ly.sh ")
     os.system(" sudo /home/liuyue/ly.sh ")

    except:
     ss=1
    #os.chmod(name,stat.S_IXOTH|stat.S_IXGRP|stat.S_IXUSR) 
    cursor.execute(" SELECT * FROM  images where url = '"+str(fnamex)+"' limit 1 ") 
    row = cursor.fetchone()
    cursor.execute(" SELECT * FROM  item_image where image_id = '"+str(row[0])+"' limit 1 ") 
    row1 = cursor.fetchone()
    uuid = request.GET.get("folder")
    uuid = str(uuid)
    uuid=uuid.replace('/upload/','')
    cursor.execute(" insert into  live_img (`image_id`,`item_id`) values ('%s','%s') " % (row[0],row1[1]) )
    cursor.execute("commit")
    cursor.execute(" SELECT image_id FROM  live_img where item_id = '"+str(row1[1])+"'") 
    rows = cursor.fetchall()
    ccff=''
    for key in rows:
     ccff+="%s%s" % (',',key[0])
    cchou=ccff.find(',')
    ccff=ccff[cchou+1:]
    cursor.execute(" SELECT image_id FROM  item_image where item_id = '"+str(row1[1])+"'") 
    rows = cursor.fetchall()
    ggcc=''
    for key in rows:
     ggcc+="%s%s" % (',',key[0])
    gghou=ggcc.find(',')
    ggcc=ggcc[gghou+1:]
    cursor.execute(" insert into  uploadlog (`uid`,`date`,`itemid`) values ('%s','%s','%s') " % (uuid,int(time.time()),int(row1[1])) )
    cursor.execute("commit")
    cursor.execute(" update  items set review = 7 where item_id = '"+str(row1[1])+"' ")
    cursor.execute("commit")
    try:
     cursor.execute(" update item_image set isdelete = 1 where image_id  in (%s) and image_id not in (%s) " % (ggcc,str(ccff)) )
     cursor.execute("commit")
    except:
     chj='123'
    try:
     cursor.execute(" update item_image set isdelete = 0 where image_id  in (%s) and image_id in (%s) " % (ggcc,str(ccff)) )
     cursor.execute("commit")
    except:
     chj='123'
    
    return HttpResponse(fname)




def uploadfy1(request):
    #if request.FILES:
    # return HttpResponse("123")   
    file_obj = request.FILES.get('Filedata', None)
    #return HttpResponse(file_obj)
    fname=file_obj.name
    #fnamex=fname.replace('#','/')
    #fnamec = fname
    #xiabiao = fnamex.rfind('/')
    #xiabiao = xiabiao + 1
    #sc = fnamec[xiabiao:]
    #return HttpResponse(fnamex)
    parser = ImageFile.Parser()  
    for chunk in file_obj.chunks():
     parser.feed(chunk)  
    img = parser.close()
    fname="%s%s%s" % (int(time.time()),random.randint(0,100),fname)
    fnamehou=fname.rfind('.')
    fnamejie=fname[0:fnamehou]
    fnamesuo="%s%s%s" % (fnamejie,"_210x117",".jpg")
    fnamewan='%s/%s' % (settings.STATIC_PATH2, fnamesuo)
    name = '%s/%s' % (settings.STATIC_PATH2, fname)
    #return HttpResponse(name)
    img.save(name)
    size = 290, 124
    im = Image.open(name)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(fnamewan, "JPEG")
    #cursor = connection.cursor()
    #cursor.execute(" SELECT * FROM  images where url = '"+str(fnamex)+"' limit 1 ") 
    #row = cursor.fetchone()
    #cursor.execute(" SELECT * FROM  item_image where image_id = '"+str(row[0])+"' limit 1 ") 
    #row1 = cursor.fetchone()
    #cursor.execute(" update  items set review = 1 where item_id = '"+str(row1[1])+"' ")
    #cursor.execute("commit")
    

    return HttpResponse(fname)


def logout(request):
    try:
        del request.session['checkuser']
	del request.session['checkrole']
    except KeyError:
        pass
    return HttpResponse("ok")


def maglist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 8
    books=Magazine.objects.filter(  ~Q(magazine_id = '0') ).order_by("-magazine_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('mag.html', locals())

def fllist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 56
    books=Fan.objects.filter(  ~Q(fan_id = '0') ).order_by("-fan_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    APP=request.META['SERVER_NAME']
    return render_to_response('fllist.html', locals())

def zilist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 55
    books=FanTheme.objects.filter(  ~Q(fan_theme_id = '0') ).order_by("-fan_theme_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    APP=request.META['SERVER_NAME']
    return render_to_response('zilist.html', locals())

def pictlist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
    cursor = connection.cursor()

    cursor.execute(" SELECT * FROM  magazine where magazine_id != 0 order by magazine_id desc ")
    row1234=cursor.fetchall()
    
    
    cursor.execute(" SELECT * FROM  magazine order by magazine_id desc limit 1 ") 
    rs = cursor.fetchone()
    mid = rs[0]
    nav = 9
    if(request.GET.get("mid")):
     books=Pictorial.objects.filter(  ~Q(pictorial_id = '0'),Q(magazine_id = request.GET.get("mid") ) ).order_by("-pictorial_id")
     mid = request.GET.get("mid")
    else:
     books=Pictorial.objects.filter(  ~Q(pictorial_id = '0'),Q(magazine_id = mid )).order_by("-pictorial_id")
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,130)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('pictlist.html', locals())

def yipictlist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 9
    cursor = connection.cursor()
    cursor.execute(" select pictorial_id from  recommend_pictorial " )
    rows3=cursor.fetchall()
    cc=''
    for key in rows3:
      cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #books=Pictorial.objects.filter(  ~Q(pictorial_id = '0') ).order_by("-pictorial_id")
    sql = "SELECT * FROM pictorial where pictorial_id in (%s) " % cc
    books=Pictorial.objects.raw(sql)
    books = tuple(books)

    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('yipictlist.html', locals())

def weipictlist(request):
    if (request.session.get('checkuser') == None) or (request.session.get('checkrole') == None) or (request.session.get('checkrole') != '1') :
     return http.HttpResponseRedirect('/login')
    else :
     try:
      user = AdminUser.objects.get(username=request.session.get('checkuser'))
     except:
      return http.HttpResponseRedirect('/login')
     
    nav = 9
    cursor = connection.cursor()
    cursor.execute(" select pictorial_id from  recommend_pictorial " )
    rows3=cursor.fetchall()
    cc=''
    for key in rows3:
      cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    #books=Pictorial.objects.filter(  ~Q(pictorial_id = '0') ).order_by("-pictorial_id")
    sql = "SELECT * FROM pictorial where pictorial_id not in (%s) " % cc
    books=Pictorial.objects.raw(sql)
    books = tuple(books)
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,30)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]
    
    APP=request.META['SERVER_NAME']

    return render_to_response('weipictlist.html', locals())


def delmag(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" delete from  magazine  where magazine_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def delfl(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" delete from  fan  where fan_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def delzi(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" delete from  fan_theme  where fan_theme_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def kaiqi(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" update  feed set ishome = 1  where feed_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def guanbi(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" update  feed set ishome = 0  where feed_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def xianshimag(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" update  magazine set ishome = 1  where magazine_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def guanbimag(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" update  magazine set ishome = 0  where magazine_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def delpict(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" delete from  pictorial  where pictorial_id = %s " % (id))
    cursor.execute("commit")
    return HttpResponse("ok")

def fengpi(request):
    id = request.GET.get("id")
    mid = request.GET.get("mid")
    cursor = connection.cursor()
    cursor.execute(" update  magazine set cover_id  = '%s' where magazine_id = %s " % (id,mid))
    cursor.execute("commit")
    return HttpResponse("ok")

def insertmag(request):
    title = request.POST.get("title")
    zhuchiren = request.POST.get("zhuchiren")
    date2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cursor = connection.cursor()

    cursor.execute(" SELECT user_id FROM  user where username = '%s' or email = '%s' " % (zhuchiren,zhuchiren) )
    row=cursor.fetchone()

    if row == None :
     user_id = 0
    else:
     user_id = row[0]

    cursor.execute(" SELECT max(phase) FROM `magazine` ")
    row=cursor.fetchone()
    phase=row[0]
    phase=int(phase)+1
        
    
    cursor.execute(" insert into  magazine (`title`,`user_id`,`phase`,`publish_date`) values ('%s','%s','%s','%s') " % (title,user_id,phase,date2))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/mag/')

def insertfl(request):
    name = request.POST.get("name")
    
    cursor = connection.cursor()

    
            
    cursor.execute(" insert into  fan (`name`,`cover_id`) values ('%s','%s') " % (name,0) )
    cursor.execute("commit")
    return http.HttpResponseRedirect('/fllist/')

def insertzi(request):
    name = request.POST.get("name")
    fan_id = request.POST.get("fan_id")
    
    cursor = connection.cursor()

    cursor.execute(" insert into  fan_theme (`name`,`fan_id`,`cover_id`) values ('%s','%s','%s') " % (name,fan_id,0) )
    cursor.execute("commit")

    cursor.execute(" update  fan set themed = 1 where fan_id = %s " % fan_id )
    cursor.execute("commit")
    return http.HttpResponseRedirect('/zilist/')

def updatemag(request):
    title = request.GET.get("title")
    zhuchiren = request.GET.get("zhuchiren")
    id = request.GET.get("id")
    cursor = connection.cursor()

    cursor.execute(" SELECT user_id FROM  user where username = '%s' or email = '%s' " % (zhuchiren,zhuchiren) )
    row=cursor.fetchone()

    if row == None :
     user_id = 0
    else:
     user_id = row[0]
    
    cursor.execute(" update  magazine set title = '%s',user_id = '%s' where magazine_id = '%s' " % (title,user_id,id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/mag/')

def updatefl(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    cursor = connection.cursor()
    cursor.execute(" update  fan set name = '%s' where fan_id = '%s' " % (name,id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/fllist/')

def updateform1(request):
    cursor = connection.cursor()

    fid1 = request.GET.get("fan_id1_1")
    cid1 = request.GET.get("did11")
    rid1 = request.GET.get("rid11")

    fid2 = request.GET.get("fan_id1_2")
    cid2 = request.GET.get("did12")
    rid2 = request.GET.get("rid12")

    fid3 = request.GET.get("fan_id1_3")
    cid3 = request.GET.get("did13")
    rid3 = request.GET.get("rid13")

    fid4 = request.GET.get("fan_id1_4")
    cid4 = request.GET.get("did14")
    rid4 = request.GET.get("rid14")

    fid5 = request.GET.get("fan_id1_5")
    cid5 = request.GET.get("did15")
    rid5 = request.GET.get("rid15")

    fid6 = request.GET.get("fan_id1_6")
    cid6 = request.GET.get("did16")
    rid6 = request.GET.get("rid16")

    fid7 = request.GET.get("fan_id1_7")
    cid7 = request.GET.get("did17")
    rid7 = request.GET.get("rid17")

    fid8 = request.GET.get("fan_id1_8")
    cid8 = request.GET.get("did18")
    rid8 = request.GET.get("rid18")


    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid1,fid1,rid1) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid2,fid2,rid2) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid3,fid3,rid3) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid4,fid4,rid4) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid5,fid5,rid5) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid6,fid6,rid6) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid7,fid7,rid7) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid8,fid8,rid8) )
    cursor.execute("commit")



    return http.HttpResponseRedirect('/shoupei/')

def updateform2(request):
    cursor = connection.cursor()

    fid1 = request.GET.get("fan_id2_1")
    cid1 = request.GET.get("did21")
    rid1 = request.GET.get("rid21")

    fid2 = request.GET.get("fan_id2_2")
    cid2 = request.GET.get("did22")
    rid2 = request.GET.get("rid22")

    fid3 = request.GET.get("fan_id2_3")
    cid3 = request.GET.get("did23")
    rid3 = request.GET.get("rid23")

    fid4 = request.GET.get("fan_id2_4")
    cid4 = request.GET.get("did24")
    rid4 = request.GET.get("rid24")

   


    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid1,fid1,rid1) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid2,fid2,rid2) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid3,fid3,rid3) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid4,fid4,rid4) )
    cursor.execute("commit")

   



    return http.HttpResponseRedirect('/shoupei/')

def updateform3(request):
    cursor = connection.cursor()

    fid1 = request.GET.get("fan_id3_1")
    cid1 = request.GET.get("did31")
    rid1 = request.GET.get("rid31")

    fid2 = request.GET.get("fan_id3_2")
    cid2 = request.GET.get("did32")
    rid2 = request.GET.get("rid32")

    fid3 = request.GET.get("fan_id3_3")
    cid3 = request.GET.get("did33")
    rid3 = request.GET.get("rid33")

    fid4 = request.GET.get("fan_id3_4")
    cid4 = request.GET.get("did34")
    rid4 = request.GET.get("rid34")

   


    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid1,fid1,rid1) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid2,fid2,rid2) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid3,fid3,rid3) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid4,fid4,rid4) )
    cursor.execute("commit")

   



    return http.HttpResponseRedirect('/shoupei/')


def updateform4(request):
    cursor = connection.cursor()

    fid1 = request.GET.get("fan_id4_1")
    cid1 = request.GET.get("did41")
    rid1 = request.GET.get("rid41")

    fid2 = request.GET.get("fan_id4_2")
    cid2 = request.GET.get("did42")
    rid2 = request.GET.get("rid42")

    fid3 = request.GET.get("fan_id4_3")
    cid3 = request.GET.get("did43")
    rid3 = request.GET.get("rid43")



   


    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid1,fid1,rid1) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid2,fid2,rid2) )
    cursor.execute("commit")

    cursor.execute(" update  recommend set target_id = '%s',feed_type='%s' where recommend_id = '%s' " % (cid3,fid3,rid3) )
    cursor.execute("commit")


   



    return http.HttpResponseRedirect('/shoupei/')


def updateform5(request):
   cursor = connection.cursor()

   fid1 = request.GET.get("fan_id5_1")
   cid1 = request.GET.get("did51")
   rid1 = request.GET.get("rid51")
   search1 = request.GET.get("did5_search_1")
   word1 = request.GET.get("did5_word_1")
   url1 = request.GET.get("fan_id5_url_1")

   fid2 = request.GET.get("fan_id5_2")
   cid2 = request.GET.get("did52")
   rid2 = request.GET.get("rid52")
   search2 = request.GET.get("did5_search_2")
   word2 = request.GET.get("did5_word_2")
   url2 = request.GET.get("fan_id5_url_2")

   fid3 = request.GET.get("fan_id5_3")
   cid3 = request.GET.get("did53")
   rid3 = request.GET.get("rid53")
   search3 = request.GET.get("did5_search_3")
   word3 = request.GET.get("did5_word_3")
   url3 = request.GET.get("fan_id5_url_3")





   if fid1 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word1,search1,url1,rid1) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word1,search1,url1,cid1,rid1) )
    cursor.execute("commit")

   if fid2 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word2,search2,url2,rid2) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word2,search2,url2,cid2,rid2) )
    cursor.execute("commit")


   if fid3 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word3,search3,url3,rid3) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=1,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word3,search3,url3,cid3,rid3) )
    cursor.execute("commit")




   


   



    return http.HttpResponseRedirect('/shoupei/')


def updateform6(request):
   cursor = connection.cursor()

   fid1 = request.GET.get("fan_id6_1")
   cid1 = request.GET.get("did61")
   rid1 = request.GET.get("rid61")
   search1 = request.GET.get("did6_search_1")
   word1 = request.GET.get("did6_word_1")
   url1 = request.GET.get("fan_id6_url_1")

   fid2 = request.GET.get("fan_id6_2")
   cid2 = request.GET.get("did62")
   rid2 = request.GET.get("rid62")
   search2 = request.GET.get("did6_search_2")
   word2 = request.GET.get("did6_word_2")
   url2 = request.GET.get("fan_id6_url_2")

   fid3 = request.GET.get("fan_id6_3")
   cid3 = request.GET.get("did63")
   rid3 = request.GET.get("rid63")
   search3 = request.GET.get("did6_search_3")
   word3 = request.GET.get("did6_word_3")
   url3 = request.GET.get("fan_id6_url_3")


   fid4 = request.GET.get("fan_id6_4")
   cid4 = request.GET.get("did64")
   rid4 = request.GET.get("rid64")
   search4 = request.GET.get("did6_search_4")
   word4 = request.GET.get("did6_word_4")
   url4 = request.GET.get("fan_id6_url_4")





   if fid1 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word1,search1,url1,rid1) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word1,search1,url1,cid1,rid1) )
    cursor.execute("commit")

   if fid2 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word2,search2,url2,rid2) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word2,search2,url2,cid2,rid2) )
    cursor.execute("commit")


   if fid3 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word3,search3,url3,rid3) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word3,search3,url3,cid3,rid3) )
    cursor.execute("commit")

   if fid4 == '1':
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=1,user_id=0 where recommend_user_id = '%s' " % (word4,search4,url4,rid4) )
    cursor.execute("commit")
   else:
    cursor.execute(" update  recommend_user set word = '%s',search='%s',url='%s',ishome=0,recommend_type=0,user_id='%s' where recommend_user_id = '%s' " % (word4,search4,url4,cid4,rid4) )
    cursor.execute("commit")




   


   



    return http.HttpResponseRedirect('/shoupei/')




def wodfaninsertuser(request):
   cursor = connection.cursor()

   username = request.GET.get("username")
   realname = request.GET.get("realname")

   cursor.execute(" SELECT * FROM  user where username = '%s' " % username )
   row=cursor.fetchone()
   if row == None:
      return http.HttpResponseRedirect("/wodfanadduser/?msg=用户名有误")
   cursor.execute(" SELECT * FROM  editor where username = '%s' and realname = '%s' " % (username,realname) )
   row1=cursor.fetchone()
   if row1 != None:
      return http.HttpResponseRedirect("/wodfanadduser/?msg=用户名已经提交过")


   cursor.execute(" insert into  editor (`user_id`,`username`,`realname`) values ('%s','%s','%s')  " % (row[0],username,realname) )
   cursor.execute("commit")
   cursor.execute(" update  user set role = 2 where user_id = '%s' " % row[0] )
   cursor.execute("commit")
      


  
   return http.HttpResponseRedirect("/wodfanadduser/?msg=提交成功")




def wodfanadduser(request):
   
    msg = request.GET.get("msg")
    return render_to_response('wodfanadduser.html', locals())



def wodfanuserlist(request):
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM editor group by realname ")
    rows=cursor.fetchall()

    
    return render_to_response('wodfanuserlist.html', locals())




def getrenwu(request):
   cursor = connection.cursor()

   date1 = request.GET.get("date")
   type = request.GET.get("type")
   realname = request.GET.get("realname")
   user_id = request.GET.get("user_id")
   shu = request.GET.get("shu")

   cursor.execute(" SELECT * FROM  job_ft where realname = '%s' and type = '%s' and date = '%s' " % (realname,type,date1) )
   row=cursor.fetchone()

   if row == None:
      cursor.execute(" insert into job_ft (`realname`,`type`,`shu`,`date`) values ('%s','%s','%s','%s') " % (realname,type,shu,date1) )
      cursor.execute("commit")
   else:
      cursor.execute(" update job_ft set shu = '%s' where realname = '%s' and date = '%s' and type = '%s'  " % (shu,realname,date1,type) )
      cursor.execute("commit")
   
   url='/job_ft/'

   if type == '0':
      url='/job_ft/'
   elif type == '1':
      url='/job_dr/'
   elif type == '3':
      url='/job_wd/'
   elif type == '2':
      url='/job_huifu/'
   elif type == '4':
      url='/job_dan/'

   return http.HttpResponseRedirect(url)


def updatezi(request):
    id = request.GET.get("id")
    name = request.GET.get("name12")
    fan_id = request.GET.get("fan_id")
    #return  HttpResponse(name)
    cursor = connection.cursor()
    cursor.execute(" update  fan_theme set name = '%s',fan_id='%s' where fan_theme_id = '%s' " % (name,fan_id,id))
    cursor.execute("commit")
    return http.HttpResponseRedirect('/zilist/')


def addmag(request):
    return render_to_response('addmag.html', locals())

def addfl(request):
    return render_to_response('addfl.html', locals())


def sback(request):
    uuid = request.session.get('uid')
    #return HttpResponse(uuid)
    #uuid = '123'
    return  HttpResponse("ok")

def tuiuser(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" insert into recommend_user (`user_id`,`ishome`) values ('%s','%s') " % (id,1))
    cursor.execute("commit")
    return  HttpResponse("ok")

def qtuiuser(request):
    id = request.GET.get("id")
    cursor = connection.cursor()
    cursor.execute(" delete from recommend_user where user_id = '%s'  " % (id))
    cursor.execute("commit")
    return  HttpResponse("ok")

def jsontest(request):
    
    
    #locations = json.read(s)
    #return HttpResponse(locations['gosee'][0]['maps'])
    #return HttpResponse(locations['gosee'][0]['maps'][0]['width'])
    #cursor = connection.cursor()
    #cursor.execute(" select image_id from  item_image where item_id = 2 ")
    #rows=cursor.fetchall()
    #cc=''
    #for key in rows:
    # cc+="%s%s" % (',',key[0])
    #cchou=cc.find(',')
    #cc=cc[cchou+1:]
    #cursor.execute(" select image_id from  images where position = 0 and image_id in (%s) limit 1 " % cc )
    #rr=cursor.fetchone()
    #cursor = connection.cursor()
    #uuid = str(request.session.get('uid'))
    #cursor.execute(" insert into  uploadlog (`uid`,`date`,`itemid`) values ('%s','%s','%s') " % (uuid,1,123 ) )
    #cursor.execute("commit")
    

    

    return HttpResponse(request.session.get('checkrole'))

def editmag(request):
    id = request.GET.get("id")
    book = Magazine.objects.get(magazine_id=id)
    cursor = connection.cursor()

    cursor.execute(" SELECT user_id FROM  magazine where magazine_id = '%s' " % id )
    row1=cursor.fetchone()    

    cursor.execute(" SELECT username FROM  user where user_id = '%s' " % row1[0] )
    row=cursor.fetchone()

    if row == None :
     username = ''
    else:
     username = row[0]
    return render_to_response('editmag.html', locals())

def editfl(request):
    id = request.GET.get("id")
    book = Fan.objects.get(fan_id=id)
    return render_to_response('editfl.html', locals())

def editzi(request):
    id = request.GET.get("id")
    book = FanTheme.objects.get(fan_theme_id=id)

    #id = request.GET.get("id")
    row1=FanTheme.objects.get(fan_theme_id=id)
    
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM  fan where fan_id != 0 ")
    row=cursor.fetchall()

    return render_to_response('editzi.html', locals())

def pictorial(request):
    nav = 9
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM  magazine where magazine_id != 0 ")
    row=cursor.fetchall()
    mid = request.GET.get("mid")
    return render_to_response('addpict.html', locals())

def addzi(request):
    cursor = connection.cursor()
    nav = 55
    cursor.execute(" SELECT * FROM  fan where fan_id != 0 ")
    row=cursor.fetchall()
    return render_to_response('addzi.html', locals())


def tuipict(request):
    cursor = connection.cursor()
    ttime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cursor.execute(" insert into recommend_pictorial (`pictorial_id`,`user_id`,`recommend_date`) values ('%s','%s','%s')  " % (request.GET.get("id"),0,str(ttime))  )
    cursor.execute("commit")
    return HttpResponse('ok')


def insertdtuijian(request):
    cursor = connection.cursor()
    ttime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    id=request.GET.get("id")
    id=id.rstrip(',')
    cursor.execute(" insert into recommend_item (`item_id`,`image_id`,`recommend_date`) values ('%s','%s','%s')  " % (request.GET.get("danid"),id,str(ttime))  )
    cursor.execute("commit")
    return HttpResponse('ok')


   

def tipai(request):
    cursor = connection.cursor()
    #ttime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    id=request.GET.get("id")
    sort=request.GET.get("sort")
    cursor.execute(" update feed set sort = '%s' where feed_id =  '%s'  " % (sort,id)  )
    cursor.execute("commit")
    return HttpResponse('ok')

def updatedapei(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    theme=request.GET.get("theme")
    theme=theme.rstrip(';')
    theme=theme.strip(';')
    cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (theme,id)  )
    cursor.execute("commit")
    return HttpResponse('ok')

def upbufenlei(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    theme=request.GET.get("theme")

    cursor.execute(" SELECT * FROM  collocation where collocation_id = %s " % id )
    dangqian=cursor.fetchone()
    
    #return HttpResponse(theme.find('f'))

    if(theme.find('f')==-1):

            #return HttpResponse('ok1')
	    cursor.execute(" SELECT * FROM  fan_theme where fan_theme_id = %s " % theme )
	    fantheme=cursor.fetchone()
	       
	    cursor.execute(" SELECT * FROM  fan where fan_id = %s " % fantheme[1] )
	    fan=cursor.fetchone()
		 
	    xinmi1="%s;%s" % (fan[1],fantheme[3])
	    xinmi2=";%s;%s" % (fan[1],fantheme[3])
	    xinmi3="%s;%s" % (dangqian[3],fan[1])
	    xinmi4="%s;%s" % (dangqian[3],fantheme[3])
	    xinmi5="%s;%s;%s" % (dangqian[3],fan[1],fantheme[3])

	    if dangqian[3]=='':
	     cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi1,id)  )
	     cursor.execute("commit")
	    else:
	     dq=dangqian[3]

	     if (dq.find(fan[1])!=-1) and (dq.find(fantheme[3])==-1)  :
	      cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi4,id)  )
	      cursor.execute("commit")

	     elif (dq.find(fan[1])==-1) and (dq.find(fantheme[3])!=-1)  :
	      cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi3,id)  )
	      cursor.execute("commit")

	     elif (dq.find(fan[1])==-1) and (dq.find(fantheme[3])==-1)  :
	      cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi5,id)  )
	      cursor.execute("commit")

    else:
              #return HttpResponse('ok')
	      theme=theme.strip('f')
              cursor.execute(" SELECT * FROM  fan where fan_id = %s " % theme )
	      fan=cursor.fetchone()
	      xinmi3="%s;%s" % (dangqian[3],fan[1])
	      xinmi1="%s" % (fan[1])
	      dq=dangqian[3]
	      if dangqian[3]=='':
	        cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi1,id)  )
	        cursor.execute("commit")
	      elif dq.find(fan[1])==-1:
	        cursor.execute(" update collocation set theme = '%s' where collocation_id = %s  " % (xinmi3,id)  )
	        cursor.execute("commit")

     
    



    cursor.execute(" SELECT theme FROM  collocation where collocation_id = %s " % id )
    gaihou=cursor.fetchone()
    gaihous=gaihou[0]

    return HttpResponse(gaihous)


def tuidapei(request):
    cursor = connection.cursor()
    ttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    id=request.GET.get("id")
    height=request.GET.get("height")
    image_id=request.GET.get("image_id")
    cursor.execute(" select title from collocation where collocation_id = %s " % id )
    title=cursor.fetchone()
    cursor.execute(" select user_id from user_collocation where isown = 1 and collocation_id = %s " % id )
    user_id=cursor.fetchone()
    if(user_id==None):
     return HttpResponse('ok')
    cursor.execute(" insert into recommend_feed (`target_id`,`user_id`,`parent_id`,`feed_type`,`image_id`,`publish_date`,`height`,`title`) values ('%s','%s','%s','%s','%s','%s','%s','%s')  " % (id,user_id[0],0,request.GET.get("isset"),image_id,str(ttime),height,title[0])  )
    cursor.execute("commit")
    return HttpResponse('ok')

def tuiblog(request):
    cursor = connection.cursor()
    ttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    id=request.GET.get("id")
    height=request.GET.get("height")
    batch_no=request.GET.get("batch_no")
    try:
     cursor.execute(" select picture_id from pictures where batch_no = %s limit 1 " % batch_no )
     isa=cursor.fetchone()
     image_id=isa[0]
    except:
     image_id=0
    cursor.execute(" select title from blog where blog_id = %s " % id )
    title=cursor.fetchone()
    cursor.execute(" select user_id from user_blog where isown = 1 and blog_id = %s " % id )
    user_id=cursor.fetchone()
    if(user_id==None):
     return HttpResponse('ok')
    cursor.execute(" insert into recommend_feed (`target_id`,`user_id`,`parent_id`,`feed_type`,`image_id`,`publish_date`,`height`,`title`) values ('%s','%s','%s','%s','%s','%s','%s','%s')  " % (id,user_id[0],0,2,image_id,str(ttime),height,title[0])  )
    cursor.execute("commit")
    return HttpResponse('ok')

def qudapei(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    cursor.execute(" delete from recommend_feed where target_id = %s and (feed_type = 0 or feed_type = 1) " % id )    
    cursor.execute("commit")
    return HttpResponse('ok')

def fuckst(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    score=request.GET.get("score")
    type=request.GET.get("type")

    cursor.execute(" select * from score where target_id = '%s' and type = '%s' " % (id,type) )
    row=cursor.fetchone()

    if row == None:        
       cursor.execute(" insert into score (`target_id`,`type`,`score`) values ('%s','%s','%s')  " % (id,type,score))
       cursor.execute("commit")
    else:
       cursor.execute(" update score set score = '%s' where target_id = '%s' and type = '%s' " % (score,id,type))
       cursor.execute("commit")

    return HttpResponse('ok')

def qublog(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    cursor.execute(" delete from recommend_feed where target_id = %s and feed_type = 2 " % id )    
    cursor.execute("commit")
    return HttpResponse('ok')

def shedai(request):
    cursor = connection.cursor()

    id=request.GET.get("id")

    cursor.execute(" SELECT item_id FROM  item_image where image_id = '"+str(id)+"' limit 1 ") 
    row1 = cursor.fetchone()

    cursor.execute(" SELECT position FROM  images where image_id = '"+str(id)+"' limit 1 ") 
    fs = cursor.fetchone()

    tablename = 'item_image'
    cursor.execute(" SELECT image_id FROM  "+tablename+" where image_id != '"+str(id)+"' and item_id = '"+str(row1[0])+"'") 
    row = cursor.fetchall()
    cc123=''
    for key in row:
     cc123+="%s%s" % (',',key[0])
    cchou=cc123.find(',')
    cc123=cc123[cchou+1:]

    cursor.execute(" update images set position = "+str(fs[0])+" where position =  0 and image_id in (%s) " % cc123 )    
    cursor.execute("commit")

    cursor.execute(" update images set position = 0 where image_id =  %s " % id )    
    cursor.execute("commit")
    return HttpResponse('ok')

def shandai(request):
    cursor = connection.cursor()
    id=request.GET.get("id")
    cursor.execute(" update images set isdelete = 1 where image_id =  %s " % id )    
    cursor.execute("commit")
    cursor.execute(" update item_image set isdelete = 1 where image_id =  %s " % id )    
    cursor.execute("commit")
    return HttpResponse('ok')

def qupict(request):
    cursor = connection.cursor()
    ttime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cursor.execute(" delete from recommend_pictorial where `pictorial_id` = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def qudan(request):
    cursor = connection.cursor()
    cursor.execute(" delete from recommend_item where item_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def quchen(request):
    cursor = connection.cursor()
    cursor.execute(" update fashion set sort = 1 where  fashion_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def chen(request):
    cursor = connection.cursor()
    cursor.execute(" update fashion set sort = -1 where  fashion_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')


def quchendaren(request):
    cursor = connection.cursor()
    cursor.execute(" update talent set sort = 1 where  talent_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def chendaren(request):
    cursor = connection.cursor()
    cursor.execute(" update talent set sort = -1 where  talent_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def quchenqa(request):
    cursor = connection.cursor()
    cursor.execute(" update qa set sort = 1 where  qa_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def chenqa(request):
    cursor = connection.cursor()
    cursor.execute(" update qa set sort = -1 where  qa_id = '%s'  " % (request.GET.get("id"))  )
    cursor.execute("commit")
    return HttpResponse('ok')

def editpict(request):
    nav = 9
    id = request.GET.get("id")
    row1=Pictorial.objects.get(pictorial_id=id)
    try:
     befresult = Pictresult.objects.get(pid=id)
    except:
     befresult = ''
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM  magazine where magazine_id != 0 ")
    row=cursor.fetchall()
    #cursor = connection.cursor()
    #cursor.execute(" SELECT * FROM  pictorial where magazine_id != 0 ")
    #row=cursor.fetchall()
    return render_to_response('editpict.html', locals())

def kongzhi(request):
    nav = 17
    id = request.GET.get("id")    
    cursor = connection.cursor()
    cursor.execute(" SELECT url FROM  images where image_id = "+str(id)+"  limit 1 ") 
    row=cursor.fetchone()
    url = row[0]
    return render_to_response('kongzhi.html', locals())


def tongguo(request):
    s_time=request.GET.get("s_time")
    e_time=request.GET.get("e_time")
    s_time=time.mktime(time.strptime(s_time,"%Y-%m-%d %H:%M:%S"))
    e_time=time.mktime(time.strptime(e_time,"%Y-%m-%d %H:%M:%S"))
    s_time=int(s_time)
    e_time=int(e_time)
    cursor = connection.cursor()
    cursor.execute(" select itemid from  uploadlog where date >= %s and date <= %s " % (s_time,e_time) )
    rows3=cursor.fetchall()
    cc=''
    for key in rows3:
      cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" update items set review = 1 where item_id in (%s) " % cc )
    cursor.execute("commit")
    return HttpResponse('ok')


def insertpict(request):
    
    cursor = connection.cursor()
    
    cursor.execute(" insert into  pictorial (`magazine_id`,`title`,`url`,`email`,`description`) values ('%s','%s','%s','%s','%s') " % (request.GET.get("mag"),request.GET.get("title"),request.GET.get("img"),request.GET.get("email"),request.GET.get("des"))   )
    cursor.execute("commit")
    cursor.execute(" SELECT LAST_INSERT_ID(); ")
    pid=cursor.fetchone()
    cursor.execute(" insert into  pictresult (`pid`,`result`) values ('%s','%s') " % (pid[0],str(request.GET.get("result")))   )
    cursor.execute("commit")
    result = request.GET.get("result")
    result = str(result)
    locations = json.read(result)
    for j in range(len(locations['gosee'])):
     top=int(locations['gosee'][j]['top'])
     left=int(locations['gosee'][j]['left'])
     width=int(locations['gosee'][j]['width'])
     height=int(locations['gosee'][j]['height'])
     item_id=int(locations['gosee'][j]['item_id'])
     cursor = connection.cursor()
     cursor.execute(" select image_id from  item_image where item_id = %s " % item_id)
     rows3=cursor.fetchall()
     cc=''
     for key in rows3:
      cc+="%s%s" % (',',key[0])
     cchou=cc.find(',')
     cc=cc[cchou+1:]
     cursor.execute(" select image_id from  images where position = 0 and image_id in (%s) limit 1 " % cc )
     image_id=cursor.fetchone()
     cursor.execute(" insert into  gosee (`pictorial_id`,`item_id`,`image_id`,`left_margin`,`top_margin`,`width`,`height`) values ('%s','%s','%s','%s','%s','%s','%s') " % (pid[0],item_id,image_id[0],left,top,width,height) )
     cursor.execute(" SELECT LAST_INSERT_ID(); ")
     goseeid=cursor.fetchone()
     for h in range(len(locations['gosee'][j]['maps'])):
      cursor.execute(" insert into  item_pictorial (`pictorial_id`,`left_margin`,`top_margin`,`width`,`height`,`gosee_id`) values ('%s','%s','%s','%s','%s','%s') " % (pid[0],int(locations['gosee'][j]['maps'][h]['left']),int(locations['gosee'][j]['maps'][h]['top']),int(locations['gosee'][j]['maps'][h]['width']),int(locations['gosee'][j]['maps'][h]['height']),int(goseeid[0]) )  )
      cursor.execute("commit")
    
      
    return HttpResponse('ok')


def testchmod(request):
    #os.chown(name, "shensl", "shensl")
    #os.chmod(name,0777)
    #os.chown("/home/shensl/Spiders/pictorial", "shensl", "shensl")
    #os.chmod("/home/shensl/Spiders/pictorial",0777)
    os.system(" chown -R shensl:shensl /home/shensl/Spiders/pictorial ")
    os.system(" chmod -R 777 /home/shensl/Spiders/pictorial ")
    

    
    return HttpResponse('ok')


def updatepict(request):
    
    cursor = connection.cursor()
    
    cursor.execute(" update pictorial set `magazine_id` = '%s',`title`= '%s',`url`= '%s',`email`= '%s',`description`= '%s' where pictorial_id = %s  " % (request.GET.get("mag"),request.GET.get("title"),request.GET.get("img"),request.GET.get("email"),request.GET.get("des"),request.GET.get("pid"))   )
    cursor.execute("commit")
    
    cursor.execute(" select * from  pictresult where pid =  %s " % (request.GET.get("pid")) )
    rows13=cursor.fetchone()
    if(rows13 == None):
     cursor.execute(" insert into  pictresult (`pid`,`result`) values ('%s','%s') " % (request.GET.get("pid"),str(request.GET.get("result")))   )
     cursor.execute("commit")
    else:
     cursor.execute(" update  pictresult set `result` = '%s' where pid = '%s' " % (str(request.GET.get("result")),request.GET.get("pid"))   )
     cursor.execute("commit")

    pid=request.GET.get("pid")
    result = request.GET.get("result")
    result = str(result)
    locations = json.read(result)
    if(len(locations['gosee']) != 0):
            cursor = connection.cursor()
            cursor.execute(" delete from gosee where `pictorial_id` = %s " % pid)
            cursor.execute("commit")
	    cursor.execute(" delete from item_pictorial where `pictorial_id` = %s " % pid)
            cursor.execute("commit")
	    for j in range(len(locations['gosee'])):
	     top=int(locations['gosee'][j]['top'])
	     left=int(locations['gosee'][j]['left'])
	     width=int(locations['gosee'][j]['width'])
	     height=int(locations['gosee'][j]['height'])
	     item_id=int(locations['gosee'][j]['item_id'])
	     
	     cursor.execute(" select image_id from  item_image where item_id = %s " % item_id)
	     rows3=cursor.fetchall()
	     cc=''
	     for key in rows3:
	      cc+="%s%s" % (',',key[0])
	     cchou=cc.find(',')
	     cc=cc[cchou+1:]
	     cursor.execute(" select image_id from  images where position = 0 and image_id in (%s) limit 1 " % cc )
	     image_id=cursor.fetchone()
	     cursor.execute(" insert into  gosee (`pictorial_id`,`item_id`,`image_id`,`left_margin`,`top_margin`,`width`,`height`) values ('%s','%s','%s','%s','%s','%s','%s') " % (pid,item_id,image_id[0],left,top,width,height) )
	     cursor.execute(" SELECT LAST_INSERT_ID(); ")
	     goseeid=cursor.fetchone()
	     for h in range(len(locations['gosee'][j]['maps'])):
	      cursor.execute(" insert into  item_pictorial (`pictorial_id`,`left_margin`,`top_margin`,`width`,`height`,`gosee_id`) values ('%s','%s','%s','%s','%s','%s') " % (pid,int(locations['gosee'][j]['maps'][h]['left']),int(locations['gosee'][j]['maps'][h]['top']),int(locations['gosee'][j]['maps'][h]['width']),int(locations['gosee'][j]['maps'][h]['height']),int(goseeid[0]) )  )
	      cursor.execute("commit")
      
    return HttpResponse('ok')
    
    
    
    
    




    
    
    

   
    

    














    





