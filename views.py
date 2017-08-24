#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from models import *
from django.db.models import F
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
import datetime
from my import settings
import sys


def hello(request):
    vo = '123'
    person = ['apples', 'bananas', 'carrots']
    p1={'name': ['apples', 'bananas', 'carrots'], 'age': '43'}
    cursor = connection.cursor()
    tablename = 'user'
    cursor.execute(" SELECT * FROM  "+tablename+" where id != 0 ") 
    #row = cursor.fetchone()
    fields = dict([(field[0],cursor.description.index(field)) for field  in  cursor.description])
    #row=cursor.fetchall()
  
    #sys.exit()
    #return row
    #print row
    vo = "不是不是"
    #vo = unicode(vo,'gbk')
    #return render_to_response('footer.html', locals())
    return HttpResponse(fields['name'])

def sc(request):
    #request.session["fav_color"] = "blue"
    vac=request.session.get('fav_color')
    request.session.set_expiry(0)
    return HttpResponse(vac)

def see(request):
    del request.session['fav_color']
    return HttpResponse('123')


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({'vo': '123'}))
    return render_to_response('index.html', locals())

def getc(request, month, day):
    #values = request.META.items()
    #values.sort()
    #html = []
    #for k, v in values:
    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return HttpResponse(day)

def db(request):
    list = User.objects.all()
    return render_to_response('footer.html', locals())

def test(request):
    cursor = connection.cursor()
    cursor.execute(" select itemid from admin_job  where userid = 2 ")
    #person = ['apples', 'bananas', 'carrots']
    row = cursor.fetchall()
    #','.join(names)
    str=''
    for rec in row:
       str = str +'%s,' %  rec[0]
    str = str.rstrip(',')
     
    return render_to_response('footer.html', locals())

def page(request):
    #books = User.objects.raw('SELECT id as id, num as num FROM test')#raw方法结果需要用tuple强转一下
    #articles = tuple(articles) 用raw方法要转换
    #books = Book.objects.all() #之前需要从models中导入Book
    #books = User.objects.all()
    #books=User.objects.filter( Q(id__gt='0') | Q(id__lt='0') ).order_by("-id")[0:1]
    #books=User.objects.filter(  ~Q(id = '0') ).order_by("-id").exclude(id=3)
    books=User.objects.filter(  ~Q(id = '0') ).order_by("-id").exclude(id=1)
    after_range_num = 5        #当前页前显示5页
    befor_range_num = 4       #当前页后显示4页
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
     page = int(request.GET.get("page",1))
     if page < 1:
      page = 1
    except ValueError:
     page = 1
    paginator = Paginator(books,1)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
     books = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
     books = paginator.page(paginator.num_pages)
    if page >= after_range_num:
     page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
     page_range = paginator.page_range[0:int(page)+befor_range_num]

    return render_to_response('page.html', locals())
    
    #return render_to_response('page.html',{'books':books_list,'page_range':page_range})



def md5(request):
    import hashlib

    m = hashlib.md5('admin')

    m.digest()

    return HttpResponse(m.hexdigest())

def zip(request):
    import zipfile, os
    filename = '%s%s' % (settings.STATIC_PATH, "/test.zip")
    testdir = '%s%s' % (settings.STATIC_PATH, "/test")
    z = zipfile.ZipFile(filename, 'w') # 注意这里的第二个参数是w，这里的filename是压缩包的名字
    #假设要把一个叫testdir中的文件全部添加到压缩包里（这里只添加一级子目录中的文件）：
    if os.path.isdir(testdir):
     for d in os.listdir(testdir):
      z.write(testdir+os.sep+d)
    z.close()
    return HttpResponse('123')

def copy(request):
    import shutil
    import os
    shutil.copy('E:/wodfan/my/images/test/123.txt', 'E:/wodfan/my/1234.txt') 
    return HttpResponse('123')










    





