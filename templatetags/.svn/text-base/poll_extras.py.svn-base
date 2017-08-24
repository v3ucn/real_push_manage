#coding=utf-8
from django import template
from my.models import *
from django.db.models import F
from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
import datetime
import sys
register = template.Library()  

def lower123(value):
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
     imgstr=row456[1]
     imgstr=imgstr.replace('.jpg','_340x340.jpg')
    else:
     imgstr='123'
    return imgstr

def lower125(value):
    cursor = connection.cursor()
    tablename = 'item_image'
    cursor.execute(" SELECT image_id FROM  "+tablename+" where item_id = '"+str(value)+"'") 
    rows = cursor.fetchall()
    ccff=''
    for key in rows:
     ccff+="%s%s" % (',',key[0])
    cchou=ccff.find(',')
    ccff=ccff[cchou+1:]
    ccff=ccff.strip()
    #return ccff
    sql=" select * from images where position = 0 and  image_id in ("+ccff+") limit 1 "

    try:
     cursor.execute(sql) 
     row456 = cursor.fetchone()
    except:
     row456='123'
    if row456 != '123':
     imgstr=row456[0]
     #imgstr=imgstr.replace('.jpg','_340x340.jpg')
    else:
     imgstr='123'
    return imgstr

def lowerdapei(value):
    cursor = connection.cursor()
    #tablename = 'images'
    imgstr = '123'
    try:
     cursor.execute(" SELECT * FROM  looks where look_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()
     if row != None:
      imgstr=row[1]
      return imgstr
     else:
      return '123'
    except:
     return '123'

def getcid(value):
    cursor = connection.cursor()
    cursor.execute(" SELECT target_id FROM feed where feed_id = '"+str(value)+"' limit 1 ") 
    row = cursor.fetchone()
    if row == None:
     return 123;
    else:
     return row[0]

def getusername(value):
    cursor = connection.cursor()
    cursor.execute(" SELECT username FROM user where user_id = '"+str(value)+"' limit 1 ") 
    row = cursor.fetchone()
    if row == None:
     return 123;
    else:
     return row[0]
    

def getfanname(value):
    cursor = connection.cursor()
    imgstr = '123'
    try:
     cursor.execute(" SELECT name FROM  fan where fan_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()
     if row != None:
      imgstr=row[0]
      return imgstr
     else:
      return '123'
    except:
     return '123'

def lowerdapei1(value):
    cursor = connection.cursor()
    #return value
    
    cursor.execute(" SELECT target_id FROM  feed where feed_id = '"+str(value)+"' limit 1 ") 
    row3 = cursor.fetchone()
    
    try:
     cursor.execute(" SELECT look_id FROM  collocation where collocation_id = '%s' limit 1 " % row3[0] ) 
     row2 = cursor.fetchone()
    except:
     row2=None
    if row2 == None:
     return 'not find'
    else :
     cid = row2[0]
    #return cid

    try:
     cursor.execute(" SELECT * FROM  looks where look_id = '"+str(cid)+"' limit 1 ") 
     row = cursor.fetchone()
     if row != None:
      imgstr=row[1]
      return imgstr
     else:
      return '123'
    except:
     return '123'


def lowerfeed(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT iscollocation,url FROM  figure where position = 0 and fashion_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
    except:
     return '123'
    if row != None:
	    if(row[0]==1):
	     #cursor.execute(" SELECT * FROM  pictures where  picture_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 == None:
	     # return '123'
	     #else:
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])
	      
	    else:
	     #cursor.execute(" SELECT * FROM  looks where look_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 != None:
	     # return "%s%s" % ("http://www.wodfan.com/images/pictures",row1[1])
	     #else:
	     # return '123'
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
            return '123'

def lowerqa(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT iscollocation,url FROM  qaImages where position = 0 and qa_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
    except:
     return '123'
    if row != None:
	    if(row[0]==1):
	     #cursor.execute(" SELECT * FROM  pictures where  picture_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 == None:
	     # return '123'
	     #else:
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])
	      
	    else:
	     #cursor.execute(" SELECT * FROM  looks where look_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 != None:
	     # return "%s%s" % ("http://www.wodfan.com/images/pictures",row1[1])
	     #else:
	     # return '123'
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
            return '123'

def lowerte(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT iscollocation,url FROM  photo where position = 0 and talent_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
    except:
     return '123'
    if row != None:
	    if(row[0]==1):
	     #cursor.execute(" SELECT * FROM  pictures where  picture_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 == None:
	     # return '123'
	     #else:
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])
	      
	    else:
	     #cursor.execute(" SELECT * FROM  looks where look_id = '"+str(row[1])+"' limit 1 ") 
	     #row1 = cursor.fetchone()
	     #if row1 != None:
	     # return "%s%s" % ("http://www.wodfan.com/images/pictures",row1[1])
	     #else:
	     # return '123'
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
    else:
            return '123'

