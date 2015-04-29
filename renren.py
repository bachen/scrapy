#coding=utf-8
import urllib2,urllib,cookielib
import time,thread
import sys
sys.path.append('/crawler')
from crawler import basic


datas = urllib.urlencode({'email':'cbl198903@163.com','password':'cbl1989'})
renren = basic.basic_crawler('http://www.renren.com/ajaxLogin',datas)
renren.initOpener()
renren.get_cookie()