def lowerblog(value):
    cursor = connection.cursor()
    #tablename = 'images'
    try:
     cursor.execute(" SELECT * FROM  pictures where batch_no = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
     imgstr=row[1]
     return imgstr
    except:
     return value

def tuijian(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT * FROM  recommend where pictorial_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
     if row == None:
      return '未推荐'
     else:
      return '已推荐'
    except:
     return '未推荐'

def dantuijian(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT * FROM  recommend_item where item_id = '"+str(value)+"' limit 1 ") 
     row = cursor.fetchone()    
     if row == None:
      return '未推荐'
     else:
      return '已推荐'
    except:
     return '未推荐'

def fengpi(value):
    cursor = connection.cursor()
    cursor.execute(" SELECT magazine_id FROM pictorial  where pictorial_id = '"+str(value)+"' limit 1 ") 
    row = cursor.fetchone()
    mid=row[0]
    cursor.execute(" SELECT cover_id FROM magazine  where magazine_id = '"+str(mid)+"' limit 1 ") 
    row = cursor.fetchone()

    if(row[0] == value):
     return '已选为封皮'
    else:
     return '未选为封皮'

def magon(value):
    cursor = connection.cursor()
    cursor.execute(" SELECT ishome FROM magazine  where magazine_id = '"+str(value)+"' limit 1 ") 
    row = cursor.fetchone()
    #return row[0]
    imgstr=''
    if(row[0] == 0):
     imgstr+="本期杂志前台显示状态:未显示<input type='button' value='点击显示' onclick='xianshi("+str(value)+")'  \/>"
    else:
     imgstr+="本期杂志前台显示状态:已显示<input type='button' value='点击关闭' onclick='guanbi("+str(value)+")'  \/>"
    
    return imgstr
     

def dapeituijian(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT * FROM  recommend_feed where target_id = '"+str(value)+"' and (feed_type=0 or feed_type=1) limit 1 ") 
     row = cursor.fetchone()    
     if row == None:
      return '未推荐'
     else:
      return '已推荐'
    except:
     return '未推荐'

def blogtuijian(value):
    cursor = connection.cursor()
    try:
     cursor.execute(" SELECT * FROM  recommend_feed where target_id = '"+str(value)+"' and feed_type = 2 limit 1 ") 
     row = cursor.fetchone()    
     if row == None:
      return '未推荐'
     else:
      return '已推荐'
    except:
     return '未推荐'

def lower124(value):
    cursor = connection.cursor()
    tablename = 'item_image'
    cursor.execute(" SELECT image_id FROM  "+tablename+" where item_id = '"+str(value)+"'") 
    rows = cursor.fetchall()
    ccff=''
    for key in rows:
     ccff+="%s%s" % (',',key[0])
    cchou=ccff.find(',')
    ccff=ccff[cchou+1:]
    ccff=ccff.strip()
    #return ccff
    sql=" select * from images where position = 0 and  image_id in ("+ccff+") limit 1 "

    try:
     cursor.execute(sql) 
     row456 = cursor.fetchone()
    except:
     row456='123'
    if row456 != '123':
     imgstr=row456[1]
     #imgstr=imgstr.replace('.jpg','_180x1024.jpg')
    else:
     imgstr='123'
    return imgstr

def fuck(value):
    cursor = connection.cursor()
    tablename = 'item_image'
    cursor.execute(" SELECT image_id FROM  "+tablename+" where isdelete = 0 and item_id = '"+str(value)+"'") 
    row = cursor.fetchall()
    cc123=''
    for key in row:
     cc123+="%s%s" % (',',key[0])
    cchou=cc123.find(',')
    cc123=cc123[cchou+1:]
    try:
     cursor.execute(" SELECT * FROM  images where image_id in ("+str(cc123)+") limit 14") 
     rows = cursor.fetchall()
    except:
     rows = '123'
    if rows == '123':
       imgstr='123'
    else :
       imgstr=''
       for j in range(len(rows)):
        cc=str(rows[j][1])
	imgid=str(rows[j][0])
	cc2=str(rows[j][1])
	cc=cc.replace('.jpg','_180x1024.jpg')
	c4=cc2.replace('.jpg','_340x340.jpg')
	id=str(rows[j][0])
        imgstr+="<img class='xiaoc' imgid='"+imgid+"' fuckstr='http://ifan.me:8081/images"+c4+"' fuckid='"+str(value)+"'  style='float:left;margin-right:3px;border:1px solid black;margin-top:2ppx;width:62px;height:62px;' src='http://ifan.me:8081/images"+cc+"'   /> " 
    return imgstr


def bianlogz(value,v2):
    cursor = connection.cursor()
    
    if v2 == '':
     cursor.execute(" SELECT count(storage_id) FROM storage where user_id = '%s' " % value )
    else:
     d1="%s%s" % (v2," 00:00:00")
     d2="%s%s" % (v2," 23:59:59")
     cursor.execute(" SELECT count(storage_id) FROM storage where user_id = '%s' and publish_date >='%s' and publish_date <='%s'  " % (value,d1,d2) )
    
    rows = cursor.fetchone()
    fuck = rows[0]

    return fuck


def mabi1(value):
    cursor = connection.cursor()
    cursor.execute(" SELECT * FROM recommend_user where recommend_user_id = '%s' " % value )
    row = cursor.fetchone()

    if row[6] == 0:
       cursor.execute(" SELECT url FROM user where user_id = '%s' " % row[1] )
       row1 = cursor.fetchone()
       fuck='%s%s' % ("http://www.wodfan.com/images/avatar",row1[0])
       return fuck
    else:
       return row[5]

def getst(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT score FROM score where target_id = '%s' and type = '%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]

def getrenwu(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT shu FROM job_ft where realname = '%s' and type = 0 and date='%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]

def getrenwu1(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT shu FROM job_ft where realname = '%s' and type = 1 and date='%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]

def getrenwu2(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT shu FROM job_ft where realname = '%s' and type = 3 and date='%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]

def getrenwu3(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT shu FROM job_ft where realname = '%s' and type = 2 and date='%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]


def getrenwu4(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT shu FROM job_ft where realname = '%s' and type = 4 and date='%s' " % (value,v2) )
    row = cursor.fetchone()

    if row == None:
       return 0
    else:
       return row[0]


def getftday(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(fashion_id) FROM  fashion where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+" 00:00:00' and '"+str(v2)+" 23:59:59'    "  ) 
    row1 = cursor.fetchone()
    return row1[0]


def getdrday(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(talent_id) FROM  talent where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+" 00:00:00' and '"+str(v2)+" 23:59:59'    "  ) 
    row1 = cursor.fetchone()
    return row1[0]


def getftdayscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM fashion where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+" 00:00:00' and '"+str(v2)+" 23:59:59'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        return row1[0]
    else :
     return '0'


def getdrdayscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM talent where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+" 00:00:00' and '"+str(v2)+" 23:59:59'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        return row1[0]
    else :
     return '0'

def getftmonthscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM fashion where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        return row1[0]
    else :
     return '0'


def getdrmonthscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM talent where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        return row1[0]
    else :
     return '0'

def getftmonthavgscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM fashion where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        zong=int(row1[0])
	zong1=zong/30
        return zong1
    else :
     return '0'

def getdrmonthavgscore(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]

    #return cc

    cursor.execute(" SELECT user_id FROM talent where user_id in ("+str(cc)+") and  publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'  " ) 
    rowsc = cursor.fetchall()
    imgstr123=rowsc
    cc1=''
    for key in imgstr123:
        cc1+="%s%s" % (',',key[0])
    cchou123=cc1.find(',')
    cc1=cc1[cchou123+1:]

    if cc1 != '':
     sql = " SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0 "
     #return sql
     cursor.execute(" SELECT sum(score) as ss11 FROM score where target_id in ("+str(cc1)+") and type = 0    "  ) 
     row1 = cursor.fetchone()
     if row1 != None:
        return '0'
     else:
        zong=int(row1[0])
	zong1=zong/30
        return zong1
    else :
     return '0'

def getftmonth(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(fashion_id) FROM  fashion where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'          "  ) 
    row1 = cursor.fetchone()
    return row1[0]

def getdrmonth(value,v2):
    cursor = connection.cursor()
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(talent_id) FROM  talent where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'          "  ) 
    row1 = cursor.fetchone()
    return row1[0]

def getftmonthsheding(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 0 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    if row == None:
       return '0'
    else:
       return row[0]

def getbackground(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 0 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    if row == None:
       return "style='background:gray;'"
    else:
       return ""

def getbackground1(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 1 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    if row == None:
       return "style='background:gray;'"
    else:
       return ""

def getdrmonthsheding(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 1 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    if row == None:
       return '0'
    else:
       return row[0]

def getftmonthchae(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 0 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    sheding = 0
    if row != None:
        sheding = row[0]
    
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(fashion_id) FROM  fashion where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'          "  ) 
    row1 = cursor.fetchone()
    chae = sheding - row1[0]
    return chae

def getdrmonthchae(value,v2):
    cursor = connection.cursor()
    v2=v2[0:7]
    cursor.execute(" SELECT shu FROM  job_ft where realname = '%s' and type = 1 and date = '%s'  " % (value,v2) ) 
    row = cursor.fetchone()
    sheding = 0
    if row != None:
        sheding = row[0]
    
    cursor.execute(" SELECT user_id FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    v2=v2[0:7]
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    cursor.execute(" SELECT count(talent_id) FROM  talent where user_id in ("+str(cc)+") and publish_date between '"+str(v2)+"-01' and '"+str(v2)+"-31'          "  ) 
    row1 = cursor.fetchone()
    chae = sheding - row1[0]
    return chae


def wodfanuserlist(value):
    cursor = connection.cursor()
      
    cursor.execute(" SELECT username FROM  editor where realname = '%s' " % value ) 
    row = cursor.fetchall()
    imgstr=row
    cc=''
    for key in imgstr:
        cc+="%s%s" % (',',key[0])
    cchou=cc.find(',')
    cc=cc[cchou+1:]
    return cc
    
       

def mabi(value,v2):
    cursor = connection.cursor()

    if v2 == 0:
        try:
         cursor.execute(" SELECT iscollocation,url FROM  figure where position = 0 and fashion_id = '"+str(value)+"' limit 1 ") 
         row = cursor.fetchone()    
        except:
         return '123'
	if row != None:
	    if(row[0]==1):
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
        else:
            return '123'
    elif v2 == 1:
        try:
         cursor.execute(" SELECT iscollocation,url FROM  photo where position = 0 and talent_id = '"+str(value)+"' limit 1 ")
         row = cursor.fetchone()    
        except:
         return '123'
	if row != None:
	    if(row[0]==1):
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
        else:
            return '123'

    elif v2 == 2:
         tablename = 'item_image'
         cursor.execute(" SELECT image_id FROM  "+tablename+" where item_id = '"+str(value)+"'") 
         rows = cursor.fetchall()
         ccff=''
         for key in rows:
          ccff+="%s%s" % (',',key[0])
         cchou=ccff.find(',')
         ccff=ccff[cchou+1:]
         ccff=ccff.strip()
         #return ccff
         sql=" select * from images where position = 0 and  image_id in ("+ccff+") limit 1 "
         try:
          cursor.execute(sql) 
          row456 = cursor.fetchone()
         except:
          row456='123'
         if row456 != '123':
          #imgstr=row456[1]
	  imgstr="%s%s" % ("http://ifan.me:8081/images",row456[1])
          #imgstr=imgstr.replace('.jpg','_340x340.jpg')
         else:
          imgstr='123'
         return imgstr
    elif v2 == 3:
        try:
         cursor.execute(" SELECT iscollocation,url FROM  qaImages where position = 0 and qa_id = '"+str(value)+"' limit 1 ")
         row = cursor.fetchone()    
        except:
         return '123'
	if row != None:
	    if(row[0]==1):
	      return "%s%s" % ("http://www.wodfan.com/images/collocation",row[1])	      
	    else:
	      return "%s%s" % ("http://www.wodfan.com/images/pictures",row[1])
        else:
            return '123'          

        

    
    

def yonghupanduan(value):
    cursor = connection.cursor()
    
    cursor.execute(" SELECT user_id FROM recommend_user where ishome = 1 and user_id = '%s'   " % (value) )
    row = cursor.fetchone()
    if row == None:
     return '未推荐'
    else:
     return '已推荐'




def getbianji(value):
    if value=='pp':
       return '潘黎'
    elif value =='潘潘':
       return '潘黎'
    elif value == 'boy':
       return '郑瑞萦'
    elif value == 'little j':
       return '李诗蔚'
    elif value == 'vivienne':
       return '孙菁'
    elif value == 'Vannesa':
       return '张月馨'
    else:
       return ''
    



register.filter(lower123)
register.filter(lower124)
register.filter(lower125)
register.filter(lowerdapei)
register.filter(lowerdapei1)
register.filter(tuijian)
register.filter(dantuijian)
register.filter(dapeituijian)
register.filter(lowerblog)
register.filter(getfanname)
register.filter(blogtuijian)
register.filter(lowerfeed)
register.filter(fengpi)
register.filter(fuck)
register.filter(magon)
register.filter(getcid)
register.filter(bianlogz)
register.filter(getbianji)
register.filter(lowerqa)
register.filter(lowerte)
register.filter(yonghupanduan)
register.filter(getusername)
register.filter(mabi)
register.filter(mabi1)
register.filter(getst)
register.filter(getrenwu)
register.filter(getrenwu1)
register.filter(getrenwu2)
register.filter(getrenwu3)
register.filter(getrenwu4)
register.filter(getftday)
register.filter(getdrday)
register.filter(getftdayscore)
register.filter(getdrdayscore)
register.filter(getftmonthscore)
register.filter(getdrmonthscore)
register.filter(getftmonthavgscore)
register.filter(getdrmonthavgscore)
register.filter(getftmonth)
register.filter(getdrmonth)
register.filter(getftmonthsheding)
register.filter(getdrmonthsheding)
register.filter(getftmonthchae)
register.filter(getdrmonthchae)
register.filter(wodfanuserlist)
register.filter(getbackground)
register.filter(getbackground1)